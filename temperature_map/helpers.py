import matplotlib.pyplot as plt
import mpld3
import json
from datetime import datetime


def plot_weather_data(json_data):
    # Parse the JSON data
    data = json.loads(json_data)

    # Extracting dates, temperatures, and humidity values
    dates = [datetime.strptime(d["date"], "%Y-%m-%d").day for d in data]
    temperatures = [d["temperature"] for d in data]
    humidity = [d["humidity"] for d in data]

    # Creating the plot
    fig, ax1 = plt.subplots()

    # Plotting temperature data
    color = "tab:red"
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Temperature (°C)", color=color)
    ax1.plot(dates, temperatures, color=color)
    ax1.tick_params(axis="y", labelcolor=color)

    # Instantiate a second axes that shares the same x-axis
    ax2 = ax1.twinx()
    color = "tab:blue"
    ax2.set_ylabel("Humidity (%)", color=color)
    ax2.plot(dates, humidity, color=color)
    ax2.tick_params(axis="y", labelcolor=color)

    # Automatically adjust the subplot params for the plot to fit into the figure area.
    fig.tight_layout()

    # Convert the matplotlib figure to HTML and return it
    return mpld3.fig_to_html(fig)
