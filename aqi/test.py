import json
import urllib.parse
import urllib.request
from pathlib import Path
import sys

query1 = urllib.parse.urlencode([('q','Bren Hall, Irvine, CA'),('format','geojson')])
url1 = 'https://nominatim.openstreetmap.org/search?' + query1
request = urllib.request.Request(url1)
response = urllib.request.urlopen(request)
data = response.read()
print(response.status)
response.close()
text = data.decode(encoding = 'utf-8')
p = Path('search.txt')
f = p.open('w')
f.write(text)
f.close()
data_dict = json.loads(text)
print(type(data_dict))




##query3 = urllib.parse.urlencode([('format','jsonv2'),('lat',33.64324045),('lon',-117.84185686276017)])
##url3 = 'https://nominatim.openstreetmap.org/reverse?' + query3
##request = urllib.request.Request(url3)
##response = urllib.request.urlopen(request)
##print(type(response.status))
##response.close()
##data = response.read()
##text = data.decode(encoding = 'utf-8')
##p = Path('reverse.txt')
##f = p.open('w')
##f.write(text)
##f.close()





