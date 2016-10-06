import requests
from datetime import datetime, timedelta
import json
from itertools import islice

APP_ID = ""
days_interval = 7
repositories_count = 20
login_url = ("https://github.com/login/oauth/authorize?"
             "client_id={}&scope=user%20public_repo")
top_created_url = ("https://api.github.com/search/repositories?"
                   "q=created:>{}&sort=stars&order=desc")
issues_url = "https://api.github.com/repos/{}/{}/issues"


def get_trending_repositories(top_size):
    week_ago = datetime.now() - timedelta(days_interval)
    string_date = week_ago.strftime("%Y-%m-%d")
    r = requests.get(top_created_url.format(string_date))
    data = json.loads(r.text)
    i = 1
    for repository in islice(data["items"], top_size):
        print_repository(i, repository)
        i += 1


def print_repository(number, repository):
    print("{}. Repository:".format(number))
    print "Name: ", repository["name"], \
        " Forks: ", repository["forks_count"], \
        " Stars: ", repository["stargazers_count"], \
        " Issues: ", \
        get_open_issues_amount(repository["owner"]["login"],
                               repository["name"])
    print "Description: ", repository["description"]
    print "URL: ", repository["html_url"]


def get_open_issues_amount(repo_owner, repo_name):
    r = requests.get(issues_url.format(repo_owner, repo_name))
    data = json.loads(r.text)
    return len(data)


def login_to_github():
    requests.get(login_url.format(APP_ID))
    print('Successfully logged in.')


if __name__ == '__main__':
    login_to_github()
    get_trending_repositories(repositories_count)
