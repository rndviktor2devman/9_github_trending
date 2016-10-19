import requests
from datetime import datetime, timedelta


def get_trending_repositories(top_size):
    date_string = (datetime.now() - timedelta(top_size)).strftime("%Y-%m-%d")
    request_params = {"q": "created:>{}".format(date_string),
                      "sort": "stars",
                      "order": "desc"}
    trending_url = "https://api.github.com/search/repositories"
    data = requests.get(trending_url, params=request_params).json()
    return data["items"]


def print_repositories(data, output_length=20):
    for index, repository in enumerate(data[:output_length]):
        print("{}. Repository:".format(index + 1))
        print("Name: ", repository["name"],
              " Forks: ", repository["forks_count"],
              " Stars: ", repository["stargazers_count"],
              " Issues: ", repository["open_issues_count"])
        print("Description: ", repository["description"])
        print("URL: ", repository["html_url"])


if __name__ == '__main__':
    days_range = 7
    print_repositories(get_trending_repositories(days_range))
