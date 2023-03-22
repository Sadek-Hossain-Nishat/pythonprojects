from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import mysql.connector

import random
from tkinter import messagebox





class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1295x550+230+220')
        # ==============Variables=========================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
        self.var_cust_name=StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()
        self.raw_string_contact=[]
        #================title==========================
        lbl_title = Label(self.root, text='ADD CUSTOMER DETAILS',
                          font=('times new roman', 18, 'bold'),
                          bg='black', fg='gold', bd=4,
                          relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)
        # ===========logo image===========
        img2 = Image.open('.\hotel_images\logohotel.png')
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimage2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)
        #==============label frame======================
        labelframeleft=LabelFrame(self.root,
                                  bd=2,relief=RIDGE,
                                  text='Customer Details',
                                  padx=2,
                                  font=('times new roman', 12, 'bold'))
        labelframeleft.place(x=0,y=50,width=425,
                             height=490)
        #================labels and entries=======================
        #====CustRef
        label_cust_ref=Label(labelframeleft,
                             text='Customer Ref',
                             font=('arial', 12, 'bold'),
                             padx=2,pady=6)
        label_cust_ref.grid(row=0,column=0,
                             sticky=W)

        enty_ref=ttk.Entry(labelframeleft,
        textvariable=self.var_ref,width=29,
                       font=('arial', 13, 'bold'),
                           state='readonly')
        enty_ref.grid(row=0,column=1)

        # ================cust name=======================
        cname = Label(labelframeleft, text='Customer Name',
                               font=('arial', 12, 'bold'),
                               padx=2, pady=6)
        cname.grid(row=1, column=0,
                            sticky=W)

        txtcname = ttk.Entry(labelframeleft, width=29,
                             textvariable=self.var_cust_name,
                             font=('arial', 13, 'bold'))
        txtcname.grid(row=1, column=1)

        # ================mother name=======================
        labelmname = Label(labelframeleft, text='Mother Name',
                               font=('arial', 12, 'bold'),

                               padx=2, pady=6)
        labelmname.grid(row=2, column=0,
                            sticky=W)

        txtmname = ttk.Entry(labelframeleft, width=29,
                             font=('arial', 13, 'bold'),
                             textvariable=self.var_mother)
        txtmname.grid(row=2, column=1)
        # ================gender combobox=======================
        label_gender = Label(labelframeleft, text='Gender',
                               font=('arial', 12, 'bold'),
                               padx=2, pady=6)
        label_gender.grid(row=3, column=0,
                            sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,
                                  font=('arial', 12, 'bold'),
                                  width=27,
                                  state='readonly'
                                  ,textvariable=self.var_gender)
        combo_gender['value']=('Male',
                               'Female',
                               'Other')
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        #=============postcode====================
        lblPostCode = Label(labelframeleft, text='PostCode',
                             font=('arial', 12, 'bold'),
                             padx=2, pady=6)
        lblPostCode.grid(row=4, column=0,
                          sticky=W)
        txtPostCode = ttk.Entry(labelframeleft, width=29,
                             font=('arial', 13, 'bold'),
                                textvariable=self.var_post)
        txtPostCode.grid(row=4, column=1)

        # =============mobile number====================
        lblMobileNumber = Label(labelframeleft, text='Mobile',
                            font=('arial', 12, 'bold'),
                            padx=2, pady=6)
        lblMobileNumber.grid(row=5, column=0,
                         sticky=W)
        txtMobileNumber = ttk.Entry(labelframeleft, width=29,
                                font=('arial', 13, 'bold'),
                                    textvariable=self.var_mobile)
        txtMobileNumber.grid(row=5, column=1)

        # =============email====================
        lblEmail = Label(labelframeleft, text='Email',
                            font=('arial', 12, 'bold'),
                            padx=2, pady=6)
        lblEmail.grid(row=6, column=0,
                         sticky=W)
        txtEmail = ttk.Entry(labelframeleft, width=29,
                                font=('arial', 13, 'bold'),
                             textvariable=self.var_email)
        txtEmail.grid(row=6, column=1)

        # =============nationality====================
        lblNationality = Label(labelframeleft, text='Nationality',
                         font=('arial', 12, 'bold'),
                         padx=2, pady=6)
        lblNationality.grid(row=7, column=0,
                      sticky=W)


        combo_nationality = ttk.Combobox(labelframeleft,
                                    font=('arial', 12, 'bold'),
                                    width=27,
                                    state='readonly'
                                    ,textvariable=self.var_nationality)
        combo_nationality['value'] = ('Indian',
                                 'American',
                                 'British',
                                      'Bangladeshi',
                                      'Pakistan')
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)

        #===============idprooftype combobox============

        lblidproof = Label(labelframeleft, text='Id Poof Type',
                         font=('arial', 12, 'bold'),
                         padx=2, pady=6)
        lblidproof.grid(row=8, column=0,
                      sticky=W)
        combo_id = ttk.Combobox(labelframeleft,
                                         font=('arial', 12, 'bold'),
                                         width=27,
                                         state='readonly',
                                         textvariable=self.var_id_proof)
        combo_id['value'] = ('AdharCard',
                                      'DrivingLicence',
                                      'Passport')
        combo_id.current(0)
        combo_id.grid(row=8, column=1)

        # ===============id Number============

        lblIdNumber = Label(labelframeleft, text='Id Number',
                           font=('arial', 12, 'bold'),
                           padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0,
                        sticky=W)
        txtIdNumber = ttk.Entry(labelframeleft, width=29,
                             font=('arial', 13, 'bold'),
                                textvariable=self.var_id_number)
        txtIdNumber.grid(row=9, column=1)

        # ===============Address============

        lblAddress = Label(labelframeleft, text='Address',
                            font=('arial', 12, 'bold'),
                            padx=2, pady=6)
        lblAddress.grid(row=10, column=0,
                         sticky=W)
        txtAddress = ttk.Entry(labelframeleft, width=29,
                                font=('arial', 13, 'bold'),
                               textvariable=self.var_address)
        txtAddress.grid(row=10, column=1)

#         ====================btn========================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE,
                        )
        btn_frame.place(x=0,y=400,width=412,
                        height=40)
        btnAdd=Button(btn_frame, text='Add',
                      font=('arial', 12, 'bold'),
                      bg='black', fg='gold',
                      width=9,
                      command=self.add_data)
        btnAdd.grid(row=0, column=0,padx=1)

        btnUpdate = Button(btn_frame, text='Update',
                        font=('arial', 12, 'bold'),
                        bg='black', fg='gold',
                        width=9,
                           command=self.update)
        btnUpdate.grid(row=0, column=1, padx=1)


        btnDelete = Button(btn_frame, text='Delete',
                        font=('arial', 12, 'bold'),
                        bg='black', fg='gold',
                        width=9,
                           command=self.mDelete)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text='Reset',
                        font=('arial', 12, 'bold'),
                        bg='black', fg='gold',
                        width=9,
                          command=self.reset)
        btnReset.grid(row=0, column=3, padx=1)
# ===================Table Frame Search====================================
        table_frame = LabelFrame(self.root,
                                    bd=2, relief=RIDGE,
                                    text='View Details And Search System',
                                    padx=2,
                                    font=('times new roman', 12, 'bold'))
        table_frame.place(x=435, y=50, width=860,
                             height=490)
        lblSearchby = Label(table_frame, text='Search By',
                           font=('arial', 12, 'bold'),
                           bg='red',fg='white')
        lblSearchby.grid(row=0, column=0,
                        sticky=W,padx=2)

        self.search_var=StringVar()


        combo_search = ttk.Combobox(table_frame,
                                    textvariable=self.search_var,
                                font=('arial', 12, 'bold'),
                                width=24,
                                state='readonly'
                                )
        combo_search['value'] = ('Mobile',
                             'Ref')
        combo_search.current(0)
        combo_search.grid(row=0, column=1,padx=2)

        self.text_search=StringVar()
        txtSearch = ttk.Entry(table_frame, width=24,
                              textvariable=self.text_search,
                               font=('arial', 13, 'bold'))
        txtSearch.grid(row=0, column=2,padx=2)

        btnSearch = Button(table_frame, text='Search',
                           font=('arial', 12, 'bold'),
                           bg='black', fg='gold',
                           width=9,
                           command=self.search)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(table_frame, text='ShowAll',
                           font=('arial', 12, 'bold'),
                           bg='black', fg='gold',
                           width=9,
                            command=self.fetch_data)
        btnShowAll.grid(row=0, column=4, padx=1)

#  ===================       show data table===================
        details_table = LabelFrame(table_frame,
                                 bd=2, relief=RIDGE,

                                 )
        details_table.place(x=0, y=50, width=860,
                          height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table, columns=(
            "ref", "name", "mother", "gender", "post", "mobile",
            "email", "nationality", "idproof", "idnumber", "address"
        ),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading('ref',text='Refer No')
        self.Cust_Details_Table.heading('name', text='Name')
        self.Cust_Details_Table.heading('mother', text='Mother Name')
        self.Cust_Details_Table.heading('gender', text='Gender')
        self.Cust_Details_Table.heading('post', text='PostCode')
        self.Cust_Details_Table.heading('mobile', text='Mobile')
        self.Cust_Details_Table.heading('email', text='Email')
        self.Cust_Details_Table.heading('nationality', text='Nationality')
        self.Cust_Details_Table.heading('idproof', text='Id Proof')
        self.Cust_Details_Table.heading('idnumber', text='Id Number')
        self.Cust_Details_Table.heading('address', text='Address')
        self.Cust_Details_Table['show']='headings'

        self.Cust_Details_Table.column('ref',width=100)
        self.Cust_Details_Table.column('name', width=100)
        self.Cust_Details_Table.column('mother', width=100)
        self.Cust_Details_Table.column('gender', width=100)
        self.Cust_Details_Table.column('post', width=100)
        self.Cust_Details_Table.column('mobile', width=100)
        self.Cust_Details_Table.column('email', width=100)
        self.Cust_Details_Table.column('nationality', width=100)
        self.Cust_Details_Table.column('idproof', width=100)
        self.Cust_Details_Table.column('idnumber', width=100)
        self.Cust_Details_Table.column('address', width=100)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror('Error','All fields are required',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',
                                             username='root',
                                             password='1234',
                                             database='hotelmanagement')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values"
                                  "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get()



                ))

                my_cursor.execute('insert into room values (%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_ref.get(),
                    self.var_mobile.get(),
                    "",
                    "",
                    "",
                    "",
                    "",
                    ""
                ))
                conn.commit()
                self.fetch_data()
                conn.close()



                messagebox.showinfo('Success','Customer has been added',
                                    parent=self.root)
                self.reset()
            except Exception as e:
                messagebox.showwarning('Warning',
                                       f'Some thing Went Wrong{e}',
                                       parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(
            host='localhost',
            username='root',
            password='1234',
            database='hotelmanagement',
            port = 3333
        )
        my_cursor=conn.cursor()
        my_cursor.execute('select * from customer')
        rows=my_cursor.fetchall()
        # if len(rows)!=0:
        self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
        for i in  rows:
            # self.Cust_Details_Table.insert("",END,values=i)
            self.Cust_Details_Table.insert("",END, values=i)
            print(i)
            print(i[5])
            self.raw_string_contact.append(i[5])

            print(self.raw_string_contact)
        conn.commit()
        conn.close()

    def get_cursor(self,events=''):
        cursor_row=self.Cust_Details_Table.focus()

        content=self.Cust_Details_Table.item(cursor_row)
        row=content['values']


        print([self.Cust_Details_Table.item(x) for x in self.Cust_Details_Table.selection()])
        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])



        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.mydb = mysql.connector.connect(
            host="localhost",
            username="root",
            password="1234",
            database='hotelmanagement'
        )
        self.connmobile = self.mydb.cursor()
        self.connmobile.execute('select mobile from customer where ref='+self.var_ref.get())
        rowmobile = self.connmobile.fetchone()

        self.var_mobile.set(rowmobile[0])

        print(rowmobile)


        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get()=='':
            messagebox.showerror('Error',
                                 'Please Enter Mobile Number',
                                 parent=self.root)
        else:
            conn = mysql.connector.connect(
                host='localhost',
                username='root',
                password='1234',
                database='hotelmanagement'
            )
            my_cursor = conn.cursor()
            my_cursor.execute('update customer set name=%s,mother=%s,gender=%s,post=%s,mobile=%s,email=%s,nationality=%s,'
                              'idproof=%s,idnumber=%s,address=%s where ref=%s',
                              (self.var_cust_name.get(),
                                self.var_mother.get(),
                                self.var_gender.get(),
                                self.var_post.get(),
                                self.var_mobile.get(),
                                self.var_email.get(),
                                self.var_nationality.get(),
                                self.var_id_proof.get(),
                                self.var_id_number.get(),
                                self.var_address.get(),
                                # for updating ref number must be placed in last side
                                self.var_ref.get()
                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Update',
                                'Customer details has been updated successfully',parent=self.root)


    def mDelete(self):

        mDelete=messagebox.askyesno('Hotel Management System',
                                    'Do you want to delete this customer',
                                    parent=self.root)

        if mDelete>0:
            conn = mysql.connector.connect(
                host='localhost',
                username='root',
                password='1234',
                database='hotelmanagement'
            )
            my_cursor = conn.cursor()
            query="delete from customer where ref=%s"
            query2 = "delete from room where id=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
            my_cursor.execute(query2, value)

            conn.commit()
            conn.close()
        else:
            if not mDelete:
                return

        self.fetch_data()


    def reset(self):
        # self.var_ref.set('')
        self.var_cust_name.set('')
        self.var_mother.set('')
        # self.var_gender.set('')
        self.var_post.set('')
        self.var_mobile.set('')
        self.var_email.set('')
        # self.var_nationality.set('')
        # self.var_id_proof.set('')
        self.var_id_number.set('')
        self.var_address.set('')

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(
            host='localhost',
            username='root',
            password='1234',
            database='hotelmanagement'
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer where "
                          +str(self.search_var.get())+" LIKE '%"+
                          str(self.text_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


if __name__ == '__main__':
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()