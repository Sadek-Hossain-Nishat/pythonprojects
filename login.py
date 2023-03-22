from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from hotel import HotelManagementSystem


def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title('Login')
        self.root.geometry('1550x800+0+0')

        # variables
        self.var_email = StringVar()
        self.var_password = StringVar()

        img = Image.open('.\seabeachimage.png')
        img = img.resize((1550, 800), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(img)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        frame =Frame(self.root,bg='black')
        frame.place(x=610,y=170,width=340,height=450)

        img1 = Image.open('user.png')
        img1 = img1.resize((100,80),Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1,bg='black',borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text='Get Started',font=('times new roman',20,'bold'),fg='white',bg='black')
        get_str.place(x=95,y=100)

#       label
        username = Label(frame,text= 'Username', font=('times new roman',15,'bold'),fg='white',bg='black')
        username.place(x=70,y=155)
        self.txtuser = ttk.Entry(frame,font=('times new roman',15,'bold'),
                                 textvariable=self.var_email)
        self.txtuser.place(x=40,y=180,width=270)

        password = Label(frame, text='Password', font=('times new roman', 15, 'bold'), fg='white', bg='black')
        password.place(x=70, y=225)
        self.txtpass = ttk.Entry(frame, font=('times new roman', 15, 'bold'),
                                 textvariable=self.var_password,show='*')
        self.txtpass.place(x=40, y=250, width=270)

#         icon images
        img2 = Image.open('user.png')
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage2, bg='black', borderwidth=0)
        lblimg1.place(x=650, y=323, width=25, height=25)

        img3 = Image.open('lockimage.png')
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimage3, bg='black', borderwidth=0)
        lblimg1.place(x=650, y=395, width=25, height=25)

        # login button

        loginbtn = Button(frame,text= 'Login',
                          font=('times new roman',15,'bold'),
                          bd=3,
                          relief=RIDGE,
                          fg='white',
                          bg='green',
                          command=self.login,
                          activeforeground='white',
                          activebackground='green')
        loginbtn.place(x=110,y=300,
                       width=120,
                       height=35)

#         register button

        registerbtn = Button(frame,text= 'New User Register',
                          font=('times new roman',10,'bold'),
                          bd=3,
                          relief=RIDGE,
                             command=self.register_window,
                          fg='white',
                          bg='black',
                          activeforeground='white',
                          activebackground='black',
                             borderwidth=0)
        registerbtn.place(x=15,y=350,width=160)

#         forget password
        forgetpassword = Button(frame, text='Forget Password',
                          font=('times new roman', 10, 'bold'),
                          bd=3,
                          relief=RIDGE,
                          fg='white',
                          bg='black',
                          activeforeground='white',
                          activebackground='black',
                          borderwidth=0,
                                command=self.forgot_password_window)
        forgetpassword.place(x=10, y=370,
                       width=160)
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get()=='' or self.txtpass.get()=='':
            messagebox.showerror('error',
                                 'all fields required')
        elif self.txtuser.get()=='kapu' and self.txtpass.get()=='ashu':
            messagebox.showinfo("Success","Welcome to codewithkiran channel please subscribe my channel ")
        else:
            connect = mysql.connector.connect(
                host='localhost',
                username='root',
                password='1234',
                database='hotelmanagement',
                port =3333
            )
            my_cursor = connect.cursor()

            my_cursor.execute('select * from register where'
                              ' email=%s and password=%s',(
                self.var_email.get(),
                self.var_password.get()


            ))
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror('Error',
                                     'Invalid username & password')

            else:
                open_main = messagebox.askyesno('YesNO',
                                                'Access only admin')
                if open_main>0:
                    self.new_window = Toplevel(self.root)
                    self.app =HotelManagementSystem(self.new_window)
                    # self.app =Hospital(self.new_window)


                else:
                    if not open_main:
                        return
            connect.commit()
            connect.close()

    #         =============== reset passward =======================
    def reset_password(self):
        if self.combo_security_Q.get()=='Select':
            messagebox.showerror('Error','Select the security question',
                                    parent=self.root2)
        elif self.txt_security.get()=='':
            messagebox.showerror('Error','Please enter the answer',
                                    parent=self.root2)
        elif self.txt_newpass.get()=='':
            messagebox.showerror('Error','Enter the new password',
                                    parent=self.root2)

        else:
            connect = mysql.connector.connect(
                host='localhost',
                username='root',
                password='1234',
                database='hotelmanagement',
                port =3333
            )
            my_cursor = connect.cursor()
            query = ('select * from register where email=%s and securityQ=%s and securityA=%s')
            value = (self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Please enter correct answer')
            else:
                query = ('update register set password=%s where email=%s')
                value = (self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                connect.commit()
                connect.close()
                messagebox.showinfo('Info',
                                    'Your password has been reset ,please login new password',
                                    parent=self.root2)

                self.root2.destroy()









    #         ============================ forget passward window======================================

    def forgot_password_window(self):
        if self.txtuser.get()=='':
            messagebox.showerror(
                "Error",
                "Please enter the Email address to reset password"
            )
        else:
            connect = mysql.connector.connect(
                host='localhost',
                username='root',
                password='1234',
                database='hotelmanagement',
                port =3333
            )
            my_cursor = connect.cursor()
            query = ('select * from register where email=%s')
            value = (self.txtuser.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror(
                    "My Error",
                    "Please enter the valid user name"
                )
            else:
                connect.close()
                self.root2 = Toplevel()
                self.root2.title('Forget Password')
                self.root2.geometry('340x450+610+170')

                l = Label(self.root2,text='Forget Password',
                          font=(
                              'times new roman',
                              20,
                              'bold'
                          ),
                          bg='black',
                          fg='white')

                l.place(x=0,y=10,relwidth=1)

                security_Q = Label(self.root2, text='Select Security Quotions',
                                   font=('times new roman', 15, 'bold'),
                                   bg='white',
                                   fg='black'
                                   )
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2,
                                                     font=('times new roman', 15, 'bold'),
                                                     state='readonly',
                                                     )
                self.combo_security_Q['values'] = (
                    'Select',
                    'Your Birth Place',
                    'Your Girlfriend name',
                    'Your Pet Name'
                )
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)
                security_A = Label(self.root2,
                                   text='Security Answer',
                                   font=('times new roman', 15, 'bold'),
                                   bg='white',
                                   fg='black'
                                   )

                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=('times new roman', 15),
                                              )
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2,
                                   text='New Password',
                                   font=('times new roman', 15, 'bold'),
                                   bg='white',
                                   fg='black'
                                   )

                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2, font=('times new roman', 15),
                                              )
                self.txt_newpass.place(x=50, y=250, width=250)

                btn = Button(self.root2,
                             text = 'Reset',
                             font=(
                                 'times new roman',
                                 15,
                                 'bold'
                             ),
                             fg='white',
                             bg='green',
                             command=self.reset_password)
                btn.place(x=100,y=290)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title('Register')
        self.root.geometry('1600x900+0+0')


        # ===========variables =================
        self.var_fname = StringVar(
        )
        self.var_lname = StringVar(
        )
        self.var_contact = StringVar(
        )
        self.var_email = StringVar(
        )
        self.var_securityQ = StringVar(
        )
        self.var_securityA = StringVar(
        )
        self.var_pass = StringVar(
        )
        self.var_confpass = StringVar(
        )


        # ================bg image ====================

        img = Image.open('seatleweatherimage.jpg')
        img = img.resize((1600, 900), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(img)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # self.bg = ImageTk.PhotoImage(
        #     file=r'H:/python file/Turtle projects/Turtle games/python projects/Hotel Management Software/loginformdirectory/download.jpg')
        # bg_lbl = Label(self.root, image=self.bg)
        # bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)


#         ==============left image ============================

        img2 = Image.open('futureimage.jpg')
        img2 = img2.resize((470, 550), Image.ANTIALIAS)
        self.bg1 = ImageTk.PhotoImage(img2)
        lbl_bg2 = Label(self.root, image=self.bg1)
        lbl_bg2.place(x=50, y=100,width=470, height=550)

        # ==========main frame =============
        frame = Frame(self.root,
                      bg='white')
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl = Label(frame,text='REGISTER HERE',
                             font=(
                                 'times new roman',
                                 20,
                                 'bold'
                             ),
                             fg='green',
                             bg='white')

        register_lbl.place(x=20,y=20)

#         ===================label and entries = =====================

        # ===============row1===============================
        fname = Label(frame,text='First Name',
                             font=(
                                 'times new roman',
                                 15,
                                 'bold'
                             ),

                             bg='white')

        fname.place(x=50,y=100)

        self.fname_entry = ttk.Entry(frame,

                                font=(
                                    'times new roman',
                                    15,
                                    'bold'
                                ),
                                     textvariable=self.var_fname
                                )
        self.fname_entry.place(x=50,y=130,width=250)

        l_name = Label(frame,text= ' Last Name',
                       font=('times new roman',15,'bold'),
                       bg = 'white',fg='black')
        l_name.place(x=370,y=100)

        self.txt_lname = ttk.Entry(frame,font=('times new roman',15),
                                   textvariable=self.var_lname)
        self.txt_lname.place(x=370,y=130,width=250)

#         ===============row2===========================
        contact = Label(frame,text='Contact No',
                        font=('times new roman',15,'bold'),
                        bg='white',fg='black')
        contact.place(x=50,y=170)

        self.txt_contact = ttk.Entry(frame,font=('times new roman',15),
                                     textvariable=self.var_contact)
        self.txt_contact.place(x=50,y=200,width=250)

        email = Label(frame,text='Email',
                      font=('times new roman',15,'bold'),
                      bg='white',
                      fg='black'
                      )
        email.place(x=370,y=170)

        self.txt_email = ttk.Entry(frame, font=('times new roman', 15),
                                   textvariable=self.var_email)
        self.txt_email.place(x=370, y=200, width=250)

#         ===============row3==================================

        security_Q = Label(frame, text='Select Security Quotions',
                           font=('times new roman', 15, 'bold'),
                           bg='white',
                           fg='black'
                           )
        security_Q.place(x=50,y=240)

        self.combo_security_Q = ttk.Combobox(frame,
                                             font=('times new roman', 15, 'bold'),
                                             state='readonly',
                                             textvariable=self.var_securityQ)
        self.combo_security_Q['values'] = (
            'Select',
            'Your Birth Place',
            'Your Girlfriend name',
            'Your Pet Name'
        )
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        security_A = Label(frame,
                           text='Security Answer',
                           font=('times new roman', 15, 'bold'),
                           bg='white',
                           fg='black'
                           )

        security_A.place(x=370,y=240)

        self.txt_security = ttk.Entry(frame, font=('times new roman', 15),
                                      textvariable=self.var_securityA)
        self.txt_security.place(x=370, y=270, width=250)
#         ==============ROW4===================
        pswd = Label(frame,text='Password',
                     font=('times new roman', 15,'bold'),
                     bg='white',
                     fg='black')
        pswd.place(x=50,y=310)

        self.txt_pswd = ttk.Entry(frame,font=('times new roman', 15),
                                  textvariable=self.var_pass)
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd = Label(frame,
                             text='Confirm Password',
                             font=('times new roman', 15,'bold'),
                             bg='white',
                             fg='black'
                             )

        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd = ttk.Entry(frame,font=('times new roman', 15),
                                          textvariable=self.var_confpass)
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

#         ================================check button ======================
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame,text='I Agree the Terms & Conditions',
                               font=('times new roman', 12,'bold'),
                               onvalue=1,
                               offvalue=0,
                               variable=self.var_check
                               )
        checkbtn.place(x= 50,y=380)

#         =================buttons========================
        img = Image.open('registerlogo.png')
        img = img.resize((200,50),Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1= Button(frame,image=self.photoimage, borderwidth=0,
                   command=self.register_date,
                   cursor='hand2')
        b1.place(x=10,y=420,width=300)

        img1 = Image.open('loginlogo.png')
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, borderwidth=0,
                    cursor='hand2',command=self.return_login)
        b1.place(x=330, y=420, width=300)


#         ===========function declaration========================


    def register_date(self):
        if self.var_fname.get()=='' or self.var_email.get()=='' or self.var_securityQ.get()=='select':
            messagebox.showerror('Error','All fields are required')
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror('Error','password & confirm password must be same')
        elif self.var_check.get()==0:
            messagebox.showerror('Error','Please agree our terms and conditions')
        else:
            connect = mysql.connector.connect(
                host='localhost',
                username='root',
                password='1234',
                database='hotelmanagement',
                port =3333
            )
            my_cursor = connect.cursor()
            query = ("select  * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Alreadey Exists,\nPlease try"
                                             "another email")
            else:
                my_cursor.execute("insert into register values (%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
                connect.commit()
                connect.close()
                messagebox.showinfo('Success','Register Successfully')

    def return_login(self):
        self.root.destroy()










class Hospital:
    def __init__(self, root):

        self.root = root
        self.root.title('+Hospital Management System')
        self.root.geometry('1540x800+0+0')

        self.Nameoftablets = StringVar()
        self.NumberofTablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.Number = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedicine = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatinetName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()

        lbltitle = Label(self.root,
                         bd=20, relief=RIDGE,
                         text="HOSPITAL MANAGEMENT SYSTEM",
                         fg='red',
                         bg='white',
                         font=('times new roman',
                               50,
                               'bold'))
        lbltitle.pack(side=TOP, fill=X)

        #        ==============first data frame================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE,
                          )
        Dataframe.place(x=0, y=130,
                        width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe,
                                   bd=10, relief=RIDGE,
                                   padx=20,
                                   font=('times new roman', 12, 'bold'),
                                   text='Patient Information')
        DataframeLeft.place(x=0, y=5, width=980,
                            height=350)

        DataframeRight = LabelFrame(Dataframe,
                                    bd=10, relief=RIDGE,
                                    padx=20,
                                    font=('times new roman', 12, 'bold'),
                                    text='Prescription')
        DataframeRight.place(x=990, y=5, width=460,
                             height=350)

        #         ===================buttons frame=============================

        Buttonframe = Frame(self.root, bd=20, relief=RIDGE,
                            )
        Buttonframe.place(x=0, y=530,
                          width=1530, height=70)

        #         ===================details frame=============================

        Detailsframe = Frame(self.root, bd=20, relief=RIDGE,
                             )
        Detailsframe.place(x=0, y=600,
                           width=1530, height=190)

        #         =======================dataframe left ===================
        lblNameTablet = Label(DataframeLeft, text="Names of Tablet",
                              font=('times new roman', 12, 'bold'),
                              padx=2,
                              pady=6
                              )
        lblNameTablet.grid(row=0, column=0)

        comNametablet = ttk.Combobox(DataframeLeft,
                                     font=('times new roman', 12, 'bold'),
                                     width=33,
                                     textvariable=self.Nameoftablets
                                     )

        comNametablet['values'] = (
            'Nice',
            'Corona Vaccine',
            'Napa Extra',
            'Nightfresh',
            'Sinafresh',
            'Omiprajol'
        )

        comNametablet.current(0)

        comNametablet.grid(row=0, column=1)

        lblref = Label(DataframeLeft,
                       font=('times new roman', 12, 'bold'),
                       text='Reference No',
                       padx=2
                       )

        lblref.grid(row=1, column=0, sticky=W)

        textref = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.ref,

            width=35
        )
        textref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft,
                        font=('times new roman', 12, 'bold'),
                        text='Dose',
                        padx=2
                        )

        lblDose.grid(row=2, column=0, sticky=W)

        textDose = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.Dose,

            width=35
        )
        textDose.grid(row=2, column=1)

        lblNoOfTablets = Label(DataframeLeft,
                               font=('times new roman', 12, 'bold'),
                               text='No Of Tablets',
                               padx=2
                               )

        lblNoOfTablets.grid(row=3, column=0, sticky=W)

        textNoOfTablets = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.NumberofTablets,

            width=35
        )
        textNoOfTablets.grid(row=3, column=1)

        lblLot = Label(DataframeLeft,
                       font=('times new roman', 12, 'bold'),
                       text='Lot:', padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)

        textLot = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.Lot,

            width=35
        )
        textLot.grid(row=4, column=1)

        lblissueDate = Label(DataframeLeft,
                             font=('times new roman', 12, 'bold'),
                             text='Issue Date:', padx=2, pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)

        textissueDate = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.Issuedate,

            width=35
        )
        textissueDate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft,
                           font=('times new roman', 12, 'bold'),
                           text='Exp Date:', padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)

        textExpDate = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.ExpDate,

            width=35
        )
        textExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataframeLeft,
                             font=('times new roman', 12, 'bold'),
                             text='Daily Dose:', padx=2, pady=6
                             )
        lblDailyDose.grid(row=7, column=0, sticky=W)

        textDailyDose = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),

            width=35,
            textvariable=self.DailyDose
        )
        textDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(DataframeLeft,
                              font=('times new roman', 12, 'bold'),
                              text='Side Effect:', padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)

        textSideEffect = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),

            width=35,
            textvariable=self.sideEffect
        )
        textSideEffect.grid(row=8, column=1)

        lblFurtherinfo = Label(DataframeLeft,
                               font=('times new roman', 12, 'bold'),
                               text='Further Information', padx=2, pady=6)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)

        textFurtherinfo = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),

            width=35,
            textvariable=self.FurtherInformation
        )
        textFurtherinfo.grid(row=0, column=3)

        lblDrivingMachine = Label(DataframeLeft,
                                  font=('times new roman', 12, 'bold'),
                                  text='Blood Pressure', padx=2, pady=6)
        lblDrivingMachine.grid(row=1, column=2, sticky=W)

        textDrivingMachine = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),

            textvariable=self.DrivingUsingMachine,

            width=35
        )
        textDrivingMachine.grid(row=1, column=3)

        lblStorage = Label(DataframeLeft,
                           font=('times new roman', 12, 'bold'),
                           text='Storage Advice', padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)

        textStorage = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.StorageAdvice,

            width=35
        )
        textStorage.grid(row=2, column=3)

        lblMedicine = Label(DataframeLeft,
                            font=('times new roman', 12, 'bold'),
                            text='Medication', padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)

        textMedicine = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),


            width=35
        )
        textMedicine.grid(row=3, column=3
                          , sticky=W)

        lblPatientId = Label(DataframeLeft,
                             font=('times new roman', 12, 'bold'),
                             text='Patient Id', padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)

        textPatientId = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),

            width=35
        )
        textPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(DataframeLeft,
                             font=('times new roman', 12, 'bold'),
                             text='NHS Number', padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)

        textNhsNumber = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.nhsNumber
            ,

            width=35
        )
        textNhsNumber.grid(row=5, column=3)

        lblPatientname = Label(DataframeLeft,
                               font=('times new roman', 12, 'bold'),
                               text='Patient Name', padx=2, pady=6)
        lblPatientname.grid(row=6, column=2, sticky=W)

        textPatientname = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.PatinetName,

            width=35
        )
        textPatientname.grid(row=6, column=3)

        lblDateOfBirth = Label(DataframeLeft,
                               font=('times new roman', 12, 'bold'),
                               text='Date Of Birth', padx=2, pady=6)
        lblDateOfBirth.grid(row=7, column=2, sticky=W)

        textDateOfBirth = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.DateOfBirth,

            width=35
        )
        textDateOfBirth.grid(row=7, column=3)

        lblPatientAddress = Label(DataframeLeft,
                                  font=('times new roman', 12, 'bold'),
                                  text='Patient Address', padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)

        textPatientAddress = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.PatientAddress,

            width=35
        )
        textPatientAddress.grid(row=8, column=3)

        #         =====================DATAFRAME RIGHT============================
        self.txtPrescription = Text(DataframeRight,
                                    font=('times new roman', 13, 'bold'),
                                    width=45,
                                    height=16,
                                    padx=2,
                                    pady=6
                                    )

        self.txtPrescription.grid(row=0, column=0)

        #          ==============================================buttons=====================
        btnPrescription = Button(Buttonframe,
                                 text='Prescription',
                                 bg='green',
                                 fg='white',
                                 font=('times new roman', 12, 'bold'),
                                 width=23,
                                 # height=10,
                                 padx=2,
                                 pady=6,
                                 command=self.iPrectioption

                                 )
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe,
                                     text='Prescription Data',
                                     bg='green',
                                     fg='white',
                                     font=('times new roman', 12, 'bold'),
                                     width=23,
                                     # height=10,
                                     padx=2,
                                     pady=6,
                                     command=self.iPrescriptionData

                                     )
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe,
                           text='Update',
                           bg='green',
                           fg='white',
                           font=('times new roman', 12, 'bold'),
                           width=23,
                           # height=10,
                           padx=2,
                           pady=6,

                           command=self.update_data

                           )
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe,
                           text='Delete',
                           bg='green',
                           fg='white',
                           font=('times new roman', 12, 'bold'),
                           width=23,
                           # height=10,
                           padx=2,
                           pady=6,

                           command=self.idelete

                           )
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe,
                          text='Clear',
                          command=self.clear,
                          bg='green',
                          fg='white',
                          font=('times new roman', 12, 'bold'),
                          width=23,
                          # height=10,
                          padx=2,
                          pady=6,

                          )
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe,
                         text='Exit',
                         bg='green',
                         fg='white',
                         font=('times new roman', 12, 'bold'),
                         width=23,
                         # height=10,
                         padx=2,
                         pady=6,
                         command=self.iExit

                         )
        btnExit.grid(row=0, column=5)

        #         ====================table ========================

        #         =================scrollbar ============================

        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(Detailsframe,
                                           columns=(
                                               "nameoftable",
                                               "ref",
                                               "dose",
                                               "nooftablets",
                                               "lot",
                                               "issuedate",
                                               "expdate",
                                               "dailydose",
                                               "storage",
                                               "nhsnumber",
                                               "pname",
                                               "dob",
                                               "address"
                                           ),
                                           xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable", text='Name of Table')
        self.hospital_table.heading("ref", text='Reference No.')
        self.hospital_table.heading("dose", text='Dose')
        self.hospital_table.heading("nooftablets", text='No of Tablets')
        self.hospital_table.heading("lot", text='Lot')
        self.hospital_table.heading("issuedate", text='Issue Date')
        self.hospital_table.heading("expdate", text='Exp Date')
        self.hospital_table.heading("dailydose", text='Daily Dose')
        self.hospital_table.heading("storage", text='Storage')
        self.hospital_table.heading("nhsnumber", text='NHS Number')
        self.hospital_table.heading("pname", text='Patient Name')
        self.hospital_table.heading('dob', text='DOB')
        self.hospital_table.heading('address', text='Address')

        self.hospital_table['show'] = 'headings'

        self.hospital_table.column("nameoftable", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)

        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_date()

    #         ============================functionality declaration==================

    def iPrescriptionData(self):
        if self.Nameoftablets.get() == '' or self.ref.get() == '':
            messagebox.showerror('Error', 'All fields are required')
        else:
            conn = mysql.connector.connect(
                host='localhost',
                username='root',
                password='1234',
                database='hospitalmanagement',
                port =3333
            )

            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.Nameoftablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.PatinetName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get()))
            conn.commit()
            self.fetch_date()
            conn.close()

            messagebox.showinfo("Success", "Record has been inserted")



    def update_data(self):

        conn = mysql.connector.connect(
            host='localhost',
            username='root',
            password='1234',
            database='hospitalmanagement',
            port =3333
        )

        my_cursor = conn.cursor()
        my_cursor.execute('update hospital set nameoftablets=%s,dose=%s,numberoftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,patientname=%s,dob=%s,patientaddress=%s where referenceno=%s',(
            self.Nameoftablets.get(),
            self.Dose.get(),
            self.NumberofTablets.get(),
            self.Lot.get(),
            self.Issuedate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.StorageAdvice.get(),
            self.nhsNumber.get(),
            self.PatinetName.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get(),
            self.ref.get()
        ))
        conn.commit()
        self.fetch_date()
        conn.close()

        messagebox.showinfo("Success", "Record has been updated")

    def fetch_date(self):
        conn = mysql.connector.connect(
            host='localhost',
            username='root',
            password='1234',
            database='hospitalmanagement',
            port=3333
        )

        my_cursor = conn.cursor()
        my_cursor.execute('select * from hospital')
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=''):
        cursor_row = self.hospital_table.focus()
        content =self.hospital_table.item(cursor_row)
        row = content['values']
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatinetName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])


    def iPrectioption(self):
        self.txtPrescription.insert(END,"Name of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t\t"+self.NumberofTablets.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.Issuedate.get()+"\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.sideEffect.get()+"\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"DrivingUsingMachine:\t\t\t"+self.DrivingUsingMachine.get()+"\n")
        self.txtPrescription.insert(END,"PatientId:\t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"NHSNumber:\t\t\t"+self.nhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t"+self.PatinetName.get()+"\n")
        self.txtPrescription.insert(END,"DateofBirth:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t\t"+self.PatientAddress.get()+"\n")




    def idelete(self):
        conn = mysql.connector.connect(
            host='localhost',
            username='root',
            password='1234',
            database='hospitalmanagement',
            port =3333
        )

        my_cursor = conn.cursor()

        query = 'delete from hospital where referenceno=%s'
        value = (self.ref.get(),)

        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_date()

        messagebox.showinfo("Success", "Record has been deleted")

    def clear(self):
        self.Nameoftablets.set('')
        self.ref.set('')
        self.Dose.set('')
        self.NumberofTablets.set('')
        self.Lot.set('')
        self.Issuedate.set('')
        self.ExpDate.set('')
        self.DailyDose.set('')
        self.sideEffect.set('')
        self.FurtherInformation.set('')
        self.StorageAdvice.set('')
        self.DrivingUsingMachine.set('')
        self.HowToUseMedicine.set('')
        self.PatientId.set('')
        self.nhsNumber.set('')
        self.PatinetName.set('')
        self.DateOfBirth.set('')
        self.PatientAddress.set('')
        self.txtPrescription.delete('1.0',END)

    def iExit(self):
        iexit = messagebox.askyesno(
            'Hospital management system',
            'Confirm you want to exit'
        )

        if iexit>0:
            self.root.destroy()
            return
























if __name__ == '__main__':
    main()













































