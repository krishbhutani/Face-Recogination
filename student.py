from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:

    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")              #Dimension of GUI
        self.root.title("Face Recoginition System")     #Title of GUI

        #***************VAriables***************
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()


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

        #Label of Page
        title_lbl = Label(self.root, text = "STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=130,width=1530,height=45)

        #Making a Frame
        main_frame = Frame(self.root,bd=2,bg="white")
        main_frame.place(x=0,y=175,width=1530,height=615)

        #Making a Frame --> Left Label Frame
        Left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Detail",font=("times new roman",15,"bold"),bg="white")
        Left_frame.place(x=40,y=10,width=700,height=580)

        img_left = Image.open(r"C:\Users\dell\OneDrive - NATIONAL INSTITUTE OF TECHNOLOGY HAMIRPUR HP\Desktop\DSA_2024-25\Face_Recogination\college_images\facial-recognition_0.jpg")
        img_left = img_left.resize((690,130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl3 = Label(Left_frame,image= self.photoimg_left)
        f_lbl3.place(x=5,y=0,width=686,height = 130)

        #Left Label Frame --> Current Course Information
        Curr_course = LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",11),bg="white")
        Curr_course.place(x=5,y=135,width=686,height=120)

        #Left Label Frame --> Current Course Information --> Department
        dep_lab = Label(Curr_course,text="Department",font=("times new roman",11,"bold"),bg="white")
        dep_lab.grid(row=0,column=0,padx=10)

        dep_combo = ttk.Combobox(Curr_course,textvariable=self.var_dep,font=("times new roman",11,"bold"),state = "readonly",width = 20)
        dep_combo.grid(row=0,column=1,padx=2)
        dep_combo["values"] = ("Select Department","CSE","MNC","EE","EC","CE","ME")
        dep_combo.current(0)

        #Left Label Frame --> Current Course Information --> Courses
        course_lab = Label(Curr_course,text="Courses",font=("times new roman",11,"bold"),bg="white")
        course_lab.grid(row=0,column=2,padx=10,pady=10)

        course_combo = ttk.Combobox(Curr_course,textvariable=self.var_course,font=("times new roman",11,"bold"),state = "readonly",width = 20)
        course_combo.grid(row=0,column=3)
        course_combo["values"] = ("Select Courses","MA-1","MA-2","MA-3","MA-4","MA-5","MA-6")
        course_combo.current(0)

        #Left Label Frame --> Current Course Information --> Semester
        sem_lab = Label(Curr_course,text="Semester",font=("times new roman",11,"bold"),bg="white")
        sem_lab.grid(row=1,column=0,padx=10,pady=10)

        sem_combo = ttk.Combobox(Curr_course,textvariable=self.var_semester,font=("times new roman",11,"bold"),state = "readonly",width = 20)
        sem_combo.grid(row=1,column=1,padx=2)
        sem_combo["values"] = ("Select Semester","1","2","3","4","5","6","7","8")
        sem_combo.current(0)

        #Left Label Frame --> Current Course Information --> Year
        year_lab = Label(Curr_course,text="Year",font=("times new roman",11,"bold"),bg="white")
        year_lab.grid(row=1,column=2,padx=10,pady=10)

        year_combo = ttk.Combobox(Curr_course,textvariable=self.var_year,font=("times new roman",11,"bold"),state = "readonly",width = 20)
        year_combo.grid(row=1,column=3)
        year_combo["values"] = ("Select Year","2028","2027","2026","2025","2024","2023")
        year_combo.current(0)

        #Left Label Frame --> Class Student Information
        Class_stu = LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",11),bg="white")
        Class_stu.place(x=5,y=260,width=686,height=290)

        #Left Label Frame --> Class Student Information -->Student ID
        stu_id = Label(Class_stu,text="StudentID: ",font=("times new roman",13,"bold"),bg="white")
        stu_id.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        stu_id_entry = ttk.Entry(Class_stu,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        stu_id_entry.grid(row = 0,column=1,padx=10,pady=5,sticky=W)

        #Left Label Frame --> Class Student Information -->Student Name
        stu_name = Label(Class_stu,text="Student Name: ",font=("times new roman",13,"bold"),bg="white")
        stu_name.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        stu_name_entry = ttk.Entry(Class_stu,width=19,textvariable=self.var_std_name,font=("times new roman",13,"bold"))
        stu_name_entry.grid(row = 0,column=3,padx=10,pady=5,sticky=W)

        #Left Label Frame --> Class Student Information -->Class Division
        stu_name = Label(Class_stu,text="Class Division: ",font=("times new roman",13,"bold"),bg="white")
        stu_name.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo = ttk.Combobox(Class_stu,textvariable=self.var_div,font=("times new roman",11,"bold"),state = "readonly",width = 20)
        div_combo.grid(row=1,column=1,padx=2)
        div_combo["values"] = ("1","2","3","4","5")
        div_combo.current(0)

        #Left Label Frame --> Class Student Information -->Roll No.
        Roll_no = Label(Class_stu,text="Roll No.: ",font=("times new roman",13,"bold"),bg="white")
        Roll_no.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Roll_no_entry = ttk.Entry(Class_stu,textvariable=self.var_roll,width=19,font=("times new roman",13,"bold"))
        Roll_no_entry.grid(row = 1,column=3,padx=10,pady=5,sticky=W)

        #Left Label Frame --> Class Student Information -->Gender
        gender = Label(Class_stu,text="Gender: ",font=("times new roman",13,"bold"),bg="white")
        gender.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo = ttk.Combobox(Class_stu,textvariable=self.var_gender,font=("times new roman",11,"bold"),state = "readonly",width = 20)
        gender_combo.grid(row=2,column=1,padx=2)
        gender_combo["values"] = ("Male","Female","Other")
        gender_combo.current(0)

        #Left Label Frame --> Class Student Information -->D.O.B
        DOB = Label(Class_stu,text="DOB: ",font=("times new roman",13,"bold"),bg="white")
        DOB.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        DOB_entry = ttk.Entry(Class_stu,textvariable=self.var_dob,width=19,font=("times new roman",13,"bold"))
        DOB_entry.grid(row = 2,column=3,padx=10,pady=5,sticky=W)

        #Left Label Frame --> Class Student Information -->Email
        mail = Label(Class_stu,text="Email: ",font=("times new roman",13,"bold"),bg="white")
        mail.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        mail_entry = ttk.Entry(Class_stu,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        mail_entry.grid(row = 3,column=1,padx=10,pady=5,sticky=W)

        #Left Label Frame --> Class Student Information -->Phone No.
        Phone_No = Label(Class_stu,text="Phone No.: ",font=("times new roman",13,"bold"),bg="white")
        Phone_No.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        Phone_No_entry = ttk.Entry(Class_stu,textvariable=self.var_phone,width=19,font=("times new roman",13,"bold"))
        Phone_No_entry.grid(row = 3,column=3,padx=10,pady=5,sticky=W)

        #Left Label Frame --> Class Student Information -->Address
        Address = Label(Class_stu,text="Address: ",font=("times new roman",13,"bold"),bg="white")
        Address.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Address_entry = ttk.Entry(Class_stu,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        Address_entry.grid(row = 4,column=1,padx=10,pady=5,sticky=W)

        #Left Label Frame --> Class Student Information -->Teacher Name
        Teacher = Label(Class_stu,text="Teacher Name: ",font=("times new roman",13,"bold"),bg="white")
        Teacher.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        Teacher_entry = ttk.Entry(Class_stu,textvariable=self.var_teacher,width=19,font=("times new roman",13,"bold"))
        Teacher_entry.grid(row = 4,column=3,padx=10,pady=5,sticky=W)

        #Left Label Frame --> Radio Button
        self.var_radio1 = StringVar()
        radiobutton1 = ttk.Radiobutton(Class_stu,text="Take Photo Sample",variable=self.var_radio1,value="Yes")
        radiobutton1.grid(row=6,column=0)

        
        radiobutton2 = ttk.Radiobutton(Class_stu,text="No Photo Sample",variable=self.var_radio1,value="No")
        radiobutton2.grid(row=6,column=1)

        #Left Label Frame --> Frame for Buttons
        Button_frame = Frame(Class_stu)
        Button_frame.place(x=8,y=200,width=670,height=35)

        #Left Label Frame --> Frame for Buttons --> Buttons
        save_btn = Button( Button_frame,command=self.add_data,text="Save",width = 16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        Update_btn = Button( Button_frame,command=self.update_data,text="Update",width =16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Update_btn.grid(row=0,column=1)

        del_btn = Button( Button_frame,command = self.delete_data,text="Delete",width = 15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        del_btn.grid(row=0,column=2)

        reset_btn = Button( Button_frame,command=self.reset_data,text="Reset",width = 16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        Button_frame2 = Frame(Class_stu)
        Button_frame2.place(x=8,y=235,width=670,height=35)

        take_photo_btn = Button( Button_frame2,command=self.generate_dataset,text="Take Photo Sample",width = 33,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        Update_photo_btn = Button( Button_frame2,text="Update Photo Sample",width =32,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Update_photo_btn.grid(row=0,column=1)

        

        #Making a Frame --> Right Label Frame
        Right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Detail",font=("times new roman",15,"bold"),bg="white")
        Right_frame.place(x=780,y=10,width=700,height=580)

        img_right = Image.open(r"C:\Users\dell\OneDrive - NATIONAL INSTITUTE OF TECHNOLOGY HAMIRPUR HP\Desktop\DSA_2024-25\Face_Recogination\college_images\facial-recognition_0.jpg")
        img_right = img_right.resize((690,130))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl4 = Label(Right_frame,image= self.photoimg_right)
        f_lbl4.place(x=5,y=0,width=686,height = 130)

        #************** Search System**************
        search_sys = LabelFrame(Right_frame,text="Search System",bd = 2, font=("times new roman",11),bg="white")
        search_sys.place(x=5,y= 140 ,width = 686 , height=60)

        Search_by = Label(search_sys,text="Search By :",font=("times new roman",12,"bold"),bg="red",fg = "white")
        Search_by.grid(row = 0,column = 0,padx=5,pady=5)

        search_by_combo = ttk.Combobox(search_sys,font=("times new roman",11,"bold"),state = "readonly",width = 20)
        search_by_combo.grid(row = 0,column = 1,padx=5,pady=5)
        search_by_combo["values"] = ("Select","Roll_No","Phone_No")
        search_by_combo.current(0)

        search_entry = ttk.Entry(search_sys, width = 15 ,font=("times new roman",11,"bold"))
        search_entry.grid(row = 0,column = 2,padx=5,pady=5)

        Search_btn = Button( search_sys,text="Search",width = 12,font=("times new roman",11,"bold"),bg="blue",fg="white")
        Search_btn.grid(row = 0,column = 3,padx=5,pady=5)

        Show_all_btn = Button(search_sys,text="Show All",width =12,font=("times new roman",11,"bold"),bg="blue",fg="white")
        Show_all_btn.grid(row = 0,column = 4,padx=5,pady=5)

        #********************Table Frame********
        table_frame = Frame(Right_frame)
        table_frame.place(x=5,y=205,width=686,height=340)

        scroll_x = ttk.Scrollbar(table_frame,orient="horizontal")
        scroll_y = ttk.Scrollbar(table_frame,orient="vertical")

        self.student_table = ttk.Treeview(table_frame,column = ("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll Number")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")

        self.student_table["show"] = "headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #*************Function for Data base*************
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="mysql@035",database = "face_recognizer")    
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                        
                                                                                    self.var_dep.get(),
                                                                                    self.var_course.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_semester.get(),
                                                                                    self.var_std_id.get(),
                                                                                    self.var_std_name.get(),
                                                                                    self.var_div.get(),
                                                                                    self.var_roll.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_dob.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_teacher.get(),
                                                                                    self.var_radio1.get()
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent =self.root)
            
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}",parent = self.root)

    #*********************fetch DATA******************
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="mysql@035",database = "face_recognizer")    
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #******************Get Cursor*************
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content =  self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])   
        


    # **********************Update Function ******************
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent = self.root)

        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update this student details",parent = self.root)

                if Update>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="mysql@035",database = "face_recognizer")    
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep = %s ,course = %s , Year = %s,Semester = %s,Name = %s, Division = %s,Roll = %s,Gender =%s, Dob = %s, Email = %s, Phone = %s, Address = %s, Teacher = %s , PhotoSample = %s where Student_id = %s",(
                        
                            
                                                                                        self.var_dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_semester.get(),
                                                                                        self.var_std_name.get(),
                                                                                        self.var_div.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_teacher.get(),
                                                                                        self.var_radio1.get(),
                                                                                        self.var_std_id.get()
                                                                                    ))

                else:
                    if not Update:
                        return
                
                messagebox.showinfo("Success","Student details successfully update completed",parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)

    #*******************Delete Function*************
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be registered",parent = self.root)
        else:
            try:
                delete= messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent = self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="mysql@035",database = "face_recognizer")    
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id = %s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent = self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)


    #*******************Reset*********************
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set(" ")
        self.var_std_name.set(" ")
        self.var_div.set("1")
        self.var_roll.set(" ")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    #********************Generate Data set Or Photo ***************
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent = self.root)

        else: 
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="mysql@035",database = "face_recognizer")    
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id +=1

                id = self.var_std_id.get()

                my_cursor.execute("update student set Dep = %s ,course = %s , Year = %s,Semester = %s,Name = %s, Division = %s,Roll = %s,Gender =%s, Dob = %s, Email = %s, Phone = %s, Address = %s, Teacher = %s , PhotoSample = %s where Student_id = %s",(
                        
                            
                                                                                        self.var_dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_semester.get(),
                                                                                        self.var_std_name.get(),
                                                                                        self.var_div.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_teacher.get(),
                                                                                        self.var_radio1.get(),
                                                                                        id
                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

           

                #-------------------Load predifiend data on face frontals from open cv------------

                face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #Minimum Neighbour =5

                    for(x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret, my_frame = cap.read()

                    if face_cropped(my_frame) is not None:
                        img_id +=1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                        file_name_path = f"data/user.{id}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Set Completed !!!")
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()