import tkinter as tk
from tkinter import messagebox
import requests

# Replace with your API Key
API_KEY = "1e810e48235ea54462550b434d458c8f"

def get_weather():
    city = city_entry.get().strip()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            messagebox.showerror("Error", "City not found!")
            return

        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"].title()
        wind = data["wind"]["speed"]

        result.config(
            text=f"""
City : {city.title()}

Temperature : {temperature} °C

Humidity : {humidity} %

Weather : {weather}

Wind Speed : {wind} m/s
"""
        )

    except Exception:
        messagebox.showerror("Error", "Unable to connect to the weather service.")

root = tk.Tk()
root.title("Weather App")
root.geometry("420x400")

title = tk.Label(root,
                 text="Weather App",
                 font=("Arial",18,"bold"))
title.pack(pady=15)

tk.Label(root,
         text="Enter City Name",
         font=("Arial",12)).pack()

city_entry = tk.Entry(root,
                      width=30,
                      font=("Arial",12))
city_entry.pack(pady=10)

tk.Button(root,
          text="Get Weather",
          command=get_weather,
          bg="green",
          fg="white",
          width=20).pack(pady=10)

result = tk.Label(root,
                  text="",
                  justify="left",
                  font=("Arial",12))
result.pack(pady=20)

root.mainloop()