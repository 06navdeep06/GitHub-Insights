import os
from typing import Dict, List, Optional, Union
import requests
from dotenv import load_dotenv

class GitHubAPI:
    """A client for interacting with the GitHub API."""
    
    BASE_URL = "https://api.github.com"
    
    def __init__(self, token: str = None):
        """Initialize the GitHub API client.
        
        Args:
            token: GitHub Personal Access Token. If not provided, will try to load from .env file.
        """
        if token is None:
            load_dotenv()
            token = os.getenv("GITHUB_TOKEN")
            
        if not token:
            raise ValueError(
                "GitHub token not provided. Please set GITHUB_TOKEN environment variable "
                "or pass it as an argument."
            )
            
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """Make a GET request to the GitHub API.
        
        Args:
            endpoint: API endpoint (e.g., '/users/username/repos')
            params: Optional query parameters
            
        Returns:
            JSON response as a dictionary
        """
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_user_repos(self, username: str) -> List[Dict]:
        """Get all public repositories for a user or organization.
        
        Args:
            username: GitHub username or organization name
            
        Returns:
            List of repository dictionaries
        """
        endpoint = f"/users/{username}/repos" if "@" not in username else f"/user/repos"
        return self._make_request(endpoint, params={"type": "public"})
    
    def get_repo_stats(self, owner: str, repo: str) -> Dict:
        """Get statistics for a specific repository.
        
        Args:
            owner: Repository owner username
            repo: Repository name
            
        Returns:
            Dictionary containing repository statistics
        """
        # Get basic repo info
        repo_info = self._make_request(f"/repos/{owner}/{repo}")
        
        # Get open issues count (issues include both issues and PRs in the count)
        issues = self._make_request(f"/repos/{owner}/{repo}/issues", {"state": "open"})
        open_issues = len([i for i in issues if 'pull_request' not in i])  # Exclude PRs
        
        # Get open PRs count
        prs = self._make_request(f"/repos/{owner}/{repo}/pulls", {"state": "open"})
        open_prs = len(prs)
        
        # Get top contributors (limited to 5)
        contributors = self._make_request(f"/repos/{owner}/{repo}/contributors", {"per_page": 5})
        
        return {
            "name": repo_info["name"],
            "full_name": repo_info["full_name"],
            "description": repo_info["description"] or "No description",
            "html_url": repo_info["html_url"],
            "stargazers_count": repo_info["stargazers_count"],
            "forks_count": repo_info["forks_count"],
            "open_issues_count": repo_info["open_issues_count"],
            "open_issues": open_issues,
            "open_prs": open_prs,
            "top_contributors": [{
                "login": c["login"],
                "contributions": c["contributions"]
            } for c in contributors] if isinstance(contributors, list) else []
        }
    
    def create_issue(self, owner: str, repo: str, title: str, body: str) -> Optional[Dict]:
        """Create a new issue in a repository.
        
        Args:
            owner: Repository owner username
            repo: Repository name
            title: Issue title
            body: Issue body
            
        Returns:
            Dictionary containing the created issue data, or None if failed
        """
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/issues"
        data = {"title": title, "body": body}
        
        try:
            response = requests.post(
                url,
                headers={"Authorization": f"token {self.headers['Authorization'].split(' ')[1]}"},
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to create issue: {e}")
            return None
