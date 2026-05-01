import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"

def report_weather(url):
    response = requests.get(url)
    data = response.json()
    hourly = data["hourly"]

    

    for i in range(len(hourly["time"])):      
        temp = hourly["temperature_2m"][i]
        if temp > 20:
            timestamp = hourly["time"][i]
            date, hour = timestamp.split("T")

            year, month, day = date.split("-")
            formatted_date = f"{day}/{month}/{year}"
            
            print(f"On {formatted_date}, at {hour}, Temperature: {temp}°C")

report_weather(url)