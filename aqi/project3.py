## Goutham Karthi, Student ID: 19652712
import json
import urllib.parse
import urllib.request
import nominatim
import calculations
import purple_air
import math
from pathlib import Path
import sys

def find_max(obj_list: list, max_nums: int) -> list:
        '''given a list of lists and the number of entries needed,
        returns the number of entries needed with the greatest AQI values'''
        purp_updated_data: list = []
        print(len(obj_list))
        if len(obj_list) <= max_nums:
                return obj_list
        for i in range(max_nums):
                index: int = 0
                max_aqi: int = 0
                for objs in obj_list:
                    if calculations.calculate_aqi(objs) > max_aqi:
                        max_aqi = calculations.calculate_aqi(objs)
                        index = obj_list.index(objs)
                purp_updated_data.append(obj_list[index])
                del obj_list[index]
        return purp_updated_data

def print_report(purp_data: list) -> None:
        '''prints report give the selected sensors from purple_air api'''
        if len(purp_data) == 0:
                print('No valid locations fit your constraints.')
                sys.exit()
        aqi: list = []
        coordinates: list = []
        location_descriptions: list = []
        
        i: int = 0
        for obj in purp_data:
                aqi.append(calculations.calculate_aqi(obj))
                coordinates.append((obj[27],obj[28]))
                reverse = nominatim.nominatim_api(nominatim.url_reverse_geo(coordinates[i][0],coordinates[i][1]))
                reverse_data = reverse.get_data()
                if type(reverse_data) == str:
                        print(reverse_data)
                        sys.exit()
                location_descriptions.append(reverse.full_description(reverse_data))
                i += 1
                
        for j in range(len(purp_data)):
                print(f'AQI {aqi[j]}')
                print(f'{nominatim.lat_and_lon(coordinates[j])}')
                print(f'{location_descriptions[j]}')
      
def run():
        while True:
                first_line: str = input('')
                if not first_line.startswith('CENTER NOMINATIM ') and not first_line.startswith('CENTER FILE '):
                        print('INVALID INPUT. TRY AGAIN.')
                        continue
                else:
                        break
        while True:
                second_line: str = input('')
                if not second_line.startswith('RANGE '):
                        print('INVALID INPUT. TRY AGAIN.')
                        continue
                else:
                        break       
        while True:
                third_line: str = input('')
                if not third_line.startswith('THRESHOLD '):
                        print('INVALID INPUT. TRY AGAIN.')
                        continue
                else:
                        break
        while True:
                fourth_line: str = input('')
                if not fourth_line.startswith('MAX '):
                        print('INVALID INPUT. TRY AGAIN.')
                        continue
                else:
                        break
        while True:
                fifth_line: str = input('')
                if fifth_line != 'AQI PURPLEAIR' and not fifth_line.startswith('AQI FILE '):
                        print('INVALID INPUT. TRY AGAIN.')
                        continue
                else:
                        break  

        while True:
                sixth_line: str = input('')
                if sixth_line != 'REVERSE NOMINATIM' and not sixth_line.startswith('REVERSE FILES '):
                        print('INVALID INPUT. TRY AGAIN.')
                        continue
                else:
                        break
                
        if first_line.startswith('CENTER NOMINATIM'):
                center = first_line[17:]
                forward = nominatim.nominatim_api(nominatim.url_forward_geo(center))
                
        else:
                center = first_line[first_line.index('FILE')+5:]
                p = Path(center)
                if p.exists():
                        forward = nominatim.nominatim_path(p)
                else:
                        print('FAILED\n' + center + '\n' + 'MISSING')
                        sys.exit()
                

        forward_data = forward.get_data()
        
        if type(forward_data) == str:
                print(forward_data)
                sys.exit()
        center_coordinate = forward.lat_lon(forward_data)        
        miles: int = int(second_line[second_line.index(' '):])
        threshold_aqi: int = int(third_line[third_line.index(' '):])
        max_num: int = int(fourth_line[fourth_line.index(' '):])

        if fifth_line == 'AQI PURPLEAIR':
                purp = purple_air.purple_air_api('https://www.purpleair.com/data.json')
         
        elif fifth_line[0:8] == 'AQI FILE':
                purple_file_path = Path(fifth_line[9:])
                if purple_file_path.exists():
                        purp = purple_air.purple_air_path(purple_file_path)
                else:
                        print('FAILED\n' + fifth_line[9:] + '\n' + 'MISSING')
                        sys.exit()
                
        purp_data = purp.get_data()
        if type(purp_data) == str:
                print(purp_data)
                sys.exit()
        purp_data = purp_data['data'][:]
        for obj in purp_data[:]:
                if not obj[4] < 3600 or not obj[25] == 0 or not calculations.calculate_aqi(obj) >= threshold_aqi or obj[27] == None or obj[28] == None:
                        purp_data.remove(obj)
        coordinate: tuple = ()
        for obj in purp_data[:]:
                coordinate = (obj[27],obj[28])
                if calculations.calculate_distance(center_coordinate, coordinate) > miles:               
                        purp_data.remove(obj)
        purp_updated_data = find_max(purp_data, max_num)
        for obj in purp_updated_data:
                print(f'{obj[27]} and {obj[28]} distance: {calculations.calculate_distance(center_coordinate, (obj[27],obj[28]))}')
        
        print(f'CENTER {nominatim.lat_and_lon(center_coordinate)}')
        if sixth_line == 'REVERSE NOMINATIM':
                print_report(purp_updated_data)

if __name__ == '__main__':
        run()
