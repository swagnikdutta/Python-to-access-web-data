import urllib.request
from bs4 import BeautifulSoup

outputFile = open('output.txt','w')

url = 'http://python-data.dr-chuck.net/known_by_Vanessa.html'

pos = 18
turn = 7
links = list()

for i in range(turn):
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser') 
	tags = soup('a')
	
	tag_at_pos = tags[pos-1]
	url = tag_at_pos.get('href',None)

	outputFile.write(str(tag_at_pos) +"\n"+ url) 	#for debugging
	outputFile.write("\n\n") 						#for debugging

outputFile.write(tag_at_pos.contents[0])			#gives the answer

outputFile.close()
