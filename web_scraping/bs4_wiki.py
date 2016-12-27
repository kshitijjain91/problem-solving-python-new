# dummy program to download html content from wiki and parsing using bs4

import requests, bs4
from bs4 import BeautifulSoup

res = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
try:
	res.raise_for_status()
except Exception as exc:
	print('There was an error in download {0)'.format(exc))

# create a BeautifulSoup object using the text attribute of the response object
wiki_python = BeautifulSoup(res.text, "html.parser")
# print(type(wiki_python))

# the select method of a bs4 object
divs = wiki_python.select('div')
print(type(divs))
print(len(divs))
print(str(divs[5]))
print(divs[5].attrs)

# pulling all the 'p' elements
p_elements = wiki_python.select('p')
print(len(p_elements))
print(p_elements[18])
print(str(p_elements[18]))
print(p_elements[18].getText())

