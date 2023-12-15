from tkinter import *
from tkinter.ttk import *
import requests
import configparser

config = configparser.ConfigParser()

config.read("env.ini")

api_key = config.get("variables", "api_key")


def get_weather(city):
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
    # res = request.
    print(res.json())

# window = Tk()

# window.title("Testing elements")

# frame = Frame(window, width=200, height=200)

# greeting = Label(frame, text="Python rocks")
# button = Button(frame, text="Submit", command=get_weather)
# entry = Entry(frame, variable=city)

# button.pack()
# greeting.pack()
# entry.pack()

# window.mainloop()

# print("Done")

get_weather("london")
    
# print(api_key)