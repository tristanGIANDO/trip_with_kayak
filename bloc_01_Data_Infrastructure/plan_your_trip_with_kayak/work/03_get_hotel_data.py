import os
import pandas as pd

"""
Gets the JSON file generated by Booking's scraping and creates a CSV file
"""

filename = "hotels.json"
csv_filename = "hotel_data.csv"

root = os.path.dirname(os.path.dirname(__file__))
input_path = os.path.join(root, "booking_scraper", filename)
output_path = os.path.join(root, "work", "csv_files", csv_filename)

with open(input_path, "r", encoding="utf-8") as file:
    hotel_content = file.read()

df = pd.DataFrame(eval(hotel_content))
df.to_csv(output_path, index=False, encoding="utf-8")