import requests
import json
import sys
import time
from pprint import pprint

print("""

Virus Total Limits API calls to 4 per minute - Your scans will be completed once per 15 seconds""")

time.sleep(3)

API_KEY = $YOUR_API_KEY

blocked = []
further_analysis = []
not_malicious = []


def url_scan(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {'x-apikey': API_KEY}
    response = requests.get(url, headers=headers)
    scan_result = response.json()
    return scan_result

while True:

    IP_LIST = input("Enter the full file name of the .txt file you want to scan:  ")
    try:
        with open(IP_LIST) as f:
            pass
    except IOError:
        print("File not accessible")
        continue

    with open(IP_LIST, 'r') as f:
        for line in f:
            ip_address = line.strip()  # Remove newline characters
            scan_result = url_scan(ip_address)
            pprint(scan_result)
            marker = scan_result.get('data', {}).get('attributes', {}).get('last_analysis_stats', {}).get('malicious')

            if marker >= 5:
                with open('blocklist.txt', 'a') as blocklist_file:
                    blocklist_file.write(ip_address + '\n')
                    blocked.append(ip_address)
                    print(f"""
                         
                          {ip_address} added to block list: has been marked malicious by {marker} engines
                          
                          """)
                time.sleep(15)
                    
            elif marker < 5 and marker >= 1:
                with open('futher_analysis.txt', 'a') as blocklist_file:
                    blocklist_file.write(ip_address + '\n')
                    further_analysis.append(ip_address)
                    print(f"""
                         
                          {ip_address} added to list for further analysis: has been marked malicious by {marker} engines
                          
                          """)
                time.sleep(15)
            
            else:
                not_malicious.append(ip_address)
                print(f"""
                         
                          {ip_address} has been not been marked malicious by any engines
                          
                          """)
                time.sleep(15)

                continue
            
    print(len(blocked), "IP addresses have been added to the blocklist")
    print(len(further_analysis), "IP addresses have been added to the list for further analysis")
    print(len(not_malicious), "IP addresses have not been marked malicious by any engines")

    choice = input("Would you like to scan an additional file? Enter [Y] or [N]  ")
    if choice == "Y":
        print("Looping for next file ")
        time.sleep(3)
    elif choice == "N":
        break
    else:
        print("Try again ")

print("Finished")
