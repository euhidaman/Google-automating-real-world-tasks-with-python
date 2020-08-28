# If you are using this to solve the "Automating Real-World Tasks with Python-Week 1" assessment.
# then, write this file in the home directory, storing the sub directories "images" and "/opt/icons/".
# to go to home directory, use this command ----> cd~

import os
from PIL import Image

old_path = os.path.expanduser('~') + '\mnt\c\Users\Dell\Desktop\googlepython\Google-automating-real-world-tasks-with-python\Week1-Scale-and-convert-images-using-PIL\images'
# my images were in the 'images' sub-folder was in the folder 'Week1-Scale-and-convert-images-using-PIL'

new_path = os.path.expanduser('~') + '\mnt\c\Users\Dell\Desktop\googlepython\Google-automating-real-world-tasks-with-python\Week1-Scale-and-convert-images-using-PIL\image_new'
# I saved the modified images in the sub-folder 'image_new', present in the main folder 'Week1-Scale-and-convert-images-using-PIL'

#to solve the qwiklabs assesment, use the below lines, instead of the above lines ---->
#old_path = os.path.expanduser('~') + '/images/'
#new_path = '/opt/icons/'

for image in os.listdir(old_path):
    if image.endswith("48dp"):
        img = Image.open(old_path + image)
        img.rotate(-90).resize((128, 128))
        img.convert("RGB").save(new_path + image.split('.')[0], 'jpeg')
        img.close()
