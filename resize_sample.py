import os
import random as rnd
from PIL import Image

# Uses directory that it is ran in to iterate through all .png files and resize a random sample of pictures

directory = os.getcwd()

#print(directory)

ideal_width = 5472 / 2.0

num = 1
folder = directory + '/resized_picture_sample'

while os.path.exists(folder + str(num)):
    num += 1

folder += str(num)

interval = input("Please enter a number for the interval at which sample should be picked (using random starting point): ")

if interval.isnumeric() == False or int(interval) <= 0:
    raise Exception("Please enter an integer bigger than 0")

interval = int(interval)

os.mkdir(folder)

print("\nFolder created with resized sample: " + folder)

cnt = 1
kth = rnd.randint(0,interval-1)

for image_path in os.listdir(directory):
    if image_path.endswith(".JPG"):
        if kth == 0:
            img = Image.open(image_path)
            
            scale = ideal_width/float(img.width)
            new_height = int(float(img.height) * scale)
            img = img.resize((int(ideal_width), new_height), Image.ANTIALIAS)

            #print(ideal_width, new_height)

            img.save(folder + '/pic' + str(cnt) + '.JPG')
            cnt += 1

            kth = interval
        kth -= 1

print("Resized " + str(cnt-1) + " pictures")


