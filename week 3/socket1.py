import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating the end points
mysock.connect(('www.py4inf.com',80))

mysock.send(b'GET http://data.pr4e.org/intro-short.txt HTTP/1.0 \n\n')

outputFile = open("output.txt", "w")

while True:
	data = mysock.recv(512)
	if( len(data) < 1 ):
		break
	outputFile.write(data.decode("utf-8")+"\n") #string cannot be appended to byte so decode.
	
mysock.close()
outputFile.close()