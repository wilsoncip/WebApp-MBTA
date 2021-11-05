# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "XgyimnTEKwa2P4NwDWHkYS59HAVxRxgT"
MBTA_API_KEY = "5be92a41c75b401283f44e93b3b46d75"


# A little bit of scaffolding if you want to use it
import json
from pprint import pprint

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    import urllib.request
    import json

    request = urllib.request.urlopen(url)
    response_text = request.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data



def get_lat_long(location):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    APIKEY = MAPQUEST_API_KEY
    data = get_json(f'http://www.mapquestapi.com/geocoding/v1/address?key={APIKEY}&location={location}')
    coordinates = data['results'][0]['locations'][0]['displayLatLng']
    return (coordinates['lat'], coordinates['lng'])


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    import urllib.request
    import json
    lat = 42.3394
    lon = -71.0940
    url = f'https://api-v3.mbta.com/stops?filter%5Blatitude%5D={lat}&filter%5Blongitude%5D={lon}&api_key={MBTA_API_KEY}&sort=distance'
    print(url)
    request = urllib.request.urlopen(url)
    response_text = request.read().decode('utf-8')
    response_data = json.loads(response_text)
    station_name = response_data['data'][0]['attributes']['description']
    wheelchair_accessible = response_data['data'][0]['attributes']['wheelchair_boarding']
    return f"You are closest to {station_name}. Wheelchair status: {wheelchair_accessible}"


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    current_location = get_lat_long(place_name)
    # nearest = get_nearest_station(current_location[0], current_location[1])
    # return nearest




def main():
    """
    You can test all the functions here
    """
    pprint(get_nearest_station(42,-71))


if __name__ == '__main__':
    main()
