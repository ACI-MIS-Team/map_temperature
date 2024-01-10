import requests
import pandas as pd

# API endpoint
url = "https://www.meteosource.com/api/v1/flexi/find_places"

# Sample points data without coordinates
points = [
    {"title": "Bagerhat"},
    {"title": "Bandarban"},
    {"title": "Barguna"},
    {"title": "Barishal"},
    {"title": "Bhola"},
    {"title": "Bogra"},
    {"title": "Brahmanbaria"},
    {"title": "Chandpur"},
    {"title": "Chapainawabganj"},
    {"title": "Chattogram"},
    {"title": "Chuadanga"},
    {"title": "Comilla"},
    {"title": "Cox's Bazar"},
    {"title": "Dhaka"},
    {"title": "Dinajpur"},
    {"title": "Faridpur"},
    {"title": "Feni"},
    {"title": "Gaibandha"},
    {"title": "Gazipur"},
    {"title": "Gopalganj"},
    {"title": "Habiganj"},
    {"title": "Jamalpur"},
    {"title": "Jashore"},
    {"title": "Jhalokathi"},
    {"title": "Jhenaidah"},
    {"title": "Joypurhat"},
    {"title": "Khagrachari"},
    {"title": "Khulna"},
    {"title": "Kishoreganj"},
    {"title": "Kurigram"},
    {"title": "Kushtia"},
    {"title": "Lakshmipur"},
    {"title": "Lalmonirhat"},
    {"title": "Madaripur"},
    {"title": "Magura"},
    {"title": "Manikganj"},
    {"title": "Meherpur"},
    {"title": "Moulvibazar"},
    {"title": "Munshiganj"},
    {"title": "Mymensingh"},
    {"title": "Naogaon"},
    {"title": "Narail"},
    {"title": "Narayanganj"},
    {"title": "Narsingdi"},
    {"title": "Natore"},
    {"title": "Nawabganj"},
    {"title": "Netrokona"},
    {"title": "Nilphamari"},
    {"title": "Noakhali"},
    {"title": "Pabna"},
    {"title": "Panchagarh"},
    {"title": "Patuakhali"},
    {"title": "Pirojpur"},
    {"title": "Rajbari"},
    {"title": "Rajshahi"},
    {"title": "Rangamati"},
    {"title": "Rangpur"},
    {"title": "Satkhira"},
    {"title": "Shariatpur"},
    {"title": "Sherpur"},
    {"title": "Sirajganj"},
    {"title": "Sunamganj"},
    {"title": "Sylhet"},
    {"title": "Tangail"},
    {"title": "Thakurgaon"},
]

# List to store place data
all_place_data = []

# Loop through each point
for point in points:
    # Extract title
    title = point["title"]

    # Parameters for the API request
    params = {
        "text": title,
        "language": "en",
        "key": "4on31zz6iiv63jz2n3j9sdtq24ebjx5e27xx97v8",
    }

    # Make the API request
    response = requests.get(url, params=params)
    data = response.json()

    # Check if any data is returned
    if data:
        # Extract place data and add to the list
        lat_str = data[0]["lat"].rstrip('N')
        lon_str = data[0]["lon"].rstrip('E') if 'E' in data[0]["lon"] else "-" + data[0]["lon"].rstrip('W')
        
        place_data = {
            "title": title,
            "place_id": data[0]["place_id"],
            "lat": float(lat_str),
            "lon": float(lon_str),
        }
        all_place_data.append(place_data)

# Create a DataFrame from the collected data
df = pd.DataFrame(all_place_data, columns=["title", "place_id", "lat", "lon"])

# Save the DataFrame to an Excel file
excel_file_path = 'points_place_data.xlsx'
df.to_excel(excel_file_path, index=False, engine='openpyxl')

print(f"Data saved to {excel_file_path}")
