#!/usr/bin/python3

"""
Script that retrieves 10 most recent \
        commits from a repository using the GitHub API.
"""

import requests
import sys

if __name__ == "__main__":
    # Repository name
    repo_name = sys.argv[1]
    # Owner name
    owner_name = sys.argv[2]

    # URL to fetch
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    # Send GET request to GitHub API
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        commits = response.json()[:10]  # Retrieve the first 10 commits

        # Print the commit sha and author name
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: Failed to retrieve commits. \
                Status code: {response.status_code}")
