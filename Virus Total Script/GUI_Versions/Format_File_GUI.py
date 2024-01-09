import PySimpleGUI as sg
import os.path

def format_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Skip the header line
        next(infile)

        for line in infile:
            # Split the line by commas
            parts = line.strip().split(',')

            # Extract the IP address and write it to the output file
            ip_address = parts[0].strip('"')
            outfile.write(ip_address + '\n')

file_list_column = [
    [
        sg.Text("File Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
    [
        sg.Button("Format", key="-FORMAT-"),
    ],
]

layout = [
    [
        sg.Column(file_list_column),
    ]
]

window = sg.Window("File Formatter", layout)


while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get a list of files in the folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".txt", '.csv'))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":
        pass 
    elif event == "-FORMAT-":  # Format button was clicked
        if values["-FILE LIST-"]:
            input_file_name = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            output_file_name = os.path.splitext(input_file_name)[0] + "_formatted.txt"
            format_file(input_file_name, output_file_name)
            sg.popup(f"File '{output_file_name}' has been created with the desired format.")

window.close()
