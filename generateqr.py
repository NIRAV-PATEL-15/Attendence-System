import csv
from tkinter import messagebox
import pyqrcode
import shutil,os
from pyqrcode import QRCode
import pandas as pd

def generate():
    data=pd.read_csv("StudentDetails\studentdata.csv")
    s=data['Enrollment'].to_list() 
    for i in range(0,len(s)):        
        # print(s[i])
        url = pyqrcode.create(s[i])
        url.png(s[i]+".png", scale=8)
        shutil.move(s[i]+".png","Qrcodes"+'/'+s[i]+".png")
    messagebox.showinfo("Success","Qr generated successfully ")
        
