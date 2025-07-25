from typing import Dict, List

def generate_markdown_report(username: str, repos_data: List[Dict]) -> str:
    """Generate a markdown report from the repository data.
    
    Args:
        username: GitHub username or organization name
        repos_data: List of repository data dictionaries
        
    Returns:
        Formatted markdown string
    """
    # Start building the markdown
    markdown = f"# GitHub Insights Report for {username}\n\n"
    
    # Add summary section
    total_repos = len(repos_data)
    total_stars = sum(repo.get('stargazers_count', 0) for repo in repos_data)
    total_forks = sum(repo.get('forks_count', 0) for repo in repos_data)
    total_issues = sum(repo.get('open_issues', 0) for repo in repos_data)
    total_prs = sum(repo.get('open_prs', 0) for repo in repos_data)
    
    markdown += "## Summary\n\n"
    markdown += f"- **Total Repositories**: {total_repos}\n"
    markdown += f"- **Total Stars**: {total_stars:,}\n"
    markdown += f"- **Total Forks**: {total_forks:,}\n"
    markdown += f"- **Total Open Issues**: {total_issues:,}\n"
    markdown += f"- **Total Open PRs**: {total_prs:,}\n\n"
    
    # Add details for each repository
    markdown += "## Repository Details\n\n"
    
    for repo in sorted(repos_data, key=lambda x: x.get('stargazers_count', 0), reverse=True):
        markdown += f"### [{repo['name']}]({repo['html_url']})\n"
        markdown += f"{repo['description']}\n\n"
        
        # Stats
        markdown += "**Stats:**  \n"
        markdown += f"⭐ **Stars:** {repo.get('stargazers_count', 0):,}  "
        markdown += f"🍴 **Forks:** {repo.get('forks_count', 0):,}  "
        markdown += f"📝 **Open Issues:** {repo.get('open_issues', 0):,}  "
        markdown += f"🔀 **Open PRs:** {repo.get('open_prs', 0):,}\n\n"
        
        # Top contributors
        if repo.get('top_contributors'):
            markdown += "**Top Contributors:**\n"
            for i, contributor in enumerate(repo['top_contributors'], 1):
                markdown += (
                    f"{i}. [{contributor['login']}](https://github.com/{contributor['login']}): "
                    f"{contributor['contributions']:,} commits\n"
                )
        else:
            markdown += "*No contributor data available*\n"
        
        # Check if we should create an issue (more than 20 open issues)
        if repo.get('open_issues', 0) > 20:
            markdown += "\n> ⚠️ **Note:** This repository has more than 20 open issues. "
            markdown += "Consider creating an issue to track them.\n"
        
        markdown += "\n---\n\n"
    
    return markdown

def save_report(report: str, filename: str = "github_insights_report.md") -> None:
    """Save the markdown report to a file.
    
    Args:
        report: Markdown formatted report string
        filename: Output filename (default: github_insights_report.md)
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"Report saved to {filename}")
