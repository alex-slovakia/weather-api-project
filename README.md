# Weather Report Script

This Python script fetches hourly temperature data from the Open-Meteo API and prints every time the temperature is higher than 20°C for the selected location. In the current code, the location is set to Berlin using latitude `52.52` and longitude `13.41`. [file:1]

## Features

- Requests hourly weather data from the Open-Meteo API. [file:1]
- Reads hourly temperature values from the JSON response. [file:1]
- Filters only temperatures above 20°C. [file:1]
- Formats the date from `YYYY-MM-DD` to `DD/MM/YYYY`. [file:1]
- Prints the matching date, hour, and temperature. [file:1]

## Requirements

- Python 3.x
- `requests` library [file:1]

Install the dependency with:

```bash
pip install requests
```

## Usage

Run the script with:

```bash
python main.py
```

The script will:
1. Send a request to the Open-Meteo API. [file:1]
2. Read the hourly forecast data. [file:1]
3. Print only the timestamps where the temperature is above 20°C. [file:1]

## Example Output

```text
On 03/05/2026, at 14:00, Temperature: 21.4°C
On 03/05/2026, at 15:00, Temperature: 22.1°C
```

## Notes

The script currently uses a hardcoded API URL for Berlin and requests only `temperature_2m` in the hourly forecast. [file:1]  
The code in `main.py` appears to have indentation issues, so it may need formatting fixes before it runs correctly. [file:1]

## API Source

Weather data is fetched from [Open-Meteo](https://open-meteo.com/). [file:1]
