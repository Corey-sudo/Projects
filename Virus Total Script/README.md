# Virus Total Automated Scanning

This script is meant to scan a .txt file of IP addresses that are listed one per line and both provide the output of the Virus Total scan as well as add the scanned addresses to new .txt files for further analysis or suggested blocking. The current print statement has been commented out - the data from each response when scanning large files can create a large terminal with unnecessary information.  If you are scanning smaller files feel free to add the print statement back in.

## In order to use the scanning script in this repository, you'll first need to obtain a free API from Virustotal.com

A sample of IP addresses from Firhol has been provided for you to run through the scanner.  There is a fork of the firehol IP block list on the main repository where you can download additional lists of IP addresses. Additional IP lists curated from a TPOT deployment on Azure are collected and added here when possible.

## TPOT Integration and Data

I currently am running a TPOT honeypot on an Azure cloud deployment.  I intend to pull attacker source IPs and upload them here. When pulled from Kibana these files are formatted as a CSV file with some additional characters surrounding the IP addresses.  The last format.py script allows you to convert a TPOT Kibana CSV file into a .txt file formatted correctly for the virust total script.

