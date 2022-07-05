import os
import random as rnd
from PIL import Image

# Uses directory entered to iterate through all .JPG files and resize a random sample of pictures using the kth-sampling-method

directory = input("Please enter directory of pictures to be resized: ")

last_folder = os.path.basename(os.path.normpath(directory))

# TO-DO: add resizing customisation
ideal_width = 5472 / 2.0

suffix = 1
# TO-DO: cleanup path process with methods(?)
folder = directory + '/' + last_folder + '_resized'

while os.path.exists(folder + str(suffix)):
    suffix += 1

folder += str(suffix)

interval = input("Please enter a number for the interval at which sample should be picked (using random starting point): ")

if interval.isnumeric() == False or int(interval) <= 0:
    raise Exception("Please enter an integer bigger than 0")

interval = int(interval)

os.mkdir(folder)

print("\nFolder created which contains resized sample: " + folder)

keep_names = input("Do you want to preserve the names of the picture files? (Y/N) ")

change_name = False

if keep_names == "N":
    change_name = True
elif keep_names != "Y":
    raise Exception("Answer not included in choices (Y/N)")


cnt = 1
kth = rnd.randint(0,interval-1)

for image_path in os.listdir(directory):
    if image_path.endswith(".JPG"):
        if kth == 0:
            img = Image.open(directory + '/' + image_path)
            
            scale = ideal_width/float(img.width)
            new_height = int(float(img.height) * scale)
            img = img.resize((int(ideal_width), new_height), Image.ANTIALIAS)

            #print(ideal_width, new_height)

            if change_name == True:
                img.save(folder + '/pic' + str(cnt) + '.JPG')
            else:
                img.save(folder + '/' + image_path)
            cnt += 1

            kth = interval
        kth -= 1

print("Resized " + str(cnt-1) + " pictures")


