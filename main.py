import tkinter as tk
import requests
import configparser

config = configparser.ConfigParser()

config.read("env.ini")

api_key = config.get("variables", "api_key")

def get_weather(city):
    try:
        res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}") 
        if res.status_code == 200:
            json_res = res.json()
            desc = json_res["weather"][0]["description"] 
            temp = json_res["main"]["temp"]
            return [desc, temp]
        else:
             raise NameError("Couldn't fetch that data.")
    except Exception as e:
        return str(e)

def make_request():
    # Get text from the entry widget
    entry_text = entry.get()
    
    # Update the label with the entry's text
    
    
    result = get_weather(entry_text)
    
    if isinstance(result, list):
        desc = result[0]
        temp = result[1]
        
        description.config(text=f"Desc: {desc}")
        temperature.config(text=f"Temp: {temp}")
        
    else:
        description.config(text=f"Error: {result}")
        temperature.config(text="")

root = tk.Tk()
root.title("Weather App")

# Entry widget for user input

instruction = tk.Label(root, text="Type in a city to get started:")
instruction.pack(pady=20)

entry = tk.Entry(root)
entry.pack(pady=10)

# Button to trigger the action
update_button = tk.Button(root, text="Check weather", command=make_request)
update_button.pack()

description = tk.Label(root, text="Desc: ")
temperature = tk.Label(root, text="Temp: ")

temperature.pack(pady=10)
description.pack(pady=10)

built_by = tk.Label(root, text="Built by Charlie ©2023 ")
built_by.pack(pady=50)

# Start the Tkinter event loop
root.mainloop()
