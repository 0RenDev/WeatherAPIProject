import requests, json
from nicegui import ui

ui.label('Hello NiceGUI!')
ui.button('BUTTON', on_click=lambda: ui.notify('button was pressed'))

ui.run()

api_key = "J79N6BMQG2YDZ7EUGA9QSNKH3"

base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

city = input("Enter city name (Limit to within the US): ")

# city = "Pleasanton"

complete_url = base_url + city + "?unitGroup=us&key="+ api_key + "&contentType=json"


response = requests.get(complete_url)

res_json = response.json()





print("The current weather in " + city + " is: " + str(res_json["currentConditions"]["temp"]) + "F")




def ret_currenttemp(response):
    return "The current weather in " + city + " is: " + str(res_json["currentConditions"]["temp"]) + "F"


ret_currenttemp(res_json)

