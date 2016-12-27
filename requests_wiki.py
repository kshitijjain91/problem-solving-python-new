# dummy program to download a wiki page using the requests module

import requests
res = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')

# always raise an exception after requests.get() to avoid crashing if the download fails
try:
	res.raise_for_status()
except Exception as exc:
	print("There was an error in downloading this page {0}".format(exc))

print(len(res.text))
print("Heydude"[:4])

# checking for errors in download
# If yes, it will print True
print(res.status_code == requests.codes.ok)

print(res.status_code)

print(res.text[:1900])
