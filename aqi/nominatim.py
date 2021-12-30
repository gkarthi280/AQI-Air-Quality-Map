## Goutham Karthi, Student ID: 19652712
import json
import urllib.parse
import urllib.request
from pathlib import Path
URL = 'https://www.purpleair.com/data.json'

def url_forward_geo(query: str) -> str:
        '''gernerates url for nominatim api forward geocoding'''
        url = 'https://nominatim.openstreetmap.org'
        query_parameters = [('q', query),('format','geojson')]
        return url + '/search?' + urllib.parse.urlencode(query_parameters)
    
def url_reverse_geo(latitude: float, longitude: float) -> str:
        '''gernerates url for nominatim api reverse geocoding given latitude and longitude'''
        url = 'https://nominatim.openstreetmap.org'
        query_parameters = [('format','jsonv2'),('lat',latitude),('lon',longitude)]
        return url + '/reverse?' + urllib.parse.urlencode(query_parameters)

def lat_and_lon(coordinates: tuple) -> str:
        '''given tuple of coordinates, returns latitude and longitude in string form'''
        lat: str = ''
        lon: str = ''
        if coordinates[0] < 0:
                lat = str(coordinates[0] * -1) + '/N'
        else:
                lat = str(coordinates[0]) + '/N'
        if coordinates[1] < 0:
                lon = str(coordinates[1] * -1) + '/W'
        else:
                lon = str(coordinates[1]) + '/W'
        return lat + ' ' + lon

class nominatim_api():
    
        def __init__(self, url: str):
                self.url = url
    
        def get_data(self) -> dict or str:
                '''returns a dictionary version of the JSON returned by the PurpleAir API'''
                request = urllib.request.Request(self.url, headers = { 'Referer' : 'https://www.ics.uci.edu/~thornton/ics32a/ProjectGuide/Project3/gkarthi' })
                response = urllib.request.urlopen(request)
                string: str = ''
                if response.status != 200:
                        string += 'FAILED\n'
                        string += str(response.status) + self.url +'\n'
                        string += 'NOT 200'
                        return string
            
                data = response.read().decode(encoding = 'utf-8')
                response.close()
                data_dict = json.loads(data)
                return data_dict
    
        def lat_lon(self, data_dict: dict) -> tuple:
                '''returns tuple containing latitude,longitude'''
                lat: float = data_dict['features'][0]['geometry']['coordinates'][1]
                lon: float = data_dict['features'][0]['geometry']['coordinates'][0]
                return (lat,lon)
    
        def full_description(self, data_dict: dict) -> str:
                '''returns string containing full deescription of address'''
                description: str = data_dict['display_name']
                return description
    

class nominatim_path():
    
        def __init__(self, path: Path):
                self.path = path

        def get_data(self) -> dict:
                '''returns a dictionary version of the JSON contained in the PurpleAir Path'''
                string: str = ''
                data_dict = json.loads(self.path.read_text())
                return data_dict

        def lat_lon(self, data_dict: dict) -> str:
                '''returns string containing latitude,longitude'''
                lat: float = data_dict['features'][0]['geometry']['coordinates'][1]
                lon: float = data_dict['features'][0]['geometry']['coordinates'][0]
                return (lat,lon)

        def full_description(self, data_dict: dict) -> str:
                '''returns string containing full deescription of address'''
                description: str = data_dict['display_name']
                return description



