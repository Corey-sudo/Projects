import requests
import json
import time
from pprint import pprint

def UrlScan():
    API_KEY = $Your_API_Key

    IP_To_Search = input("What IP address would you like to search? ")
    headers = {'API-Key': API_KEY, 'Content-Type': 'application/json'}
    data = {"url": IP_To_Search, "visibility": "public"}

    # Make the API request using the requests library
    response = requests.post('https://urlscan.io/api/v1/scan/', headers=headers, data=json.dumps(data))

    # Check if the request was successful (status code 200)
    
    if response.status_code == 200:
        # Print the raw response content
        print("Raw Response:")
        print(response.text)

        # Parse the JSON response
        json_response = response.json()

        # Extract and print specific information from the response
        result = json_response.get("api")
        # Allow time for the website to update the content
        print("Parsing Json content, please wait 60 seconds...")
        time.sleep(60)
        
        if result:
            print("\nExtracted Result:")
            pprint(result)

            # Assuming result is a URL, you can make another request to get information
            info_response = requests.get(result)
            if info_response.status_code == 200:
                pprint(info_response.json())
            else:
                print(f"Error getting information: {info_response.status_code} - {info_response.text}")
        else:
            print("No result found in the response.")

    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code} - {response.text}")
    while True:
  
        Save = input("Would you like to save this file? [Y] or [N]")
        if Save == "N":
            break
        if Save == "Y":
            File_Name = input("Creat a .txt file and enter the name here")
            with open(File_Name, "a") as f:
                print(result.json(), file=f)
                
                break
    else:
        print("Try Again")

def CrowdSec():
  IP_To_Search = input("What IP address would you like to search?")
  headers = {'x-api-key': $YOUR_API_Key,}
  response = requests.get('https://cti.api.crowdsec.net/v2/smoke/' + IP_To_Search, headers=headers)
  #dump = json.dump(response)
  #File_Text = pprint(response.json())
  pprint(response.json())
  
  while True:
  
    Save = input("Would you like to save this file? [Y] or [N]  ")
    if Save == "N":
        break
    if Save == "Y":
        File_Name = input("Creat a .txt file and enter the name here  ")
        with open(File_Name, "a") as f:
            print(response.json(), file=f)
    else:
        print("Try Again")
        

while True:
    try:
        choice = int(input("Would you like to use [1] UrlScan or [2] CrowdSec? Type [3] to exit  "))
    except ValueError:
        print("That is not a number")
    else:
        if choice == 1:
            UrlScan()
        elif choice == 2:
            CrowdSec()
        elif choice == 3:
            quit()
        else:
            print("Try Again")
