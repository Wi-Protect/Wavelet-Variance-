import csv


def write_to_csv(file_path, data):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def delete_all_records(file_path):
    with open(file_path, 'w', newline='') as file:
        file.truncate()
