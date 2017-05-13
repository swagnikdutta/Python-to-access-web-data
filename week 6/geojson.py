
import urllib.request
from bs4 import BeautifulSoup
import json

outputFile = open('output.txt','w')

address = input('Enter location')
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

serviceurl = serviceurl + urllib.parse.urlencode({
						'sensor': 'false',
						'address': address
						})

source_code = urllib.request.urlopen(serviceurl).read()
js = json.loads(source_code)
place_id = js['results'][0]['place_id']
outputFile.write(str(place_id))


