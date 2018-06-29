import JSON_parser

class Directions:
    '''stores all directions in a class and returns it'''
    def __init__(self, result):
        self = JSON_parser.directions(result)
    def generate(self):
        return self

class Distance:
    '''stores total distance in a class and returns it'''
    def __init__(self, result):
        self = JSON_parser.distance(result)
    def generate(self):
        return self

class Time:
    '''stores total time in minutes in a class and returns it'''
    def __init__(self, result):
        self = JSON_parser.time(result)
    def generate(self):
        return self

class Lat_Long:
    '''stores latitude and longitude of the locations and returns them'''
    def __init__(self, result):
        self = JSON_parser.lat_long(result)
    def generate(self):
        return self
                     
