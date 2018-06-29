 # ICS 32, Lab 5 (Code: 36614) Edward Chen ID:88277651
 # Assignment #3
import json
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = 'Fmjtd%7Cluu821u2l9%2C2s%3Do5-94as90'
BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2/route?key='

def build_search_url(input1):
    '''
    This function builds the search URL given the locations that user inputs
    '''
    #makes sure that any following inputted locations are recorded as to in url
    to = input1[1:]
    #used as a placeholder to insert '&to='
    to = 'NULL'.join(to)
    query_parameters = [
                        ('from', input1[0]), ('to', to)              
    ]
    #constructs url from base, api key, &, and encodes locations before replacing to
    #make sure '&' is not encoded into different characters
    URL = BASE_MAPQUEST_URL + MAPQUEST_API_KEY + '&' + urllib.parse.urlencode(query_parameters).replace('NULL','&to=')
    return(URL)
def get_result(url: str) -> 'json':
    '''
    This function takes a URL and returns a Python object representing the
    parsed JSON response.
    '''
    response = None

    try:
        #opens url and then reads and decodes the message to be use in json.loads()
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        #convers json_text into a Python object
        return json.loads(json_text)

    finally:
        #makes sure to close response no matter if function fails or not
        if response != None:
            response.close()
'''
Functions used to parse JSON response
to be used in the classes
'''

def directions(json_result):
    '''
    formats directions
    '''
    print('DIRECTIONS')
    for item in json_result['route']['legs']:
        b = item.get('maneuvers')
        for i in b:
            print((i.get('narrative')))
    print('\n')
    
def distance(json_result):
    '''
    calculates and formats distance
    '''
    total_distance = 0
    for item in json_result['route']['legs']:
        b = item.get('maneuvers')
        for i in b:
            total_distance += i.get('distance')
    total_distance = round(total_distance)
    print('Total Distance: ' + str(total_distance) + ' miles\n' )\
                 
def time(json_result):
    '''
    calculates and formats time
    '''
    z = 0
    for item in json_result['route']['legs']:
        b = item.get('maneuvers')
        for i in b:
            z += i.get('time')
    p = round(z/60)
    #return p
    print('Total Time: ' + str(p) + ' minutes\n')
    
def lat_long(json_result):
    '''
    calculates and formats longitude and latitude
    '''
    z = []
    t = []
    count = 0
    for g in json_result['route']['locations']:
        d = g.get('latLng')
        z.append(d.get('lat'))
        z.append(d.get('lng'))
    for variable in z:
        if count % 2 == 0:
            
            if (variable < 0):
                t.append(str(abs(round(variable,2))) + 'S')
            else:
                t.append(str(round(variable,2)) + 'N')
        else:
            if (round(variable,2) < 0):
                t.append(str(abs(round(variable,2))) + 'W')
            else:
                t.append(str(round(variable,2)) + 'E')
        count += 1
    #return t
    time_print = round(len(t)/2)
    for i in range(time_print):
        print(t[2*i] + ' ' + t[2*i+1])
        #just returning t
    print('\n')
                     

    
        
    
    


