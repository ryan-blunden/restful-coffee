import requests

from django.conf import settings


class GoogleDistanceMatrix:
    mode = 'driving'
    units = 'imperial'
    origins = None
    destinations = None

    def __init__(self, origins, destinations):
        self.origins = origins
        self.destinations = destinations

    def compute(self):
        url = 'https://maps.googleapis.com/maps/api/distancematrix/json?mode={mode}&units={units}&origins={origins}&destinations={destinations}&key={key}'.format(
            mode=self.mode,
            units=self.units,
            origins=self.origins,
            destinations=self.destinations,
            key=settings.GOOGLE_MAPS_API_KEY
        )

        response = requests.get(url).json()

        return {
            'origin_addresses': response['origin_addresses'][0],
            'destination_addresses': response['destination_addresses'][0],
            'distance': response['rows'][0]['elements'][0]['distance']['text'],
            'time': response['rows'][0]['elements'][0]['duration']['text']
        }
