import os
import re
import csv


csv_dirs = []
csv_folder = "TrainingData"
for csv_file in os.listdir(csv_folder):
    csv_dirs.append(os.path.join(csv_folder, csv_file))

unique = []

for csv in csv_dirs:
    with open(csv, "r") as file:
        for line in file.readlines():
            try:
                row = line.split()
                number = line.split()[1]
                if re.match(r'^(0|[1-9][0-9]*)$', row[1]):
                    if row[1] not in unique:
                        unique.append(row[1])

                else:
                    if '"' in row[0]:
                        row = row[0][1::]
                        if row not in unique:
                            unique.append(row)
                    else:
                        unique.append(row[0])
            except IndexError:
                row = line.split(',')[0]
                if row not in unique:
                    unique.append(row)
            except Exception as E:
                print(E)
                break
        #break

def save_csv():
    with open("Combined.csv", "w") as file:
        writer = csv.writer(file)
        for row in unique:
            writer.writerow(row)


if __name__ == "__main__":
    save_csv()