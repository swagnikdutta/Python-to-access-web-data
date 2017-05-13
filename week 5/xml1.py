import urllib.request
import xml.etree.ElementTree as ET 
from bs4 import BeautifulSoup

outputFile = open('output.txt','w')

url = 'http://python-data.dr-chuck.net/comments_372161.xml'

source_code = urllib.request.urlopen(url).read()
soup = BeautifulSoup(source_code,'lxml')

sum = 0

for item in soup.findAll('count'):
	outputFile.write(str(item.contents[0])+"\n")
	sum = sum + int(item.contents[0])

print(sum)
