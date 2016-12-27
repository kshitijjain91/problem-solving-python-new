# dummy program to download html text from freshdesk using requests 
# also, creating a bs4 object using the text attribute of the bs4 object

import bs4, requests
from bs4 import BeautifulSoup

# download content using requests.get() and raise an exception
res = requests.get('https://upgradsupport.freshdesk.com/helpdesk/dashboard?view=standard')

try:
	res.raise_for_status()
except Exception as exc:
	print('There was some problem downloading this page {0}'.format(exc))

print(res.text[:])

# creating a bs4 object using text attribute of res 
freshdesk = BeautifulSoup(res.text, "html.parser")
# print(type(freshdesk))

pElems = freshdesk.select('p')
print(len(pElems))

divElems = freshdesk.select('div')
print(len(divElems))
div_texts = [x.getText().lower() for x in divElems]

div_summary = freshdesk.select('.alt-login-button')
print(len(div_summary))
print(div_summary[0].getText())



