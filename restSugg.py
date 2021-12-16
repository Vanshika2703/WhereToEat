#Business Search      URL -- 'https://api.yelp.com/v3/businesses/search'
#Business Match       URL -- 'https://api.yelp.com/v3/businesses/matches'
#Phone Search         URL -- 'https://api.yelp.com/v3/businesses/search/phone'

#Business Details     URL -- 'https://api.yelp.com/v3/businesses/{id}'
#Business Reviews     URL -- 'https://api.yelp.com/v3/businesses/{id}/reviews'

#Businesses, Total, Region

# Import the modules
import requests
import json
import PySimpleGUI as sg
from random import randint

# Define a business ID
business_id = '6HW31CueDTgaqd6Q5MNXLg'
unix_time = 1546047836

# Define my API Key, My Endpoint, and My Header
API_KEY = 'CChxA4UmzeOEqS6UNr5rUDGggs8alwg189striIRcS9H_mjt5MlzcxKAcpaaaHYlzqTRnqCK8dUc3ndWCMBYGExKAK-41YOqr4mUh_BAgP_5ZcTsr_oIYu12q_63YXYx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'.format(business_id)
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

#sg.preview_all_look_and_feel_themes()
sg.theme('Black')
preferences=[   [sg.Text("Need Help Choosing? Fill out some basic information")], 
            [sg.Text("What Zip code are you looking to go eat near?*")],
            [sg.InputText()],
            [sg.Text("What are you craving?")],
            [sg.Text("(optional)")],
            [sg.InputText()],  
            [sg.Button("Next")]
        ]

window = sg.Window(title="Where To Eat", layout = preferences ,size=(500,350))
event, values = window.read()

while True:
    if event == "Next":
        zipcode = values[0]
        if len(values) > 1:
            cuisine = values[1]
        print("Zip: ", zipcode)
        if cuisine:
            print("Cuisine: ", cuisine)
            PARAMETERS = {'location':{'zip_code': zipcode},
                'term': cuisine,
                'open_now': True
                }
        else:
            PARAMETERS = {'location':{'zip_code': zipcode},
                'term': 'food',
                'open_now': True
                }
        
        print(PARAMETERS)
        # Make a request to the Yelp API
        response = requests.get(url = ENDPOINT,
                                params = PARAMETERS,
                                headers = HEADERS)

        # Conver the JSON String
        business_data = response.json()

        # print the response
        # print(json.dumps(business_data, indent = 3))
        window.close()
        num = randint(0,19)
        displayResult=[[sg.Text(business_data["businesses"][num]["name"], size=(60,1), justification='center')],
        [sg.Text("Location: "),sg.Text(business_data["businesses"][num]["location"]["display_address"][0], justification='center')],
        [sg.Text("Rating: "),sg.Text(business_data["businesses"][num]["rating"], justification='center')],
        [sg.Button("Great Thanks!")],[sg.Button("Meh Show me something else")]]
        displayWindow = sg.Window(title="Where To Eat", layout = displayResult ,size=(500,350))

        event, values = displayWindow.read()
        break

print(event,values)

