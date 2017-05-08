import urllib.request

fhand = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
#fhand = open('index.html' , 'r') 

outputFile = open('output.txt','w') #need write permission 

for line in fhand:
	string = line.decode("utf-8")
	outputFile.write(string)

	#outputFile.write(line)	#if you're reading a text file. Strings need not be decoded.

outputFile.close()