# Weather App
My submission for the final bootcamp project.

## Description
This is a python program to spin up a Tkinter GUI where users can search for the weather condition of any city in the world. 

## Todo
- [ ] Make the user choose if they want the temperature shown in K (default) or °C.
- [ ] Add another tab and add some other functionality. Maybe a calculator?

## Getting Started
Clone this GitHub repository locally from the command line using:

```bash
git clone https://github.com/davidcharlie381/python-weather-app.git
```
After cloning, you should have the following file structure:

```plaintext
python-weather-app/
|-- main.py/
|-- .gitignore/
|-- README.md
|-- example.ini
```

Go to [Open Weather](https://openweathermap.org), create an account if you don't have one, and grab the API keys.

Replace the second line in the file `example.ini` with:

```
api_key = thenewapikey
```
Rename `example.ini` to `env.ini` from the command line using:

`mv example.ini env.ini`

Run:
`pip install requests`
To install the requests library used.

Finally, run:

`python3 main.py`

Voila! You can now find out if your partner in some other city is lying about where they currently are. 😅😉

Don't thank me; what are friends for? 🤗

Have fun! ✌🏽
