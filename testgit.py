from github import Github
import os
from pprint import pprint

token = os.getenv('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')
g = Github(token)
repo = g.get_repo("PranavHegde99")
issues = repo.get_issues(state="open")
pprint(issues.get_page(0))