import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

# Function to sanitize filenames
def sanitize_filename(filename):
    return ''.join(c for c in filename if c.isalnum() or c in '._- ')

# Function to download images
def download_images(url, folder_path):
    # Sending a GET request to the URL
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for unsuccessful status codes
    except requests.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return
    except requests.RequestException as e:
        print(f"Request exception: {e}")
        return

    # Parsing the content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Finding all image tags in the webpage
    img_tags = soup.find_all('img')

    # Creating a folder to save images
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Downloading images
    for img in img_tags:
        if 'src' in img.attrs:
            img_url = img['src']
            img_name = os.path.basename(urllib.parse.urlparse(img_url).path)
            img_name = sanitize_filename(img_name)
            img_path = os.path.join(folder_path, img_name)

            if not img_url.startswith('http'):
                img_url = urllib.parse.urljoin(url, img_url)

            try:
                img_data = requests.get(img_url).content
                with open(img_path, 'wb') as handler:
                    handler.write(img_data)
                    print(f"Downloaded: {img_name}")
            except requests.RequestException as e:
                print(f"Error downloading {img_url}: {e}")
        else:
            print("Image source not found or accessible.")

# Example usage:
website_url = 'https://itti.com.np/'
folder_to_save = 'itti_images'  # Folder name to save images

download_images(website_url, folder_to_save)
