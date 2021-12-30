## Goutham Karthi, Student ID: 19652712
import math

def calculate_aqi(obj: list) -> int:
        '''given a list of list, ('data' element of purple air dictionary), returns aqi value'''
        pm_25: float = obj[1]
        if pm_25 == None:
            pm_25 = 0
        aqi: int = 0
        if pm_25 >= 500.5:
            aqi = 501
            return aqi
        elif pm_25 >= 350.5 and pm_25 < 500.5:
            aqi = (0.6604402935290195 * pm_25) + 169.51567711807866
            return round(aqi)
        elif pm_25 >= 250.5 and pm_25 < 350.5:
            aqi = (0.9909909909909912 * pm_25) + 52.756756756756715
            return round(aqi)
        elif pm_25 >= 150.5 and pm_25 < 250.5:
            aqi = (0.990990990990991 * pm_25) + 51.85585585585585
            return round(aqi)
        elif pm_25 >= 55.5 and pm_25 < 150.5:
            aqi = (0.5163329820864068 * pm_25) + 122.34351949420441
            return round(aqi)
        elif pm_25 >= 35.5 and pm_25 < 55.5:
            aqi = (2.462311557788945 * pm_25) + 13.587939698492448
            return round(aqi)
        elif pm_25 >= 12.1 and pm_25 < 35.5:
            aqi = (2.103004291845494 * pm_25) + 25.553648068669517
            return round(aqi)
        elif pm_25 >= 0 and pm_25 < 12.1: 
            aqi = 4.166666666666667 * pm_25
            return round(aqi) 
        else:
            return 0

def calculate_distance(coordinates_1: tuple, coordinates_2: tuple) -> float:
        '''given two strings, where each string is in the form
        "(float)/N (float)/W", and calcualtes equirectangular distance'''
        lat_1: float = coordinates_1[0]
        lat1 = (lat_1 * math.pi) / 180
        lon_1: float = coordinates_1[1]
        lon1 = (lon_1 * math.pi) / 180
        lat_2: float = coordinates_2[0]
        lat2 = (lat_2 * math.pi) / 180
        lon_2: float = coordinates_1[1]
        lon2 = (lon_2 * math.pi) / 180
        dlat: float = abs(lat2 - lat1)
        dlon: float = abs(lon2 - lon1)
        alat: float = (lat_1 + lat_2)/2
        radius: float = 3958.8
        x: float = dlon * math.cos(alat)
        return math.sqrt((x ** 2) + (dlat ** 2)) * radius

