import cv2
import sys
import os

def image_to_text(image_array, file_name):
    git_logs = open(file_name, 'w')

    git_logs.write(str(len(image_array[0])) + "\n")
    git_logs.write(str(len(image_array)) + "\n")

    for row in image_array:
        for char in row:
            # print (type(char))
            for color in char:
                git_logs.write(str(color) + " ")
            # git_logs.write(str(char))
            git_logs.write("\n")
    git_logs.close()

image_array = cv2.imread(sys.argv[1])
image_to_text(image_array, sys.argv[2])
