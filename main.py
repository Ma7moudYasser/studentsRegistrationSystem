from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import mysql.connector

class Student:
    #-----------Making the window of the program---------------
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x690+250+200')
        self.root.title('[School Management System]')
        self.root.config(background= "silver")
        self.root.iconbitmap('school.ico')
        self.root.resizable(False, False)
        title = Label(self.root,
                      text = '[Students registeration system]',
                      bg = '#F03F07',
                      font = ('monospace', 14),
                      fg = 'white'
                      )
        title.pack(fill=X)


        #-------------variables -----------

        self.id_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.phone_var = StringVar()
        self.qual_var = StringVar()
        self.gender_var = StringVar()
        self.address_var = StringVar()
        self.se_by = StringVar()
        self.se_var = StringVar()
        self.del_var = StringVar()

    #-----------Management tools of the program-----------------

        Manage_Frame = Frame(self.root, bg = 'white')
        Manage_Frame.place(x=1137, y=30, width=210, height=400)
        lbl_ID = Label(Manage_Frame, text = 'Serial Number',
                       bg = 'white')
        lbl_ID.pack()
        ID_entry = Entry(Manage_Frame, textvariable = self.id_var, bd='2')
        ID_entry.pack()
        lbl_name = Label(Manage_Frame, bg = 'white',
                         text = 'Student Name')
        lbl_name.pack()
        Name_entry = Entry(Manage_Frame,textvariable = self.name_var, bd = '2')
        Name_entry.pack()
        lbl_email = Label(Manage_Frame, bg = 'white',
                         text = 'Email')
        lbl_email.pack()
        email_entry = Entry(Manage_Frame,textvariable = self.email_var, bd = '2')
        email_entry.pack()
        lbl_phone = Label(Manage_Frame, bg = 'white',
                         text = 'Phone')
        lbl_phone.pack()
        phone_entry = Entry(Manage_Frame,textvariable = self.phone_var, bd = '2')
        phone_entry.pack()

        lbl_qual = Label(Manage_Frame, bg = 'white',
                          text = 'Qualifications')
        lbl_qual.pack()

        qual_entry = Entry(Manage_Frame,text = self.qual_var, bd = '2')
        qual_entry.pack()


        lbl_gender = Label(Manage_Frame, text = 'choose gender',
                           bg = 'white')
        lbl_gender.pack()

        combo_gender = ttk.Combobox(Manage_Frame, textvariable = self.gender_var)
        combo_gender['value'] = ('male', 'female')
        combo_gender.pack()


        lbl_address = Label(Manage_Frame, text = 'Student Address', bg= 'white')
        lbl_address.pack()

        address_entry = Entry(Manage_Frame, textvariable = self.address_var ,bd = '2')
        address_entry.pack()

        lbl_delete = Label(Manage_Frame, fg = 'red', bg = 'white', text = 'Delete student with name')
        lbl_delete.pack()

        delete_entry = Entry(Manage_Frame, textvariable = self.del_var, bd = '2')
        delete_entry.pack()



        #---------Buttons -----------------------

        btn_Frame = Frame(self.root, bg = 'white')
        btn_Frame.place(x = 1137, y = 435, width = 210, height = 253)


        title1 = Label(btn_Frame, text = 'Dashboard', font = ('Deco', 14), fg = 'white', bg = '#F03F07')
        title1.pack(fill = X)


        add_btn = Button(btn_Frame, text = 'Adding Student', bg = '#58D68D', fg = 'white', command = self.add_student)
        add_btn.place(x = 33, y = 39, width = '150', height = '30')
        del_btn  = Button(btn_Frame, text = 'Delete Student', bg = '#CB4335', fg = 'white', command = self.delete)
        del_btn.place(x=33, y=80, width='150', height='30')
        update_btn  = Button(btn_Frame, text = 'Update Data', bg = '#5DADE2', fg = 'white', command = self.update)
        update_btn.place(x=33, y=115, width='150', height='30')
        clear_btn  = Button(btn_Frame, text = 'Clearing Data', bg = '#34495E', fg = 'white', command = self.clear)
        clear_btn.place(x=33, y=150, width='150', height='30')
        about_btn  = Button(btn_Frame, text = 'About', bg = '#5B2C6F', fg = 'white', command = self.about)
        about_btn.place(x=33, y=185, width='150', height='30')
        exit_btn  = Button(btn_Frame, text = 'Exit', bg = 'black', fg = 'white', command= root.quit)
        exit_btn.place(x=33, y=225, width='150', height='30')
        # --------- Search Manage -----------------------
        search_frame = Frame(self.root, bg = 'white')
        search_frame.place(x= 1, y = 30, width = 1134, height = 50)


        lbl_search = Label(search_frame, text = 'search for student',
                           bg = 'white')
        lbl_search.place(x=10, y =12)

        combo_search = ttk.Combobox(search_frame, textvariable = self.se_by)
        combo_search['value'] = ('id', 'name', 'email', 'phone')
        combo_search.place(x = 115, y=12)


        search_Entry = Entry(search_frame, textvariable = self.se_var ,bd = '2')
        search_Entry.place(x= 265, y=12)

        se_btn = Button(search_frame, text = 'search', bg = '#3498DB', fg = 'white', command= self.search)
        se_btn.place(x=405, y=12, width = 100, height = 25)


        #---------Details ----------------------

        details_frame = Frame(self.root, bg ='#F03F07')
        details_frame.place(x=1, y=82, width = 1134, height = 605)
        #-----------scroll ------------
        scroll_x = Scrollbar(details_frame, orient = HORIZONTAL)
        scroll_y = Scrollbar(details_frame, orient = VERTICAL)
        #---------Treeview-------
        self.student_table = ttk.Treeview(details_frame,
                                          columns = ('id', 'name', 'email', 'phone','qualifications', 'gender', 'address'),
                                          xscrollcommand = scroll_x.set,
                                          yscrollcommand = scroll_y.set)
        self.student_table.place(x = 1, y= 1, width = 1115.4, height = 586)
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_x.config(command = self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table['show'] = 'headings'
        self.student_table.heading('id', text = 'id')
        self.student_table.heading('name', text = 'name')
        self.student_table.heading('email', text = 'email')
        self.student_table.heading('phone', text = 'phone')
        self.student_table.heading('qualifications', text = 'qualifications')
        self.student_table.heading('gender', text = 'gender')
        self.student_table.heading('address', text = 'address')


        self.student_table.column('id', width = 17)
        self.student_table.column('name', width = 100)
        self.student_table.column('email', width = 70)
        self.student_table.column('phone', width = 65)
        self.student_table.column('qualifications', width = 65)
        self.student_table.column('gender', width = 30)
        self.student_table.column('address', width = 125)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

        #-------- CON + ADD -------
        self.fetch_all()
    def add_student(self):
        con =pymysql.connect(host = 'localhost',user = 'root',password= '',database = 'stud', port = 3308)
        cur = con.cursor()
        cur.execute("insert into student values (%s, %s, %s, %s, %s, %s, %s)", (
                                                                self.id_var.get(),
                                                                self.name_var.get(),
                                                                self.email_var.get(),
                                                                self.phone_var.get(),
                                                                self.qual_var.get(),
                                                                self.gender_var.get(),
                                                                self.address_var.get()



        ))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()
    def fetch_all(self):
        con = pymysql.connect(host = 'localhost', user= 'root', password= '', database= 'stud', port= 3308)
        cur = con.cursor()
        cur.execute('select * from student')
        rows = cur.fetchall()

        if len (rows) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END, value = row)
            con.commit()
        con.close()
    def delete(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='stud', port=3308)
        cur = con.cursor()
        cur.execute('delete from student where name=%s', self.del_var.get())
        con.commit()
        self.fetch_all()
        con.close()
    def clear(self):
        self.id_var.set('')
        self.name_var.set('')
        self.email_var.set('')
        self.phone_var.set('')
        self.qual_var.set('')
        self.gender_var.set('')
        self.address_var.set('')
    def get_cursor(self,ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.phone_var.set(row[3])
        self.qual_var.set(row[4])
        self.gender_var.set(row[5])
        self.address_var.set(row[6])
    def update(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='stud', port=3308)
        cur = con.cursor()
        cur.execute("update student set name=%s, email=%s, phone=%s,qual=%s, gender=%s, address=%s where id=%s", (

            self.name_var.get(),
            self.email_var.get(),
            self.phone_var.get(),
            self.qual_var.get(),
            self.gender_var.get(),
            self.address_var.get(),
            self.id_var.get()

        ))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()
    def search(self):
        con = pymysql.connect(host = 'localhost', user= 'root', password= '', database= 'stud', port= 3308)
        cur = con.cursor()
        cur.execute("select * from student where " +
                    str(self.se_by.get()) + " LIKE '%" + str(self.se_var.get()) + "%'")

        rows = cur.fetchall()

        if len (rows) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END, value = row)
            con.commit()
        con.close()
    def about(self):
        messagebox.showinfo("Developer Mahmoud Yasser", "Welcome to my simple school Management system project version 1.1")


















root = Tk()
ob = Student(root)
root.mainloop()