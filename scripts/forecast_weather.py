import requests
# import pyodbc
import pandas as pd

# Step 1: Make an HTTP request to the API endpoint
API_ENDPOINT = "https://www.meteosource.com/api/v1/free/point?place_id=dhaka&sections=all&timezone=UTC&language=en&units=metric&key=4on31zz6iiv63jz2n3j9sdtq24ebjx5e27xx97v8"
response = requests.get(API_ENDPOINT)
data = response.json()

# Parse the JSON response
weather_data = {
    'Latitude': [data['lat']],
    'Longitude': [data['lon']],
    'Elevation': [data['elevation']],
    'Timezone': [data['timezone']],
    'Current Data': [str(data['current'])],
    'Hourly Data': [str(data['hourly']['data'])],
    'Daily Data': [str(data['daily']['data'])]
}

# Step 2: Convert the data into a pandas DataFrame
df = pd.DataFrame(weather_data)

# Step 3: Save the DataFrame to an Excel file
excel_filename = 'weather_data.xlsx'
df.to_excel(excel_filename, index=False)

print(f"Data saved to {excel_filename}.")

# Parse the JSON response
# lat = data['lat']
# lon = data['lon']
# elevation = data['elevation']
# timezone = data['timezone']
# current_data = str(data['current'])
# hourly_data = str(data['hourly']['data'])
# daily_data = str(data['daily']['data'])

# Step 2: Connect to the SQL Server database
# server = '192.168.101.230,1433'
# database = 'AIDataset'
# username = 'sa'
# password = 'dataport'
# table = 'MSWeatherPrediction'

# Establish a connection
# conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
# cursor = conn.cursor()

# Step 3: Insert the fetched data into the database table
# insert_query = '''
# INSERT INTO {table} (lat, lon, elevation, timezone, current_data, hourly_data, daily_data)
# VALUES (?, ?, ?, ?, ?, ?, ?);
# '''.format(table=table)

# cursor.execute(insert_query, (lat, lon, elevation, timezone, current_data, hourly_data, daily_data))

# Commit the transaction and close the connection
# conn.commit()
# conn.close()

# print("Data saved to the database table MSWeatherPrediction.")