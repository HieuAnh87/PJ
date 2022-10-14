from __future__ import annotations

import math
from enum import Enum


class CapitalType(Enum):
    """
    The different types of capitals (e.g. "primary").
    """
    primary = "primary"
    admin = "admin"
    minor = "minor"
    unspecified = ""

    def __str__(self) -> str:
        return self.value

class City():
    """
    Represents a city.
    """

    cities = dict() # a dict that associates city IDs to instances.

    def __init__(self, name: str, latitude: str, longitude: str, country: str, capital_type: str, city_id: str) -> None:
        """
        Initialises a city with the given data.
        """
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.country = country
        self.capital_type = capital_type
        self.city_id = city_id
        
        City.cities[self.name] = self.capital_type
        
        # raise NotImplementedError
    
    
    # City.cities[self.city_id] = City(self.name, self.latitude, self.longitude, self.country, self.capital_type, self.city_id)

    def distance(self, other_city: City) -> int:
        """
        Returns the distance in kilometers between two cities using the great circle method,
        rounded up to an integer.
        """
    
        R = 6378.137
    
        # Our formula requires we convert all degrees to radians
        lat1 = math.radians(float(self.latitude))
        lat2 = math.radians(float(other_city.latitude))
        lon1 = math.radians(float(self.longitude))
        lon2 = math.radians(float(other_city.longitude))
    
        lat_span = lat1 - lat2
        lon_span = lon1 - lon2
    
        a = math.sin(lat_span / 2) ** 2
        b = math.cos(lat1)
        c = math.cos(lat2)
        d = math.sin(lon_span / 2) ** 2
    
        dist = 2 * R * math.asin(math.sqrt(a + b * c * d))
        return int(dist)

    def __str__(self) -> str:
        """
        Returns the name of the city and the country ISO3 code in parentheses.
        For example, "Melbourne (AUS)".
        """
        # ios3 = Country.countries[self.country]
        
        ios3 = Country.countries.get(self.country)
        return self.name + f' ({ios3})'
        
 
class Country():
    """
    Represents a country.
    """

    countries = dict()  # a dict that associates country names to instances.

    def __init__(self, name: str, iso3: str) -> None:
        """
        Creates an instance with a country name and a country ISO code with 3 characters.
        """
        self.name = name
        self.iso3 = iso3
        
        
        Country.countries[self.name] = self.iso3
        # raise NotImplementedError

    # def _add_city(self, city: City):
    #     """
    #     Adds a city to the country.
    #     """
        
        	
        
        # raise NotImplementedError

    def get_cities(self, capital_types: list[CapitalType] = None) -> list[City]:
        """
        Returns a list of cities of this country.

        The argument capital_types can be given to specify a subset of the capital types that must be returned.
        Cities that do not correspond to these capital types are not returned.
        If no argument is given, all cities are returned.
        """
        res = []
        # city = City(name=City.cities.g, capital_type=City.cities[self.name])
        
        for cap_type in capital_types:
            for name, capital_type  in City.cities.items():
                if capital_type == str(cap_type):
                    res.append(name.lower())
        print(res)
        return res
    
        
        
        
        

    # def get_city(self, city_name: str) -> City:
    #     """
    #     Returns a city of the given name in this country.
    #     Returns None if there is no city by this name.
    #     If there are multiple cities of the same name, returns an arbitrary one.
    #     """
        
    #     city = City(city_name, self)
    #     # raise NotImplementedError

    def __str__(self) -> str:
        """
        Returns the name of the country.
        """
        return self.name
        # raise NotImplementedError

australia = Country("Australia","AUS")
# print(australia)
melbourne = City("Melbourne", "-37.8136", "144.9631", "Australia", "admin", "1036533631")
sydney = City("Sydney", "-33.865", "151.2094", "Australia", "admin", "1036074917")
# print(City.cities)
# print("The distance between {} and {} is {}km".format(melbourne, sydney, melbourne.distance(sydney)))
australia.get_cities([CapitalType.admin, CapitalType.primary])

# for city in australia.get_cities([CapitalType.admin, CapitalType.primary]):
#         print(city.lower())
#         print(city.)
        # print("{} is a {} capital of {}".format(city, city.capital_type, city.country))
