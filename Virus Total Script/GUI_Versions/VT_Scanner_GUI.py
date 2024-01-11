import time
import requests
import threading
import PySimpleGUI as sg

sg.theme("DarkGrey5")

API_KEY = $YOUR_API_KEY

blocked = []
further_analysis = []
not_malicious = []
countries = []

def url_scan(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {'x-apikey': API_KEY}
    response = requests.get(url, headers=headers)
    scan_result = response.json()
    return scan_result

def scan_file(filename, multiline_elem):
    global blocked, further_analysis, not_malicious, countries

    try:
        with open(filename) as f:
            pass
    except IOError:
        sg.popup_error("File not accessible")
        return

    with open(filename, 'r') as f:
        for line in f:
            ip_address = line.strip()
            scan_result = url_scan(ip_address)
            marker = scan_result.get('data', {}).get('attributes', {}).get('last_analysis_stats', {}).get('malicious')
            country = scan_result.get('data', {}).get('attributes', {}).get('country')
            countries.append(country)

            if marker is None:
                result_text = f"No data available for {ip_address}\n"

            elif marker >= 5:
                with open('blocklist.txt', 'a') as blocklist_file:
                    blocklist_file.write(ip_address + '\n')
                blocked.append(ip_address)
                result_text = f"{ip_address} added to block list: has been marked malicious by {marker} engines\n"

            elif marker < 5 and marker >= 1:
                with open('further_analysis.txt', 'a') as blocklist_file:
                    blocklist_file.write(ip_address + '\n')
                further_analysis.append(ip_address)
                result_text = f"{ip_address} added to list for further analysis: has been marked malicious by {marker} engines\n"

            else:
                not_malicious.append(ip_address)
                result_text = f"{ip_address} has not been marked malicious by any engines\n"

            multiline_elem.print(result_text)  # Print the result to the multiline element
            time.sleep(15)

    countries = set(countries)
    result_text = (
        f"\n{len(blocked)} IP addresses added to the blocklist\n"
        f"{len(further_analysis)} IP addresses added to the list for further analysis\n"
        f"{len(not_malicious)} IP addresses not marked malicious by any engines\n"
        f"The following countries were found in the list: {countries}\n"
    )
    multiline_elem.print(result_text)

def scan_button_click(filename, multiline_elem):
    if not filename:
        sg.popup_error("Please select a file for scanning.")
        return

    threading.Thread(target=scan_file, args=(filename, multiline_elem), daemon=True).start()

# GUI layout
layout = [
    [
        sg.Text("Enter the full file name of the .txt file you want to scan: "),
        sg.In(size=(30, 1), enable_events=True, key="-FILE-"),
        sg.FileBrowse(),
    ],
    [sg.Button("Scan", key="-SCAN-", button_color=('white', 'green'), enable_events=True)],
    [sg.Multiline(size=(50, 20), key="-RESULTS-", text_color="black", autoscroll=True)],
]

window = sg.Window("VirusTotal IP Scanner", layout)

# Run the Event Loop
while True:
    event, values = window.read(timeout=100)

    if event == sg.WIN_CLOSED:
        break

    elif event == "-SCAN-":
        scan_button_click(values["-FILE-"], window["-RESULTS-"])

window.close()
