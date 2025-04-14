import requests
import time
import pandas as pd
from datetime import datetime
import json

# Required imports
API_KEY = ''  # Updated to your working key from the error message
latitude = 27.680095
longitude = 84.428262
radius = 20000  # in meters (20km radius)

# Start with just a few place types to test
place_types = ['restaurant', 'cafe', 'hotel']

# Prepare data for Excel
data = []
# Track all found places by place_id to avoid duplicates
all_places = {}

print(f"Searching for places within {radius/1000}km of coordinates {latitude}, {longitude}...")

try:
    for place_type in place_types:
        print(f"Searching for {place_type}s...")
        
        # Google Places API endpoint
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius={radius}&type={place_type}&key={API_KEY}"
        print(f"Making request to API for {place_type}...")
        
        response = requests.get(url)
        print(f"Response status code: {response.status_code}")
        
        # Print API status instead of writing to file (avoids encoding issues)
        response_data = response.json()
        api_status = response_data.get('status')
        print(f"API status: {api_status}")
        
        if api_status != 'OK' and api_status != 'ZERO_RESULTS':
            print(f"API Error: {api_status}")
            print(f"Error message: {response_data.get('error_message', 'No specific error message')}")
            continue
        
        results = response_data.get('results', [])
        
        print(f"Found {len(results)} {place_type}(s)")
        
        if len(results) > 0:
            for place in results:
                place_id = place.get('place_id')
                
                # Skip if we've already processed this place
                if place_id in all_places:
                    continue
                    
                all_places[place_id] = True
                
                name = place.get('name')
                address = place.get('vicinity')
                rating = place.get('rating', 'N/A')
                user_ratings_total = place.get('user_ratings_total', 'N/A')
                
                print(f"Getting details for: {name}")
                # Get detailed info to extract website and phone number
                details_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,website,formatted_phone_number&key={API_KEY}"
                details_response = requests.get(details_url)
                
                details_result = details_response.json().get('result', {})
                
                website = details_result.get('website', 'No website found')
                phone = details_result.get('formatted_phone_number', 'No phone found')
                
                # Display info as we find it
                print(f"  Name: {name}")
                print(f"  Type: {place_type}")
                print(f"  Website: {website}")
                
                # Store the gathered data
                data.append({
                    'Name': name,
                    'Type': place_type,
                    'Address': address,
                    'Website': website,
                    'Phone': phone,
                    'Rating': rating,
                    'Reviews': user_ratings_total
                })
                
                # Add a short delay to avoid hitting API rate limits
                time.sleep(0.2)
            
            # Handle pagination to get more than 20 results
            next_page_token = response_data.get('next_page_token')
            
            while next_page_token:
                print(f"Getting next page of results for {place_type}...")
                # Wait before making the next page request (required by Google API)
                time.sleep(2)
                
                next_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={next_page_token}&key={API_KEY}"
                next_response = requests.get(next_url)
                
                next_data = next_response.json()
                next_results = next_data.get('results', [])
                print(f"Found {len(next_results)} more {place_type}(s)")
                
                for place in next_results:
                    place_id = place.get('place_id')
                    
                    # Skip if we've already processed this place
                    if place_id in all_places:
                        continue
                        
                    all_places[place_id] = True
                    
                    name = place.get('name')
                    address = place.get('vicinity')
                    rating = place.get('rating', 'N/A')
                    user_ratings_total = place.get('user_ratings_total', 'N/A')
                    
                    print(f"Getting details for: {name}")
                    # Get detailed info to extract website and phone number
                    details_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,website,formatted_phone_number&key={API_KEY}"
                    details_response = requests.get(details_url)
                    
                    details_result = details_response.json().get('result', {})
                    
                    website = details_result.get('website', 'No website found')
                    phone = details_result.get('formatted_phone_number', 'No phone found')
                    
                    # Display info as we find it
                    print(f"  Name: {name}")
                    print(f"  Type: {place_type}")
                    print(f"  Website: {website}")
                    
                    # Store the gathered data
                    data.append({
                        'Name': name,
                        'Type': place_type,
                        'Address': address,
                        'Website': website,
                        'Phone': phone,
                        'Rating': rating,
                        'Reviews': user_ratings_total
                    })
                    
                    # Add a short delay to avoid hitting API rate limits
                    time.sleep(0.2)
                
                # Update token for next page, if any
                next_page_token = next_data.get('next_page_token')
        
        # Add a slightly longer delay between different place type searches
        time.sleep(1.5)
    
    print(f"\nTotal unique places found: {len(all_places)}")
    
    if len(all_places) > 0:
        # Create DataFrame from collected data
        df = pd.DataFrame(data)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"nearby_places_{timestamp}.xlsx"
        
        # Export to Excel
        df.to_excel(filename, index=False)
        print(f"Data successfully exported to {filename}")
    else:
        print("No places found to export.")
        
except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
    import traceback
    traceback.print_exc()