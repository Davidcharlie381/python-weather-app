from tkinter import *
from tkinter.ttk import *
import requests
import configparser

config = configparser.ConfigParser()

config.read("env.ini")

api_key = config.get("variables", "api_key")

city = ""

def get_weather(city):
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
    # res = request.

    json_res = res.json()

    city = json_res["weather"][0]["description"]

root = Tk()

root.title("Weather app")

# frame = Frame(root, width=200, height=200)


# 

entry = Entry()
button = Button(text="Submit", command=get_weather(entry.get()))

greeting = Label(text=city)


button.pack()
# greeting.pack()
entry.pack()

root.mainloop()

