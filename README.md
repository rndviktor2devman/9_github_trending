# 9_github_trending

Run script: type ' python github_trending.py '

For work script requires APP_ID, which can be obtained by the URL: https://github.com/settings/applications/new

Main purpose this script - to print out top trendy github's repositories

After providing APP_ID script will be able to retrieve list of top 'repositories_count' rated repositories,
which were created within last 'days_interval' days.

At retrieving data script prints out formatted repository's data.

Format exmple:

'number'. Repository:
Name:  'repository name'  Forks:  'count forks'  Stars:  'count stars'  Issues:  'count issues'
Description:  'repository description'
URL:  'repository url'