import tkinter as tk
import requests
import configparser

config = configparser.ConfigParser()

config.read("env.ini")

api_key = config.get("variables", "api_key")

# function to fetch weather 

def get_weather(city):
    """"
    Fetch the weather of param {city}
    """

    # it could go wrong
    
    try:
        res = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)) 

        # response status might not be OK
        
        if res.status_code == 200:
            json_res = res.json()
            desc = json_res["weather"][0]["description"] 
            temp = json_res["main"]["temp"]
            return [desc, temp]
        else:
             raise NameError("Couldn't fetch that data.")
    except Exception as e:
        return str(e)

# function to run when user clicks the button

def make_request():
    """
    When the user clicks the button
    """

    # Get text from the entry widget
    
    entry_text = entry.get()
    
    # The result from the get_weather function passing in the entry_text as argument
    
    result = get_weather(entry_text)

    # Our function is expected to return a list of two things if all goes well.

    if isinstance(result, list):
        desc = result[0]
        temp = result[1]
        
        description.config(text="Desc: {}".format(desc))
        temperature.config(text="Temp: {}".format(temp))
        
    # Else an error has been thrown
    
    else:
        description.config(text="Error: {}".format(result))
        temperature.config(text="")

# Create a root window

root = tk.Tk()
root.title("Weather App")

# Label to instruct user

instruction = tk.Label(root, text="Type in a city to get started:")
instruction.pack(pady=20)

# Entry to get user input

entry = tk.Entry(root)
entry.pack(pady=10)

# Button to trigger the action
update_button = tk.Button(root, text="Check weather", command=make_request)
update_button.pack()

# Label widgets for description and temperature

description = tk.Label(root, text="Desc: ")
temperature = tk.Label(root, text="Temp: ")

temperature.pack(pady=10)
description.pack(pady=10)

# Copyright because I wrote python, bro!!! 🥺

built_by = tk.Label(root, text="Built by Charlie ©2023 ")
built_by.pack(pady=50)

# Start the Tkinter event loop
root.mainloop()
