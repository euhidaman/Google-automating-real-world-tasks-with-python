import os
from PIL import Image

old_path = os.path.expanduser('~') + '\mnt\c\Users\Dell\Desktop\googlepython\Google-automating-real-world-tasks-with-python\Week1-Scale-and-convert-images-using-PIL\images'
# my images were in the 'images' sub-folder was in the folder 'Week1-Scale-and-convert-images-using-PIL'

new_path = os.path.expanduser('~') + '\mnt\c\Users\Dell\Desktop\googlepython\Google-automating-real-world-tasks-with-python\Week1-Scale-and-convert-images-using-PIL\image_new'
# I saved the modified images in the sub-folder 'image_new', present in the main folder 'Week1-Scale-and-convert-images-using-PIL'

for image in os.listdir(old_path):
    print(image)
    if '.' not in image[0]:
        img = Image.open(old_path + image)
        img.rotate(-90).resize((128, 128)).convert("RGB").save(new_path + image.split('.')[0], 'jpeg')
        img.close()
