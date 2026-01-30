# GitHub Insights



A command-line tool to fetch and analyze GitHub repository statistics for any user or organization.


##  Installation

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

##  Usage

### Basic Usage

```bash
python main.py
```

1. **Enter a GitHub username or organization name** when prompted
2. **Browse repositories**:
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

 Fetching insights for octocat/Hello-World...

===========================================================
 Repository: octocat/Hello-World
===========================================================
 Open Issues: 42 ⚠️ (More than 20 open issues!)
 Open Pull Requests: 5

👥 Top Contributors:
  1. octocat - 1,234 commits
  2. otheruser - 56 commits
  3. contributor - 12 commits
============================================================

Press Enter to continue...
```

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

 Fetching insights for octocat/Hello-World...

============================================================
 Repository: octocat/Hello-World
============================================================
 Open Issues: 42 ⚠️  (More than 20 open issues!)
 Open Pull Requests: 5

👥 Top Contributors:
  1. octocat - 1,234 commits
  2. otheruser - 56 commits
  3. contributor - 12 commits
============================================================

Press Enter to continue...
```


## 🙏 Acknowledgments

- GitHub API for providing the data
- Python community for awesome tools and libraries

## Development

1. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

2. Run tests:
   ```bash
   pytest
   ```
