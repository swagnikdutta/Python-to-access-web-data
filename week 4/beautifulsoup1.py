import urllib.request
from bs4 import BeautifulSoup

outputFile = open('output.txt','w')

#url = input('Enter url- ') #raw_input was renamed to input
url = 'http://python-data.dr-chuck.net/comments_372164.html'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser') #soup is an object 

#outputFile.write(soup.prettify()+"\n") #if you wanna display the html

tags = soup('span')
ans = 0 

for tag in tags:
	#outputFile.write('TAG: \t'      + str(tag))
	#outputFile.write('URL: \t'      + str(tag.get('href', None)))
	#outputFile.write('Attrs: \t'    + str(tag.attrs))

	number = str(tag.contents[0])
	ans = ans + int(number)

outputFile.write(str(ans))
outputFile.close()
