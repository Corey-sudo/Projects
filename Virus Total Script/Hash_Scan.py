import requests
import json
import hashlib
import time
import sys
from pprint import pprint


API_KEY = $Your_API_Key

while True:

    def file_scan(hash):
        url = f"https://www.virustotal.com/api/v3/files/{hash}"
        headers = {'x-apikey': API_KEY}
        response = requests.get(url, headers=headers)
        scan_result = response.json()
        malicious = scan_result.get('data', {}).get('attributes', {}).get('total_votes', {}).get('malicious')
    
        print(f"\nThis file has been marked malicious {malicious} times")

    def sha256sum(file):
        try:
            with open(file, 'rb', buffering=0) as f:
                return hashlib.file_digest(f, 'sha256').hexdigest()
        except IOError:
            print("File not accessible - please check your path and spelling and run the script again")
            sys.exit()
    
    file = input("What file would you like to analyze?  ")
    file_hash = sha256sum(file)


    print("""

    Conducting Virus Total Scan of File...""")

    print(f"\nThe SHA256 has of your file is {file_hash}")

    time.sleep(3)

    def file_scan(hash):
        url = f"https://www.virustotal.com/api/v3/files/{hash}"
        headers = {'x-apikey': API_KEY}
        response = requests.get(url, headers=headers)
        scan_result = response.json()
        malicious = scan_result.get('data', {}).get('attributes', {}).get('total_votes', {}).get('malicious')
        print(scan_result)    
        print(f"\nThis file has been marked malicious {malicious} times")


    file_scan(file_hash)

    Vote = input('If you would like to add a vote, please type either malicious or harmless.  If you would like to skip the vote enter type skip  ')
    if Vote != 'skip':
        url = f'https://www.virustotal.com/api/v3/files{hash}/votes'
        headers = {'x-apikey': API_KEY, 'Content-Type': 'application/json',}
        data = {'data': {'type': 'vote', 'attributes': {'verdict': Vote,}}}
    else:
        continue

    Vote_Result = requests.post(url, headers=headers, json=data)
    print(Vote_Result.json())

    
    choice = input("Would you like to scan an additional file? Enter [Y] or [N]  ")
    if choice == "Y":
        print("Looping for next file ")
        time.sleep(3)
    else:
        print('Goodbye')
        sys.exit
