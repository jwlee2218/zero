#!/usr/local/bin/python3
 
import cv2
import argparse
import os
import functools
from functools import cmp_to_key
 
def help ():
    with open(__file__, "r", encoding="UTF-8") as open_file:
        for line in open_file:
            if ":" in line and "def" in line and "if " not in line:
                print(line.split(" ")[1])
 
#Function to check if string can be cast to int
def isnum (num):
    try:
        int(num)
        return True
    except:
        return False
 
#Numerically sorts filenames
def image_sort_name (x,y):
   
    x = int(x.split(".")[0])
    y = int(y.split(".")[0])
    return x-y
 
#Sort filenames by their last edited datetime stamp
#This way, even if you didn't name and number your frames, you can still use their order of creation for sorting
#10/10! :)
def image_sort_datetime (x,y):
    x = os.path.getmtime(x)
    y = os.path.getmtime(y)
    return x - y
 
def render ():
    # Construct the argument parser and parse the arguments
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-e", "--extension", required=False, default='png', help="Extension name. default is 'png'.")
    arg_parser.add_argument("-o", "--output", required=False, default='output.mp4', help="Output video file.")
    arg_parser.add_argument("-d", "--directory", required=False, default='.', help="Specify image directory.")
    arg_parser.add_argument("-fps", "--framerate", required=False, default='10', help="Set the video framerate.")
    arg_parser.add_argument("-s", "--sort", required=False, default='numeric', help="Determines the type of file-order sort that will be used. Current values: none, numeric, datetime")
    arg_parser.add_argument("-t", "--time", required=False, default='none', help="Sets the framerate so that the video length matches the time in seconds.")
    arg_parser.add_argument("-v", "--visual", required=False, default='false', help="If 'true' then will display preview window.")
    arg_parser.add_argument("-safe", "--safe", required=False, default='true', help="If 'false' then will try to render all images, not just consistenly-sized ones.")
    args = vars(arg_parser.parse_args())
 
    # Arguments
    dir_path = args['directory']
    ext = args['extension']
    output = args['output']
    framerate = args['framerate']
    sort_type = args['sort']
    time = args['time']
    visual = args['visual']
 
    #Flips bools to a bool-type
    visual = visual == "true"
    safe = args['safe'] == "true"
 
    #Sets the framerate to argument, or defaults to 10
    if not isnum(framerate):
        framerate = 10
    else:
        framerate = int(framerate)
 
    #Get the files from directory
    images = []
    for f in os.listdir(dir_path):
        if f.endswith(ext):
            images.append(f)
 
    #Sort the files found in the directory
    if sort_type == "numeric":
        int_name = images[0].split(".")[0]
        if isnum(int_name):
            images = sorted(images, key=cmp_to_key(image_sort_name))
        else:
            print("Failed to sort numerically, switching to alphabetic sort")
            images.sort()
    elif sort_type == "datetime":
        images = [dir_path + "/" + im for im in images]
        images = sorted(images, key=cmp_to_key(image_sort_datetime))
        images = ["".join(im.split(dir_path + "/")[1:]) for im in images]
    elif sort_type == "alphabetic":
        images.sort()
 
    #Change framerate to fit the time in seconds if a time has been specified.
    #Overrides the -fps arg
    if isnum(time):
        framerate = int(len(images) / int(time))
        print("Adjusting framerate to " + str(framerate))
 
    # Determine the width and height from the first image
    image_path = os.path.join(dir_path, images[0])
    frame = cv2.imread(image_path)
 
    if visual:
        cv2.imshow('video',frame)
    regular_size = os.path.getsize(image_path)
    height, width, channels = frame.shape
 
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
    out = cv2.VideoWriter(output, fourcc, framerate, (width, height))
 
    for n, image in enumerate(images):
        image_path = os.path.join(dir_path, image)
        image_size = os.path.getsize(image_path)
        if image_size < regular_size / 1.5 and safe:
            print("Cancelled: " + image)
            print("Abnormal image size. Use the '-safe false' to disable this check")
            continue
 
        frame = cv2.imread(image_path)
        out.write(frame) # Write out frame to video
        if visual:
            cv2.imshow('video', frame)
 
        if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
            break
        if n%100 == 0:
            print("Frame " + str(n))
 
    # Release everything if job is finished
    out.release()
    cv2.destroyAllWindows()
 
    print("The output video is {}".format(output))
 
if __name__ == "__main__":
    do = "[]"
    while do not in "[q][quit][end][exit][-q]":
        do = "[" + input("do: ").lower() + "]"
        if do in "[render]":
            render()
        elif do in "[-h][h][help][--help][--h]":
            help()
    print("Bye!")
