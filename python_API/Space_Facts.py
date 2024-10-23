import os
from io import BytesIO

import requests
from PIL import Image
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

# API key and the base URL
API_KEY = os.getenv('NASA_API_KEY')
url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

# GET request to the NASA API
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    title = data.get('title')
    explanation = data.get('explanation')
    image_url = data.get('url')
    
    print(f"Title: {title}")
    print(f"Explanation: {explanation}")
    print(f"Image URL: {image_url}")
    
    # Check if the image_url is valid
    if image_url is not None and image_url.endswith(('.jpg', '.png', '.jpeg')):
        # Fetch and display the image
        image_response = requests.get(image_url)
        img = Image.open(BytesIO(image_response.content))
        img.show()
    else:
        print("No valid image URL available. The content might be a video or other media.")
    
else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")