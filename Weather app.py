'''
This program lets the user know the temperature, humidity, and a descripton of the sky. It asks the user what city they want to get the info about
then it gets the weather data from a external webstise and prints it 
'''

import requests

api_key = '7e7dc02656b21b911f54d74ffeb1d7c0'  # Replace with your actual API key

city = input("Enter the city name: ")

# Construct the URL with units set to imperial for Fahrenheit
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}'

# Make the request
response = requests.get(url)

# Check for errors
if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    print(f'Temperature: {temp}°F')
    print(f'Humidity: {humidity}%')
    print(f'Description: {description.capitalize()}')
else:
    # Print out the error from the API for troubleshooting
    print('Error:', response.json().get("message", "Please try again later"))




