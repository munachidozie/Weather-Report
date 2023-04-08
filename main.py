import requests

api_key = "4d8e3dc4ef19ea67d1f1838ed7a59b1a"
web_url = "http://api.weatherstack.com/current"

while True:
  city = input(""" ⛈️⚡🌦️  WEATHER REPORT ☔☀️❄️

  Input your city:  """)

  parameters = {'access_key': api_key, 'query': city}
  response = requests.get(web_url, parameters)

  if response.status_code != 200:
        print("Error retrieving weather data.")
        continue
    
  js = response.json()
  temperature = js["current"]["temperature"]
  date = js["location"]["localtime"]
  city = js["location"]["name"]
  country = js["location"]["country"]
  description = js["current"]["weather_descriptions"][0]

  print(f"The temperature in {city}, {country} on {date} is {temperature} degrees Celsius and/with {description}")

  answer = input("Would you like to check the weather for another city? (Y/N) ")
  if answer == "y" or answer == "Y":
    print()
    print()
    print()
    continue
  else:
    break