#ryt now, this program prints only title of each file, modify it make a dictionary, and store the necessary values of all the files in it.

import os
import requests

feed_dict = {}

for file in os.listdir():
    if file.endswith(".txt"):
        with open(file) as file_in:
            lines = []
            for line in file_in:
                lines.append(line.rstrip())

            feed_dict["title"] = lines[0]
            feed_dict["name"] = lines[1]
            feed_dict["date"] = lines[2]
            feed_dict["feedback"] = lines[3]

        print(feed_dict)

        if response.ok is "False":
            raise Exception("POST failed with status code {}".format(response.status_code))
        else:
            print("Added feedback successfully to the website !!!")    
