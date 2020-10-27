import pandas as pd
from PIL import Image
import cv2
import numpy as np
from openpyxl import Workbook,load_workbook
import pytesseract


# video filename
cap = cv2.VideoCapture('/home/prajith_v/Videos/dbms.mp4')

# loading the student names in my class
names = pd.read_excel("/home/prajith_v/Downloads/Attendance _harsh.xlsx")

Students = names["Name "].tolist()
print("reading data over...")

# finding the names present in the classroom
present=[]
while(cap.isOpened()):
    ret, frame = cap.read()
    try:
        img = Image.fromarray(frame)
        width, height = img.size
        # sample of cropping the image : croppedimage = img.crop((width-500,0,width, height))
        croppedimage = img.crop((0,0,width, height))
        text = pytesseract.image_to_string(croppedimage)
        text = text.lower()
        for student in Students:
            if student.lower() in text:
                if student not in present:
                    present.append(student)

    except:
        break


print("finding absentees......")

# comparing the names present in the video with the list of all students in the class and finding the missing ones
absent=[]
for i in Students:
    if i not in present:
        absent.append(i)

abs = pd.DataFrame({"Absent":absent})

print("saving as absentees.xlsx.........")

abs.to_excel("absentees.xlsx")
