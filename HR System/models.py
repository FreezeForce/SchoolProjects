import os
import glob
import csv
import sys

class Employee:
    def __init__(self, efname, elname, empbirthday, emphiredate, eage, esex, ):
        # declare
        self.efname = efname
        self.elname = elname
        self.empbirthday = empbirthday
        self.emphiredate = emphiredate
        self.eage = eage
        self.esex = esex
    

    # Show .mp4 files in directory and play input
    def playvideo():
        mp4_files = glob.glob('*.mp4')
        # Print out the list of .mp4 video files inside current directory 
        print("Available Video files:")
        for f in mp4_files:
            print(f)

        # enter the name of the video file
        filename1 = input("Enter the name of the video you want to play (without '.mp4'): ")
        filename2 = (filename1+'.mp4')
        # Play the selected file using os.system
        if filename2.lower() in mp4_files:
            os.system("start " + filename2)
        else:
            print("File not found!")
