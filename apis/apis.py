# %%
import requests

latitude  = 16.80
longitude = 81.36

url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m'

response = requests.get(url)
data = response.json()

temprature = data["current"]["temperature_2m"]

#print(data)
print(f'current temprature is - {temprature}')
# %%
