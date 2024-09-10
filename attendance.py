from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Attendane:

    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")              #Dimension of GUI
        self.root.title("Face Recoginition System")     #Title of GUI

        #Header Image One
        img1 = Image.open(r"college_images\smart-attendance.jpg")
        img1 = img1.resize((800,200))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root,image = self.photoimg1)
        f_lbl1.place(x=0,y=0,width=800,height = 200)

        #Header Image Two
        img2 = Image.open(r"college_images\facialrecognition.png")
        img2 = img2.resize((800,200))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root,image= self.photoimg2)
        f_lbl2.place(x=510,y=0,width=510,height = 130)


if __name__ == "__main__":
    root = Tk()
    obj = Attendane(root)
    root.mainloop()