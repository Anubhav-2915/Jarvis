import requests

api_key =  "f3d8867d4a2b4b3b861195658262202"

url = "http://api.weatherapi.com/v1/current.json"   

params = {
    "key" : api_key,
    "q" : "New Delhi"
}

def weather():
    response = requests.get(url, params=params)
    data =  response.json()

    city = data["location"]["name"]
    temp = data["current"]["temp_c"]
    date_time = data["current"]["last_updated"]
    print(f"Location: {city}\n Temp(C): {temp}\n Last Updated: {date_time}")

if __name__ == "__main__":
    weather()