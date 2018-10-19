from bs4 import BeautifulSoup
import requests
import pandas as pd
from github import Github

# Pandas print options
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# url
website = 'https://gist.github.com/paulmillr/2657075'

def get_element_in_table(soup):
    title = soup.find('table', cellspacing="0")
    row = title.findChild('tbody').findChild('tr')
    result = []
    result.append(row.findChild('td').findChild('a').text)
    for i in range(20):
        row = row.findNext('tr')
        result.append(row.findChild('td').findChild('a').text)
    return result


def get_results():
    results = []
    res = requests.get(website)
    if res.status_code == 200:
        html_doc = res.text
        soup = BeautifulSoup(html_doc, "html.parser")
        results = get_element_in_table(soup)
    return results

# First create a Github instance:
# using an access token
g = Github("8c1cd46a0e763ef735d05c21f1752651f05d4460")

users = get_results()
mean_star = []

# Then play with your Github objects:
for user in users:
    git_user = g.get_user(user)
    count_star = 0
    for repo in git_user.get_repos():
        count_star += repo.stargazers_count
    if(git_user.public_repos != 0):
        mean_star.append(count_star/git_user.public_repos)
    else:
        mean_star.append(0)

df = pd.DataFrame()
df['Username'] = users
df['Stars per repository'] = mean_star

print(df.sort_values('Stars per repository', ascending=False))