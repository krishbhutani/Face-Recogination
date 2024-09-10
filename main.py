from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
import os
from face_recognition import FaceRecognition

class Face_Recognition_System:

    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")              #Dimension of GUI
        self.root.title("Face Recoginition System")     #Title of GUI

        #Header Image One
        img1 = Image.open(r"C:\Users\dell\OneDrive - NATIONAL INSTITUTE OF TECHNOLOGY HAMIRPUR HP\Desktop\DSA_2024-25\Face_Recogination\college_images\Stanford.jpg")
        img1 = img1.resize((510,130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root,image = self.photoimg1)
        f_lbl1.place(x=0,y=0,width=510,height = 130)

        #Header Image Two
        img2 = Image.open(r"C:\Users\dell\OneDrive - NATIONAL INSTITUTE OF TECHNOLOGY HAMIRPUR HP\Desktop\DSA_2024-25\Face_Recogination\college_images\facialrecognition.png")
        img2 = img2.resize((510,130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root,image= self.photoimg2)
        f_lbl2.place(x=510,y=0,width=510,height = 130)

        #Header Image Three
        img3 = Image.open(r"C:\Users\dell\OneDrive - NATIONAL INSTITUTE OF TECHNOLOGY HAMIRPUR HP\Desktop\DSA_2024-25\Face_Recogination\college_images\u.jpg")
        img3 = img3.resize((510,130))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl3 = Label(self.root,image= self.photoimg3)
        f_lbl3.place(x=1020,y=0,width=510,height = 130)

        #background Image
        img4 = Image.open(r"C:\Users\dell\OneDrive - NATIONAL INSTITUTE OF TECHNOLOGY HAMIRPUR HP\Desktop\DSA_2024-25\Face_Recogination\college_images\wp2551980.jpg")
        img4 = img4.resize((1530,660))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image= self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height = 660)

        #Title
        title_lbl = Label(bg_img, text = "FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"))
        title_lbl.place(x=0,y=0,width=1530,height=45) 

        #Student Detail Button
        img5 = Image.open(r"C:\Users\dell\OneDrive - NATIONAL INSTITUTE OF TECHNOLOGY HAMIRPUR HP\Desktop\DSA_2024-25\Face_Recogination\college_images\gettyimages-1022573162.jpg")
        img5 = img5.resize((220,220))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoimg5 ,command=self.student_details,cursor="hand2")
        b1.place(x=205,y=100,width=220,height= 220)

        b1_1 = Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"))
        b1_1.place(x=205,y=300,width=220,height= 40)

        #Face Recogintion Button
        img6 = Image.open(r"C:\Users\dell\OneDrive - NATIONAL INSTITUTE OF TECHNOLOGY HAMIRPUR HP\Desktop\DSA_2024-25\Face_Recogination\college_images\face_detector1.jpg")
        img6 = img6.resize((220,220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2 = Button(bg_img,image=self.photoimg6 ,cursor="hand2",command=self.face_data)
        b2.place(x=505,y=100,width=220,height= 220)

        b2_2 = Button(bg_img,text="FACE RECOGINITION",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"))
        b2_2.place(x=505,y=300,width=220,height= 40)

        #Attendance Button
        img7 = Image.open(r"C:\Users\dell\OneDrive - NATIONAL INSTITUTE OF TECHNOLOGY HAMIRPUR HP\Desktop\DSA_2024-25\Face_Recogination\college_images\report.jpg")
        img7 = img7.resize((220,220))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b3 = Button(bg_img,image=self.photoimg7 ,cursor="hand2")
        b3.place(x=805,y=100,width=220,height= 220)

        b3_3 = Button(bg_img,text="ATTENDANCE",cursor="hand2",font=("times new roman",15,"bold"))
        b3_3.place(x=805,y=300,width=220,height= 40)

        #Help Button
        img8 = Image.open(r"C:\Users\dell\OneDrive - NATIONAL INSTITUTE OF TECHNOLOGY HAMIRPUR HP\Desktop\DSA_2024-25\Face_Recogination\college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img8 = img8.resize((220,220))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b4 = Button(bg_img,image=self.photoimg8 ,cursor="hand2")
        b4.place(x=1105,y=100,width=220,height= 220)

        b4_4 = Button(bg_img,text="HELP",cursor="hand2",font=("times new roman",15,"bold"))
        b4_4.place(x=1105,y=300,width=220,height= 40)

        #Train Data Button
        img9 = Image.open(r"C:\Users\dell\OneDrive - NATIONAL INSTITUTE OF TECHNOLOGY HAMIRPUR HP\Desktop\DSA_2024-25\Face_Recogination\college_images\Train.jpg")
        img9 = img9.resize((220,220))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b5 = Button(bg_img,image=self.photoimg9 ,cursor="hand2",command=self.train_data)
        b5.place(x=205,y=380,width=220,height= 220)

        b5_5 = Button(bg_img,text="TRAIN DATA",cursor="hand2",font=("times new roman",15,"bold"),command=self.train_data)
        b5_5.place(x=205,y=580,width=220,height= 40)

        #Photos Button
        img10 = Image.open(r"C:\Users\dell\OneDrive - NATIONAL INSTITUTE OF TECHNOLOGY HAMIRPUR HP\Desktop\DSA_2024-25\Face_Recogination\college_images\sample.jpg")
        img10 = img10.resize((220,220))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b6 = Button(bg_img,image=self.photoimg10 ,cursor="hand2",command = self.open_img)
        b6.place(x=505,y=380,width=220,height= 220)

        b6_6 = Button(bg_img,text="PHOTOS",cursor="hand2",font=("times new roman",15,"bold"),command = self.open_img)
        b6_6.place(x=505,y=580,width=220,height= 40)

        #Developer Button
        img11 = Image.open(r"C:\Users\dell\OneDrive - NATIONAL INSTITUTE OF TECHNOLOGY HAMIRPUR HP\Desktop\DSA_2024-25\Face_Recogination\college_images\dev.jpg")
        img11 = img11.resize((220,220))
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b7 = Button(bg_img,image=self.photoimg11 ,cursor="hand2")
        b7.place(x=805,y=380,width=220,height= 220)

        b7_7 = Button(bg_img,text="DEVELOPER",cursor="hand2",font=("times new roman",15,"bold"))
        b7_7.place(x=805,y=580,width=220,height= 40)

        #Exit Button
        img12 = Image.open(r"C:\Users\dell\OneDrive - NATIONAL INSTITUTE OF TECHNOLOGY HAMIRPUR HP\Desktop\DSA_2024-25\Face_Recogination\college_images\exit.jpg")
        img12 = img12.resize((220,220))
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b8 = Button(bg_img,image=self.photoimg12 ,cursor="hand2")
        b8.place(x=1105,y=380,width=220,height= 220)

        b8_8 = Button(bg_img,text="EXIT",cursor="hand2",font=("times new roman",15,"bold"))
        b8_8.place(x=1105,y=580,width=220,height= 40)

    def open_img(self):
        os.startfile("data")
        


    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)



    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=FaceRecognition(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

    