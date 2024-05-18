import os
import glob
from tqdm import tqdm

def count_files_by_extension(directory): #counts the extention of every file it looks through
    extension_count = {}

    # Iterate through all files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Get the file extension
            _, extension = os.path.splitext(file)
            # Increment the count for this extension
            extension_count[extension] = extension_count.get(extension, 0) + 1

    print("File extensions and their counts:")
    for extension, count in extension_count.items():
        print(f"{extension}: {count}")

def find_string_in_files(folder_path, search_string): #finds searched string of all files
    stringoutput = []
    file_paths = glob.glob(os.path.join(folder_path, '**', '*'), recursive=True)
    with tqdm(total=len(file_paths), desc="Processing files") as pbar:
        for filename in file_paths:
            if os.path.isfile(filename): #check it its a file(if not its a folder)
                if "TextMap/TextMap" in filename:
                    if "TextMap/TextMapEN.json" not in filename: #only for english, we don't need anyone else
                        pbar.update(1)
                        continue
                elif '/Readable/' in filename:
                    if "/Readable/EN" not in filename: #only for english, we don't need anyone else, for now...
                        pbar.update(1)
                        continue
                try:
                    with open(filename, 'r', encoding='utf-8') as file:
                        for line_number, line in enumerate(file, start=1):
                            if search_string in line: #maybe convert them to lower? or maybe just exact string idk.....
                                stringoutput.append(f'Found "{search_string}" in {filename} at line {line_number}:')
                                stringoutput.append(line.rstrip())
                                stringoutput.append('---')
                    pbar.update(1)
                except UnicodeDecodeError:
                    stringoutput.append(f'Error decoding file: {filename}')
                    pbar.update(1)
            else:
                pbar.update(1)
    for i in stringoutput:
        print(i)

if __name__ == "__main__":
    folder_path = '' #folder path you will search through
    search_string = '' #the string you want to search in every file in the folder path

    find_string_in_files(folder_path, search_string)
    count_files_by_extension(folder_path)
