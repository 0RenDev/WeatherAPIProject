import requests, json


api_key = "J79N6BMQG2YDZ7EUGA9QSNKH3"

base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

# city = input("Enter city name (Limit to within the US): ")

city = "Pleasanton"

complete_url = base_url + city + "?unitGroup=us&key="+ api_key + "&contentType=json"


response = requests.get(complete_url)

res_json = response.json()


json_obj = json.dumps(res_json, indent=4)

print(res_json["currentConditions"]["temp"])


with open("temp.json", "w") as outfile:
    outfile.write(json_obj)