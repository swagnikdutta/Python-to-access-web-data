import urllib.request
import json
from bs4 import BeautifulSoup

outputFile = open('output.txt','w')
url = 'http://python-data.dr-chuck.net/comments_372165.json'
data = urllib.request.urlopen(url).read()

soup = BeautifulSoup(data,'lxml')

# The source code as received from the url:
# outputFile.write(str(soup.prettify()))

# Deserializing the data to a python object js
js = json.loads(data)

# There are two keys in the js. "note" and "comments". 
# We are conserned only about "comments" which is an array of objects
js = js['comments']

sum = 0
for item in js:
	sum = sum + item['count']

outputFile.write(str(sum))

