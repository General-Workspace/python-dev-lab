import requests

# Get the weather data from OpenWeatherMap's API
city = 'Abuja'
open_weather_api_url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=77e2f812e0da1660eb246b665fc1b08c'
weather_api_url = 'https://api.weatherapi.com/v1/current.json?key=cf95eca18b2f4280a03162827240410&q='+city+'&aqi=no'
response = requests.get(open_weather_api_url)
data = response.json()

print(data)

output = ''
# Print the weather data
for key, value in data.items():
    if key == 'location':
        output += f"The current temperature in {value['name']} is {data['current']['temp_c']}°C - ({data['current']['condition']['text']})"
    elif key == 'current':
        output += f"\nThe weather condition is {value['condition']['text']} with a humidity of {value['humidity']}%."
        output += f"\nIt feels like {value['feelslike_c']}°C with a wind speed of {value['wind_kph']} km/h."
        output += f"\nVisibility is {value['vis_km']} km and the UV index is {value['uv']}."
        output += f"\nLast updated: {value['last_updated']}"
    # print(f"The current temperature in {data['location']['name']} is {data['current']['temp_c']}°C.")
print(output)

# Sample weather response
'''
{
    "location": {
        "name": "Abuja",
        "region": "Federal Capital Territory",
        "country": "Nigeria",
        "lat": 9.1758,
        "lon": 7.1808,
        "tz_id": "Africa/Lagos",
        "localtime_epoch": 1728059832,
        "localtime": "2024-10-04 17:37"
    },
    "current": {
        "last_updated_epoch": 1728059400,
        "last_updated": "2024-10-04 17:30",
        "temp_c": 23.5,
        "temp_f": 74.3,
        "is_day": 1,
        "condition": {
            "text": "Patchy rain nearby",
            "icon": "//cdn.weatherapi.com/weather/64x64/day/176.png",
            "code": 1063
        },
        "wind_mph": 4.7,
        "wind_kph": 7.6,
        "wind_degree": 102,
        "wind_dir": "ESE",
        "pressure_mb": 1010.0,
        "pressure_in": 29.83,
        "precip_mm": 0.14,
        "precip_in": 0.01,
        "humidity": 92,
        "cloud": 84,
        "feelslike_c": 25.8,
        "feelslike_f": 78.5,
        "windchill_c": 23.5,
        "windchill_f": 74.3,
        "heatindex_c": 25.8,
        "heatindex_f": 78.5,
        "dewpoint_c": 22.2,
        "dewpoint_f": 71.9,
        "vis_km": 10.0,
        "vis_miles": 6.0,
        "uv": 5.0,
        "gust_mph": 7.0,
        "gust_kph": 11.3
    }
}
'''