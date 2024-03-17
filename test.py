from jinja2 import Environment, FileSystemLoader
import os
import json
from datetime import datetime


def datestring():
    current_date = datetime.now()
    return current_date.strftime("%d-%m-%y")


def get_file_names(directory):
    files = os.listdir(directory)
    file_names = [os.path.splitext(file)[0] for file in files]
    return file_names


"""
- Get list of files in PDFs directory
- Get list of old files fron json datafile
- If there are new files, 
  update list data list with new entry and current date
- save json datafile
- render template

"""


def main():
    new_file_data_list = []

    current_filenames = get_file_names("site/notice_pdf")

    with open("site/notice_list.json", "r") as file:
        old_file_data_list = json.load(file)

    old_filenames = [x["name"] for x in old_file_data_list]

    # if there's a new file in the folder
    # add it to the new data list, along with date
    for fname in current_filenames:
        if fname not in old_filenames:
            new_file_data_list.append({"date": datestring(), "name": fname})

    # if there's a filename in old filenames that's not in current filenames
    # then we should remove those entries from old_file_list before extending current with it
    index = 0
    while index < len(old_file_data_list):
        if old_file_data_list[index]["name"] not in current_filenames:
            del old_file_data_list[index]
        else:
            index += 1

    new_file_data_list.extend(old_file_data_list)

    ## convert the new data list into json and write to file
    with open("site/notice_list.json", "w") as file:
        file.write(json.dumps(new_file_data_list))


main()
