import requests
import pytz
from datetime import datetime

# Define the API endpoint
API_ENDPOINT = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
# Define the menu options
MENU_OPTIONS = [
    "Get weather",
    "Get Wind Speed",
    "Get Pressure",
    "Exit",
]


def print_menu():
    for index in range(len(MENU_OPTIONS) - 1):
        print(str(index +1) + ".", MENU_OPTIONS[index])

    print("0.", MENU_OPTIONS[-1])


def print_result(data):
    london_tz = pytz.timezone('Europe/London')
    london_now = datetime.now(london_tz)
        
    for data_item in data["list"]:
        if date in data_item["dt_txt"] and str(london_now.hour) in data_item["dt_txt"]:

            if user_input == 1:
                print("The temperature of London for the date {} at {} is {} degrees Celsius.".format(date, str(london_now.hour) + ":00:00", data_item["main"]["temp"]))
            elif user_input == 2:
                print("The wind speed of London for the date {} at {} is {} meters per second.".format(date, str(london_now.hour) + ":00:00", data_item["wind"]["speed"]))
            elif user_input == 3:
                print("The pressure of London for the date {} at {} is {} hectopascals.".format(date, str(london_now.hour) + ":00:00", data_item["main"]["pressure"]))

            return
    #As this static API has data from 2019-03-27 18:00:00 to 2019-03-31 17:00:00
    print ("Data not found for the perticular date at the current time of London")



def make_api_request():
    response = requests.get(API_ENDPOINT, params={"q": "London,us", "appid": "b6907d289e10d714a6e88b30761fae22"})
    # Check the API response
    if response.status_code == 200:
        # Get the JSON data from the API response
        data = response.json()
        # Print the results
        print_result(data)


while True:
    # Print all menu items
    print_menu()
    # Get the user's input
    user_input = int(input("Please select an option from the menu: "))
    # If user enters 0 
    if user_input == 0:
        break
    # Check the user's input
    while user_input not in range(0, len(MENU_OPTIONS)):
        print("Invalid input. Please try again.")
        print_menu()
        user_input = int(input("Please select an option from the menu: "))
    # Get the date from the user
    if user_input == 1 or user_input == 2 or user_input == 3:
        date = input("Please enter the date (YYYY-MM-DD): ")

    # Make the API request
    make_api_request()