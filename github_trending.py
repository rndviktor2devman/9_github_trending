import requests
from datetime import datetime, timedelta
from itertools import islice


def get_trending_repositories(top_size):
    date_string = (datetime.now() - timedelta(top_size)).strftime("%Y-%m-%d")
    request_params = {"q": "created:>{}".format(date_string),
              "sort": "stars",
              "order": "desc"}
    trending_url = "https://api.github.com/search/repositories"
    data = requests.get(trending_url, params=request_params).json()
    return data["items"]


def print_repositories(repositories_list, output_length=20):
    index = 1
    for repository in islice(repositories_list, output_length):
        print("{}. Repository:".format(index))
        print "Name: ", repository["name"], \
            " Forks: ", repository["forks_count"], \
            " Stars: ", repository["stargazers_count"], \
            " Issues: ", repository["open_issues_count"]
        print "Description: ", repository["description"]
        print "URL: ", repository["html_url"]
        index += 1


def login_to_github():
    request_params = {"client_id": "8cb0e9b7166af6cef14c",
                      "scope": "user"}
    login_url = "https://github.com/login/oauth/authorize"
    requests.get(login_url, params=request_params)
    print('Successfully logged in.')


if __name__ == '__main__':
    login_to_github()
    print_repositories(get_trending_repositories(7))
