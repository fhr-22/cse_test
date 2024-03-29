from jinja2 import Environment, FileSystemLoader
import os
import json
import sys
from datetime import datetime


def datestring():
    current_date = datetime.now()
    return current_date.strftime("%d-%m-%y")


def fakedate():
    x = sys.argv[1]
    return f"01-01-{x:02}"


def get_file_names(directory):
    files = os.listdir(directory)
    file_names = [os.path.splitext(file)[0] for file in files]
    return file_names


def get_fname_ext(directory):
    files = os.listdir(directory)
    file_data = [
        {"name": os.path.splitext(file)[0], "ext": os.path.splitext(file)[1]}
        for file in files
        if file != "ignore.txt"
    ]
    return file_data


def main():

    new_file_data_list = []

    current_file_data = get_fname_ext(f"..{os.sep}site{os.sep}notice_files")

    with open(f"..{os.sep}site{os.sep}notice_list.json", "r") as file:
        old_file_data_list = json.load(file)

    old_filenames = [x["name"] for x in old_file_data_list]

    # for adding new files
    for fname in current_file_data:
        if fname["name"] not in old_filenames:
            new_file_data_list.append(
                {"date": datestring(), "name": fname["name"], "ext": fname["ext"]}
            )

    # for removing deleted files
    current_filenames = [x["name"] for x in current_file_data]
    index = 0
    while index < len(old_file_data_list):
        if old_file_data_list[index]["name"] not in current_filenames:
            del old_file_data_list[index]
        else:
            index += 1

    new_file_data_list.extend(old_file_data_list)

    new_file_data_list.sort(
        key=lambda x: datetime.strptime(x["date"], "%d-%m-%y"), reverse=True
    )

    with open(f"..{os.sep}site{os.sep}notice_list.json", "w") as file:
        file.write(json.dumps(new_file_data_list))

    env = Environment(loader=FileSystemLoader(f"..{os.sep}templates"))
    template = env.get_template("notices.html")
    rendered_content = template.render(
        data=new_file_data_list,
        json_list=json.dumps([x["name"] for x in new_file_data_list]),
    )

    with open(f"..{os.sep}site{os.sep}notices.html", "w", encoding="utf-8") as file:
        file.write(rendered_content)


main()
