import os
import csv
from bs4 import BeautifulSoup
import json


def extract_metadata(file_path):
    # Initialize variables
    title = 'N/A'
    publication_time = 'N/A'
    last_editorial_update = 'N/A'
    page_categories = 'N/A'

    # Recurse through HTML files
    with (open(file_path, 'r', encoding='utf-8') as file):
        soup = BeautifulSoup(file, 'html.parser')
        title = soup.title.string if soup.title else 'N/A'
        divList = soup.find_all("div", class_="v-instance")
        for div in divList:
            jsonData = json.loads(div.attrs["data-v"])
            if 'mc' in jsonData:
                mcData = jsonData.get('mc', {})
                pluginData = mcData.get('pluginData', {})
                trackingData = pluginData.get('trackingPiano@all', {})
                avData = trackingData.get('avContent', {})
                print (avData)
                publication_time = avData.get('d:content_publication_time', 'N/A')
                last_editorial_update = avData.get('d:content_last_editorial_update', 'N/A')
                page_categories = avData.get('page_categories', 'N/A')
            else:
                continue
       
        return title, publication_time, last_editorial_update, page_categories


def recurse_directories(root_dir, output_csv):
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['File Path', 'Title', 'Publication Time', 'Last Editorial Update', 'Categories'])

        for subdir, _, files in os.walk(root_dir):
            for file in files:
                if file.endswith('.html'):
                    file_path = os.path.join(subdir, file)
                    title, publication_time, last_editorial_update, page_categories = extract_metadata(file_path)
                    csvwriter.writerow([file_path, title, publication_time, last_editorial_update, page_categories])


# Run the script
root_directory = '/path/to/your/HTML/files'
output_csv_file = 'output_metadata.csv'
recurse_directories(root_directory, output_csv_file)
