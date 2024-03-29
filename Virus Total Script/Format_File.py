import os.path

def format_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Skip the header line
        next(infile)

        for line in infile:
            # Split the line by commas
            parts = line.strip().split(',')

            # Check if the line is not empty
            if parts:
                # Extract the IP address and write it to the output file
                ip_address = parts[0].strip('"')
                outfile.write(ip_address + '\n')

if __name__ == "__main__":
    input_file_name = input("Enter the input file name: ")
    output_file_name = os.path.splitext(input_file_name)[0] + "_formatted.txt"

    try:
        format_file(input_file_name, output_file_name)
        print(f"File '{output_file_name}' has been created with the desired format.")
    except Exception as e:
        print(f"An error occurred: {e}")
