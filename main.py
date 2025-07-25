import sys
from typing import List, Dict, Any, Optional
from github_api import list_public_repos, get_repo_insights

def display_repo_list(repos: List[Dict[str, Any]]) -> None:
    """Display a numbered list of repositories."""
    print(f"\nFound {len(repos)} public repositories\n")
    print(f"{'#':<4} {'Repository':<40} {'Stars':<10} {'Forks':<10} URL")
    print("-" * 90)
    
    for i, repo in enumerate(repos, 1):
        print(f"{i:<4} {repo['name']:<40} {repo['stars']:<10} {repo['forks']:<10} {repo['url']}")

def display_repo_insights(owner: str, repo_name: str) -> None:
    """Fetch and display insights for a specific repository."""
    try:
        print(f"\n📊 Fetching insights for {owner}/{repo_name}...")
        insights = get_repo_insights(owner, repo_name)
        
        # Display insights
        print("\n" + "=" * 60)
        print(f"📊 Repository: {owner}/{repo_name}")
        print("=" * 60)
        
        # Issues and PRs
        issues_count = insights['open_issues_count']
        prs_count = insights['open_prs_count']
        
        issues_display = f"🔢 Open Issues: {issues_count}"
        if insights['has_many_issues']:
            issues_display += " ⚠️  (More than 20 open issues!)"
            
        print(issues_display)
        print(f"🔁 Open Pull Requests: {prs_count}")
        
        # Top contributors
        print("\n👥 Top Contributors:")
        if not insights['top_contributors']:
            print("  No contributor data available")
        else:
            for i, contributor in enumerate(insights['top_contributors'], 1):
                print(f"  {i}. {contributor['login']} - {contributor['contributions']:,} commits")
        
        print("=" * 60 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error fetching repository insights: {str(e)}")

def main():
    print("GitHub Repository Insights")
    print("=" * 25)
    
    current_repos = []
    current_username = ""
    
    while True:
        # If we don't have a list of repos yet, ask for username
        if not current_repos:
            username = input("\nEnter GitHub username or organization (or 'q' to quit): ").strip()
            
            if username.lower() == 'q':
                print("Goodbye!")
                sys.exit(0)
                
            if not username:
                print("Please enter a valid username or organization name.")
                continue
                
            try:
                print(f"\nFetching repositories for {username}...")
                current_repos = list_public_repos(username)
                current_username = username
                
                if not current_repos:
                    print("No public repositories found or user/organization does not exist.")
                    continue
                    
                # Sort repositories by number of stars (descending)
                current_repos = sorted(current_repos, key=lambda x: x['stars'], reverse=True)
                
            except Exception as e:
                print(f"\nAn error occurred: {str(e)}")
                print("Please check the username/organization name and your internet connection.")
                continue
        
        # Display the list of repositories
        display_repo_list(current_repos)
        
        # Prompt for repository selection
        print("\nEnter a repository number to view insights")
        print("'b' to go back, 'q' to quit, or 'r' to refresh")
        choice = input("\nYour choice: ").strip().lower()
        
        if choice == 'q':
            print("Goodbye!")
            break
            
        if choice == 'b':
            current_repos = []  # Reset to go back to username input
            continue
            
        if choice == 'r':
            current_repos = []  # This will trigger a refresh
            continue
            
        # Try to parse the choice as a number
        try:
            repo_index = int(choice) - 1
            if 0 <= repo_index < len(current_repos):
                repo = current_repos[repo_index]
                display_repo_insights(current_username, repo['name'])
                input("\nPress Enter to continue...")
            else:
                print(f"Please enter a number between 1 and {len(current_repos)}")
        except ValueError:
            print("Invalid input. Please enter a number, 'b', 'q', or 'r'.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user. Goodbye!")
        sys.exit(0)
