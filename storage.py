import csv
import os

class Storage:

    # Saving or updating data into a csv file on the basis append flag
    def save_data(self, filename, data, headers, append=False):
        file_exists = os.path.isfile(filename)

        mode = 'a' if append and file_exists else 'w'
        with open(filename, mode = mode, newline='') as file:
            writer = csv.DictWriter(file, fieldnames= headers)
            if not file_exists or not append:
                writer.writeheader()
            writer.writerows(data)
    

    # Loading data from a csv file
    def load_data(self, filename, headers):
            try:
                with open(filename, mode='r', newline='') as file:
                    reader = csv.DictReader(file, fieldnames=headers)
                    next(reader)
                    return [row for row in reader]
            except FileNotFoundError:
                return[]