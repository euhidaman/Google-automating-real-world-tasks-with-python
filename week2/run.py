#ryt now, this program prints only title of each file, modify it make a dictionary, and store the necessary values of all the files in it.

import os
import requests

feed_store = []

for file in os.listdir():
    if file.endswith(".txt"):
        with open(file) as file_in:
            lines = []
            for line in file_in:
                lines.append(line.rstrip())

            title = lines[0]
            name = lines[1]
            date = lines[2]
            feedback = lines[3]
            print(title)


#print(lines)
#print(name)
