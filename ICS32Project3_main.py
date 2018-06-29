 # ICS 32, Lab 5 (Code: 36614) Edward Chen ID:88277651
 # Assignment #
import JSON_parser
import Implement_output
#needs to read input make it have the functions for it.

def get_input() -> list:
    '''
    recieves input for locations to be used to
    construct url
    '''
    number_locations = input("")
    list_locations = []
    for locations in range(eval(number_locations)):
        location = input("")
        list_locations.append(location)
    return list_locations

def indicate_results() -> list:
    '''
    recieves input for what results the user
    wants such as steps, distance,  etc.
    '''
    number_output = input("")
    list_output = []
    for outputs in range(eval(number_output)):
        output_wanted = input("")
        list_output.append(output_wanted)
    return list_output

def return_results (list: 'list of what user wants', dict: 'json_result'):
    '''
    recieves json_result and list of what user wants
    to determine what to print
    '''
    for results_wanted in list:
        if(results_wanted == 'STEPS'):
            Implement_output.Directions(result).generate()
        elif(results_wanted == 'TOTALDISTANCE'):
            Implement_output.Distance(result).generate()
        elif(results_wanted == 'TOTALTIME'):
            Implement_output.Time(result).generate()
        elif(results_wanted == 'LATLONG'):
            Implement_output.Lat_Long(result).generate()
            
    
if __name__ == '__main__':

    locations = get_input()
    
    results_wanted = indicate_results()
    result = JSON_parser.get_result(JSON_parser.build_search_url(locations))
    print('\n')
    return_results(results_wanted, result)
    print('\n')
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')

    
