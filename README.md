# GitHub Insights

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

A command-line tool to fetch and analyze GitHub repository statistics for any user or organization.

## ✨ Features

- 🔍 List all public repositories for any GitHub user or organization
- 📊 View detailed repository insights:
  - 🔢 Number of open issues (with warning for >20 issues)
  - 🔄 Number of open pull requests
  - 👥 Top 3 contributors by commit count
  - ⭐ Number of stars and forks
- 🖥️ Clean, interactive command-line interface
- 🚦 Colorful output with emojis for better readability
- 🔄 Easy navigation between repositories
- ⚡ Fast and efficient API usage

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/06navdeep06/GitHub-Insights.git
   cd GitHub-Insights
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your GitHub token**:
   - Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
   - Click "Generate new token (classic)"
   - Give it a descriptive name
   - Select the `public_repo` scope
   - Copy the generated token

4. **Configure the application**:
   - Create a `.env` file in the project root:
     ```bash
     echo "GITHUB_TOKEN=your_token_here" > .env
     ```
   - Replace `your_token_here` with the token you copied

## 🎯 Usage

### Basic Usage

1. **Run the script**:
   ```bash
   python main.py
   ```

2. **Enter a GitHub username or organization name** when prompted

3. **Browse repositories**:
   - Enter a number to view detailed insights for that repository
   - Press Enter to go back to the repository list
   - Type 'b' to go back to username input
   - Type 'r' to refresh the repository list
   - Type 'q' to quit

### Example Session

```
GitHub Repository Insights
=========================

Enter GitHub username or organization (or 'q' to quit): octocat

Fetching repositories for octocat...

Found 8 public repositories

#    Repository                             Stars      Forks      URL
------------------------------------------------------------------------------------------
1    Hello-World                           1234       5678       https://github.com/octocat/Hello-World
2    git-consortium                        901        234        https://github.com/octocat/git-consortium
...

Enter a repository number to view insights
'b' to go back, 'q' to quit, or 'r' to refresh

Your choice: 1

📊 Fetching insights for octocat/Hello-World...

============================================================
📊 Repository: octocat/Hello-World
============================================================
🔢 Open Issues: 42 ⚠️  (More than 20 open issues!)
🔁 Open Pull Requests: 5

👥 Top Contributors:
  1. octocat - 1,234 commits
  2. otheruser - 56 commits
  3. contributor - 12 commits
============================================================

Press Enter to continue...
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- GitHub API for providing the data
- Python community for awesome tools and libraries

This will generate a markdown report named `github_insights_report.md` in the current directory.

### Options

```
usage: gh-insights [-h] [--token TOKEN] [--output OUTPUT] [--create-issue] [--version] username

GitHub Insights - Fetch and analyze GitHub repository statistics

positional arguments:
  username          GitHub username or organization name

options:
  -h, --help        show this help message and exit
  --token TOKEN     GitHub Personal Access Token (default: reads from GITHUB_TOKEN env var)
  -o, --output OUTPUT
                    Output filename (default: github_insights_report.md)
  --create-issue    Create an issue if a repo has more than 20 open issues
  --version         Show version and exit
```

### Examples

1. Generate a report for a user:
   ```bash
   gh-insights octocat
   ```

2. Save the report to a specific file:
   ```bash
   gh-insights octocat -o octocat_report.md
   ```

3. Create issues for repositories with many open issues:
   ```bash
   gh-insights octocat --create-issue
   ```

4. Use a specific GitHub token:
   ```bash
   gh-insights octocat --token your_github_token_here
   ```

## Development

1. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

2. Run tests:
   ```bash
   pytest
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
