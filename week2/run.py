# make sure to write this script in the home directory.
# to go to home directory, use the command --> cd ~

import os
import requests

path = '/data/feedback/'
feed_dict = {}

for file in os.listdir():
    with open(path + file) as file_in:
            lines = []
            for line in file_in:
                lines.append(line.rstrip())

            feed_dict["title"] = lines[0]
            feed_dict["name"] = lines[1]
            feed_dict["date"] = lines[2]
            feed_dict["feedback"] = lines[3]

        print(feed_dict)

        response = requests.post("http://34.121.110.232/feedback/", json = feed_dict)

        if response.ok is "False":
            raise Exception("POST failed with status code {}".format(response.status_code))
        else:
            print("Added feedback successfully to the website !!!")
