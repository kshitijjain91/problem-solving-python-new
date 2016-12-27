#! /usr/bin/env/python3

# I'm feeling lucky.py opens top Google search results using a set of keywords from the command line

import webbrowser, bs4, requests, sys
from bs4 import BeautifulSoup


# take input from sys.argv
print('Googling {0}'.format(' '.join(sys.argv[1:])))

# search on Google using requests
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))

try:
	res.raise_for_status()
except Exception as exc:
	print("There was an error getting results from Google: {0}".format(exc))

res = requests.get('http://google.com/search?q=' + ' '.join(["beautifulsoup"]))

# find out the top 5 results' URL using bs4
soup = BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.r a')
print(len(linkElems))

# open each URL in a new tab using webbrowser (min of 5 or the number of results found)
numOpen = min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href'))



