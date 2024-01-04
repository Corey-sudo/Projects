def format_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line_num, line in enumerate(infile, start=1):
                if line_num < 7:
                    # Skip the first 6 lines
                    continue

                # Split the line by whitespace
                parts = line.strip().split(' ')

                ip_address = parts[0].strip('"')
                if not ip_address:
                    print(f"Error processing line {line_num}: No IP address found")
                    continue

                outfile.write(ip_address + '\n')

                # Remove the final two lines
                with open(output_file, 'r+') as outfile:
                    lines = outfile.readlines()
                    outfile.seek(0)
                    outfile.truncate()
                    outfile.writelines(lines[:-2])


        print(f"File '{output_file}' has been created with the desired format.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    try:
        input_file_name = input("Enter the input file name: ")
        output_file_name = input("Enter the output file name: ")

        format_file(input_file_name, output_file_name)

    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
