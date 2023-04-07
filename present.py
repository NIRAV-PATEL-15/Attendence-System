import csv
import pyqrcode
import shutil,os
from tkinter import messagebox
from pyqrcode import QRCode
import numpy as np
import cv2
import pandas as pd
import datetime
import time


def scan():
    #reading data
    sdata=pd.read_csv("StudentDetails\studentdata.csv")
    enrollments=sdata['Enrollment'].to_list()#separating lists of enrollment nos
    # print(enrollments)
    names=sdata['Name'].to_list()#getting names


    #setting values
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')




    exists = os.path.isfile("Attendance\Attendance_" + date + ".csv")

    #variable which stores enrollment of present students
    pdata=pd.read_csv("Attendance\Attendance_" + date + ".csv")
    p_enrollment=pdata['Enrollment'].to_list()

    # print(p_enrollment)



    #to enter data in attendence file
    def enterData(id,i):
        attendance = [str(enrollments[i]), '', str(names[i]), '', str(date), '', str(timeStamp)]
        if id in p_enrollment: 
            pass
        else:
            #  namez.append(id)
            
            with open(r"Attendance\Attendance_" + date + ".csv", 'a+') as f:
                writer = csv.writer(f)
                writer.writerow(attendance)
            f.close()
        
            print('Reading code.............')
                
    def checkData(data):
        # print(data)
        i=enrollments.index(data)
        # print(i)
        if data in p_enrollment:
         print('Already present')
        else:
            print('\n'+str(len (names[i])+1)+ '\n'+'Present done')
            enterData(data,i)
    
    
    #for capturing video
    cap=cv2.VideoCapture (0)
    detector=cv2.QRCodeDetector() 
    
    while True:
        _,frame=cap.read()
        f,b,_=detector.detectAndDecode(frame)
        if f:
            # print(f)
            checkData(f)
            time.sleep(1)

        cv2.imshow('Capturing Qr Codes', frame)
        if cv2.waitKey(1)&0xff==ord('q'):
            break
    cv2.destroyAllWindows()
    messagebox.showinfo("Success","Attendance successfully inserted")
            


        
        