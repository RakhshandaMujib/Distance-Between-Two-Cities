from geopy.geocoders import Nominatim #Module used for getting geographical data using Python.
from geopy import distance            #Check the link below for more details:
                                      #https://geopy.readthedocs.io/en/stable/#module-geopy.geocoders
def findingDist(city_1, city_2):
    '''
    This method will return the distance between the cities the user wants.
    Arguments:
    city_1 - String. Name of the origin-city.
    city_2 - String. Name of the destination city.
    Returns:
    A tuple- (distance,unit)
    '''
    geolocator = Nominatim(user_agent="distance_finder") #Giving "distance_finder" as the name of our Nominatim application.
    
    #Getting location details of the cities.
    city_1_loc = geolocator.geocode(city_1)
    city_2_loc = geolocator.geocode(city_2)

    #Filtering the coordinates (tuple: (latitude,longitude)) from the location details of the cities.
    coords_1 = (city_1_loc.latitude, city_1_loc.longitude)
    coords_2 = (city_2_loc.latitude, city_2_loc.longitude)
    
    unit = input("Do you want the distance in miles or km?")
    
    #Returning the distance between the coordinates depending on the unit choice of user.
    if unit.lower() == "miles":
        return (distance.distance(coords_1, coords_2).miles, 'miles')
    else:
        return (distance.distance(coords_1, coords_2).km, 'km')
    
def main():
    print("This program calculates the distance between two cities of your choice.")
    origin = input("\nEnter the name of origin:\n\t")
    destination = input("Enter the name of destination:\n\t")
    result = findingDist(origin,destination)
    print(f"The distance between {origin.title()} and {destination.title()} is:\n\t {round(result[0],2)} {result[1]}.")

if __name__ == '__main__':
    main()