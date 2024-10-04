import requests

response = requests.get('http://api.open-notify.org/astros.json')
data = response.json()

print(f"There are {data['number']} astronauts in space right now.")

for astronaut in data['people']:
    print(f"{astronaut['name']} is on the {astronaut['craft']}.")