# Attendance-using-pytessaract
It is a very simple project which takes in input of a small video file of all the people present in a meet and an excel file containing the students in a classroom

In attendance.py , trying changing the "croppedimage = img.crop((0,0,width, height))" line with suitable fills to get an output image similar to the image "0.jpg" uploaded above
Eg: croppedimage = img.crop((width-500,0,width, height))

Pytesseract reads each frame of the video and outputs the strings present in it . The output is stored and compared to find the absentees in a classroom
So its a very simple code , and very simple to understand , do try it out :)
