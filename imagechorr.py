import requests
from bs4 import BeautifulSoup
import os

# Function to download images
def download_images(url, folder_path):
    # Sending a GET request to the URL
    response = requests.get(url)

    # Parsing the content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Finding all image tags in the webpage
    img_tags = soup.find_all('img')

    # Creating a folder to save images
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Downloading images
    for img in img_tags:
        img_url = img['src']
        img_name = img_url.split('/')[-1]
        img_path = os.path.join(folder_path, img_name)
        
        # Check if the image URL is relative
        if not img_url.startswith('http'):
            img_url = url + img_url

        # Download the image and save it
        img_data = requests.get(img_url).content
        with open(img_path, 'wb') as handler:
            handler.write(img_data)
            print(f"Downloaded: {img_name}")

# Example usage:
website_url = 'https://bigbyte.com.np/'
folder_to_save = 'bigbyte_images'  # Folder name to save images

download_images(website_url, folder_to_save)
