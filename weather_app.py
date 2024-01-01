import tkinter as tk
from tkinter import ttk
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.api_key = "aa67a77495ddfb24fb0b96c7adc987f1"  # Replace with your API key
        self.weather_data = {}

        self.create_widgets()

    def create_widgets(self):
        # Location Entry
        location_label = ttk.Label(self.root, text="Enter Location:")
        location_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.location_entry = ttk.Entry(self.root)
        self.location_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Get Weather Button
        get_weather_button = ttk.Button(
            self.root, text="Get Weather", command=self.get_weather
        )
        get_weather_button.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        # Weather Information
        self.weather_label = ttk.Label(self.root, text="")
        self.weather_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def get_weather(self):
        location = self.location_entry.get()
        if not location:
            self.weather_label.config(text="Please enter a location.")
            return

        try:
            weather_data = self.fetch_weather_data(location)
            self.display_weather_info(weather_data)
        except Exception as e:
            self.weather_label.config(text=f"Error: {e}")

    def fetch_weather_data(self, location):
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": location,
            "appid": self.api_key,
            "units": "metric",  # You can change units to "imperial" for Fahrenheit
        }

        response = requests.get(base_url, params=params)
        response.raise_for_status()

        weather_data = response.json()
        return weather_data

    def display_weather_info(self, weather_data):
        city = weather_data["name"]
        description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        weather_info = (
            f"City: {city}\n"
            f"Description: {description}\n"
            f"Temperature: {temperature}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )

        self.weather_label.config(text=weather_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
