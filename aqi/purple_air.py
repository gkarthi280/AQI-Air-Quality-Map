## Goutham Karthi, Student ID: 19652712
import json
import urllib.parse
import urllib.request
from pathlib import Path
URL = 'https://www.purpleair.com/data.json'



class purple_air_api():
    
    def __init__(self, url: str):
        self.url = url
    
    def get_data(self) -> dict or str:
        '''returns a dictionary version of the JSON returned by the PurpleAir API'''
        request = urllib.request.Request(self.url)
        response = urllib.request.urlopen(request)
        string:str = ''
        if response.status != 200:
            string += 'FAILED\n'
            string += str(response.status) + self.url +'\n'
            string += 'NOT 200'
            return string
        data = response.read().decode(encoding = 'utf-8')
        response.close()
        data_dict = json.loads(data)
        return data_dict


class purple_air_path():
    
    def __init__(self, path: Path):
        self.path = path

    def get_data(self):
        '''returns a dictionary version of the JSON contained in the PurpleAir Path'''
        string: str = ''
        data_dict = json.loads(self.path.read_text())
        return data_dict

    
