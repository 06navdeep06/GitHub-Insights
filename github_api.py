import os
import requests
from typing import Dict, List, Tuple, Optional
from dotenv import load_dotenv

def get_github_headers():
    """Load GitHub token from .env and return headers for API requests."""
    load_dotenv()
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        raise ValueError("GitHub token not found in .env file")
    return {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

def list_public_repos(user_or_org):
    """Fetch all public repositories for a given GitHub user or organization.
    
    Args:
        user_or_org (str): GitHub username or organization name
        
    Returns:
        list: List of repository dictionaries with name, stars, and forks
    """
    url = f'https://api.github.com/users/{user_or_org}/repos'
    if '/' in user_or_org:  # If it's a full URL path
        url = f'https://api.github.com/{user_or_org}/repos'
    
    headers = get_github_headers()
    repos = []
    page = 1
    
    while True:
        params = {
            'per_page': 100,
            'page': page,
            'type': 'public'
        }
        
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        if not data:  # No more repositories
            break
            
        for repo in data:
            repos.append({
                'name': repo['name'],
                'stars': repo['stargazers_count'],
                'forks': repo['forks_count'],
                'url': repo['html_url']
            })
        
        # Check if there are more pages
        if 'next' not in response.links:
            break
            
        page += 1
    
    return repos

def get_repo_insights(owner: str, repo_name: str) -> Dict[str, any]:
    """Fetch insights for a specific repository.
    
    Args:
        owner: Repository owner (username or org name)
        repo_name: Repository name
        
    Returns:
        Dictionary containing repository insights:
        - open_issues_count: Number of open issues (excluding PRs)
        - open_prs_count: Number of open pull requests
        - top_contributors: List of top 3 contributors with their commit counts
        - has_many_issues: Boolean indicating if there are more than 20 open issues
    """
    headers = get_github_headers()
    base_url = f'https://api.github.com/repos/{owner}/{repo_name}'
    
    # Get open issues (excluding PRs)
    issues_url = f'{base_url}/issues'
    params = {'state': 'open', 'per_page': 1, 'page': 1}
    
    try:
        # Get open issues count (excluding PRs)
        issues = []
        page = 1
        while True:
            params['page'] = page
            response = requests.get(issues_url, headers=headers, params=params)
            response.raise_for_status()
            
            page_issues = response.json()
            if not page_issues:
                break
                
            # Filter out pull requests (they're included in issues endpoint)
            issues.extend([i for i in page_issues if 'pull_request' not in i])
            
            # Stop if we've checked enough pages to know there are > 20 issues
            if len(issues) > 20 or 'next' not in response.links:
                break
                
            page += 1
        
        # Get open PRs count
        prs_url = f'{base_url}/pulls'
        prs_response = requests.get(prs_url, headers=headers, params={'state': 'open', 'per_page': 1})
        prs_response.raise_for_status()
        
        # Get top contributors
        contributors_url = f'{base_url}/contributors'
        contributors_response = requests.get(
            contributors_url, 
            headers=headers, 
            params={'per_page': 3, 'sort': 'contributions', 'direction': 'desc'}
        )
        contributors_response.raise_for_status()
        
        # Process contributors
        top_contributors = [
            {'login': c['login'], 'contributions': c['contributions']} 
            for c in contributors_response.json()
        ][:3]  # Ensure we only take top 3
        
        return {
            'open_issues_count': len(issues),
            'open_prs_count': len(prs_response.json()),
            'top_contributors': top_contributors,
            'has_many_issues': len(issues) > 20
        }
        
    except requests.exceptions.RequestException as e:
        error_msg = str(e)
        if e.response is not None:
            if e.response.status_code == 404:
                error_msg = f"Repository '{owner}/{repo_name}' not found"
            elif e.response.status_code == 403:
                error_msg = "API rate limit exceeded. Please try again later."
            else:
                error_msg = f"GitHub API error: {e.response.status_code} - {e.response.text}"
        raise Exception(f"Failed to fetch repository insights: {error_msg}")
