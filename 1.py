# from __future__ import annotations 
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
        # raise NotImplementedError

    def distance(self, other_city: City) -> int:
        """
        Returns the distance in kilometers between two cities using the great circle method,
        rounded up to an integer.
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """
        Returns the name of the city and the country ISO3 code in parentheses.
        For example, "Melbourne (AUS)".
        """
        return self.name + f'({Country.iso3})'
        # raise NotImplementedError


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
        raise NotImplementedError

    def get_city(self, city_name: str) -> City:
        """
        Returns a city of the given name in this country.
        Returns None if there is no city by this name.
        If there are multiple cities of the same name, returns an arbitrary one.
        """
        
        city = City(city_name, self)
        # raise NotImplementedError

    def __str__(self) -> str:
        """
        Returns the name of the country.
        """
        return self.name
        # raise NotImplementedError



def create_example_countries_and_cities() -> None:
    """
    Creates a few Countries and Cities for testing purposes.
    """
    australia = Country("Australia", "AUS")
    # melbourne = City("Melbourne", "-37.8136", "144.9631", "Australia", "admin", "1036533631")
    # canberra = City("Canberra", "-35.2931", "149.1269", "Australia", "primary", "1036142029")
    # sydney = City("Sydney", "-33.865", "151.2094", "Australia", "admin", "1036074917")

    # japan = Country ("Japan", "JPN")
    # tokyo = City("Tokyo", "35.6839", "139.7744", "Japan", "primary", "1392685764")


def test_example_countries_and_cities() -> None:
    """
    Assuming the correct cities and countries have been created, runs a small test.
    """
    australia = Country.countries['Australia']
    # canberra =  australia.get_city("Canberra")
    # melbourne = australia.get_city("Melbourne")
    # sydney = australia.get_city("Sydney")
    print(australia)

    # print("The distance between {} and {} is {}km".format(melbourne, sydney, melbourne.distance(sydney)))

    # for city in australia.get_cities([CapitalType.admin, CapitalType.primary]):
    #     print("{} is a {} capital of {}".format(city, city.capital_type, city.country))


if __name__ == "__main__":
    create_example_countries_and_cities()
    test_example_countries_and_cities()



#     Task 1: City and Country
# Task
# Create a class City and a class Country by defining all the methods that currently raise NotImplementedError.

# Use the documentation of each method to determine how to implement them.

# Without modifying it, use the enum CapitalType in class City to define the capital types for each city as an instance variable.

# You may use the module geopy to approximate the distance between two instances of City using the great circle method.

# Classes City and Country both have a class variable, respectively cities and countries, that contains all instances of that class created so far. You need to ensure that these class variables are gradually populated in __init__. We give an example here.

# Input/output example
# Main code

# if __name__ == "__main__":
#     create_example_countries_and_cities()
#     test_example_countries_and_cities()
# Output

# The distance between Melbourne (AUS) and Sydney (AUS) is 714km
# Melbourne (AUS) is a admin capital of Australia
# Canberra (AUS) is a primary capital of Australia
# Sydney (AUS) is a admin capital of Australia
# We provide the function create_example_countries_and_cities() and a main to help you with your own tests. You can modify them.