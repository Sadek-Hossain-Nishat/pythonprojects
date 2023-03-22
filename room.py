from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import mysql.connector
from time import strftime
from datetime import datetime
from tkinter import messagebox


class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title('Hotel Management System')
        self.root.geometry('1295x550+230+220')
        # ==================variables ============
        self.var_customerRef=StringVar()
        self.var_contact=StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()
        # ================title==========================
        lbl_title = Label(self.root, text='ROOMBOOKING DETAILS',
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
        # ==============label frame======================
        labelframeleft = LabelFrame(self.root,
                                    bd=2, relief=RIDGE,
                                    text='Roombooking Details',
                                    padx=2,
                                    font=('times new roman', 12, 'bold'))
        labelframeleft.place(x=0, y=50, width=425,
                             height=490)
        # ================labels and entries=======================
        # =============== customer id ==============

        label_cust_contact = Label(labelframeleft,
                                   text='Customer Ref',
                                   font=('arial', 12, 'bold'),
                                   padx=2, pady=6)
        label_cust_contact.grid(row=0, column=0,
                                sticky=W)

        enty_contact = ttk.Entry(labelframeleft,
                                 width=20,
                                 font=('arial', 13, 'bold'),

                                 textvariable=self.var_customerRef)
        enty_contact.grid(row=0, column=1,
                          sticky=W)





        #  all necessary buttons

        # ====Customer contact
        label_cust_contact = Label(labelframeleft,
                                   text='Customer Contact',
                                   font=('arial', 12, 'bold'),
                                   padx=2, pady=6)
        label_cust_contact.grid(row=1, column=0,
                                sticky=W)

        enty_contact = ttk.Entry(labelframeleft,
                                 width=20,
                                 font=('arial', 13, 'bold'),

                                 textvariable=self.var_contact)
        enty_contact.grid(row=1, column=1,
                          sticky=W)

        # ================ fetch data button=======================
        btnFetchData = Button(labelframeleft, text='Fetch Data',
                              font=('arial', 8, 'bold'),
                              bg='black', fg='gold',
                              width=8,
                              command=self.fetch_contact)
        btnFetchData.place(x=347, y=4)

        # ================check in date=======================
        check_in_date = Label(labelframeleft, text='Check_in Date',
                              font=('arial', 12, 'bold'),
                              padx=2, pady=6)
        check_in_date.grid(row=2, column=0,
                           sticky=W)

        txtcheck_in_date = ttk.Entry(labelframeleft, width=29,

                                     font=('arial', 13, 'bold'),
                                     textvariable=self.var_checkin)
        txtcheck_in_date.grid(row=2, column=1)

        # ================check out date=======================
        check_out_date = Label(labelframeleft, text='Check_Out Date',
                               font=('arial', 12, 'bold'),
                               padx=2, pady=6,
                               )
        check_out_date.grid(row=3, column=0,
                            sticky=W)

        txt_check_out = ttk.Entry(labelframeleft, width=29,

                                  font=('arial', 13, 'bold'),
                                  textvariable=self.var_checkout)
        txt_check_out.grid(row=3, column=1)




        # ================Room Type=======================
        conn = mysql.connector.connect(
            host='localhost',
            username='root',
            password='1234',
            database='hotelmanagement',
            port =3333
        )
        my_cursor = conn.cursor()


        label_RoomType = Label(labelframeleft, text='Room Type',
                               font=('arial', 12, 'bold'),
                               padx=2, pady=6)
        label_RoomType.grid(row=4, column=0,
                            sticky=W)

        my_cursor.execute('select roomtype from details')
        ide = my_cursor.fetchall()

        combo_RoomType = ttk.Combobox(labelframeleft,
                                      font=('arial', 12, 'bold'),
                                      width=27,
                                      state='readonly'
                                      ,
                                      textvariable=self.var_roomtype)

        combo_RoomType['value'] = ide


        combo_RoomType.current(0)

        combo_RoomType.grid(row=4, column=1)

        # == #=============Available Room====================
        lblRoomAvailable = Label(labelframeleft, text='Available Room',
                                 font=('arial', 12, 'bold'),
                                 padx=2, pady=6)
        lblRoomAvailable.grid(row=5, column=0,
                              sticky=W)


        my_cursor.execute('select roomno from details')
        rows = my_cursor.fetchall()

        combo_RoomNo = ttk.Combobox(labelframeleft,
                                      font=('arial', 12, 'bold'),
                                      width=27,
                                      state='readonly'
                                      ,
                                      textvariable=self.var_roomavailable)

        combo_RoomNo['value'] =rows
        combo_RoomNo.current(0)

        combo_RoomNo.grid(row=5, column=1)
        # =============Meal====================
        lblMeal = Label(labelframeleft, text='Meal',
                        font=('arial', 12, 'bold'),
                        padx=2, pady=6)
        lblMeal.grid(row=6, column=0,
                     sticky=W)
        txtMeal = ttk.Entry(labelframeleft, width=29,
                            font=('arial', 13, 'bold'),
                            textvariable=self.var_meal )
        txtMeal.grid(row=6, column=1)

        # =============No of Days====================
        lblNoOfDays = Label(labelframeleft, text='No Of Days',
                            font=('arial', 12, 'bold'),
                            padx=2, pady=6)
        lblNoOfDays.grid(row=7, column=0,
                         sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft, width=29,
                                font=('arial', 13, 'bold'),
                                textvariable=self.var_noofdays)
        txtNoOfDays.grid(row=7, column=1)

        # =============Paid Tax====================
        lblNoOfDays = Label(labelframeleft, text='Paid Tax',
                            font=('arial', 12, 'bold'),
                            padx=2, pady=6)
        lblNoOfDays.grid(row=8, column=0,
                         sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft, width=29,
                                font=('arial', 13, 'bold'),
                                textvariable=self.var_paidtax)
        txtNoOfDays.grid(row=8, column=1)

        # =============Sub Total====================
        lblNoOfDays = Label(labelframeleft, text='Sub Total',
                            font=('arial', 12, 'bold'),
                            padx=2, pady=6)
        lblNoOfDays.grid(row=9, column=0,
                         sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft, width=29,
                                font=('arial', 13, 'bold'),
                                textvariable=self.var_actualtotal)
        txtNoOfDays.grid(row=9, column=1)

        # =============Total Cost====================
        lblNoOfDays = Label(labelframeleft, text='Total Cost',
                            font=('arial', 12, 'bold'),
                            padx=2, pady=6)
        lblNoOfDays.grid(row=10, column=0,
                         sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft, width=29,
                                font=('arial', 13, 'bold'),
                                textvariable=self.var_total)
        txtNoOfDays.grid(row=10, column=1)

        # ============btn bill======================


        #         ====================btn========================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE,
                          )
        btn_frame.place(x=0, y=410, width=412,
                        height=40)
        btnBill = Button(btn_frame, text='Bill',
                        font=('arial', 12, 'bold'),
                        bg='black', fg='gold',
                        width=9,
                         command=self.total

                        )
        btnBill.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text='Update',
                           font=('arial', 12, 'bold'),
                           bg='black', fg='gold',
                           width=9,
                           command=self.update
                           )
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text='Delete',
                           font=('arial', 12, 'bold'),
                           bg='black', fg='gold',
                           width=9,
                           command=self.mDelete
                           )
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text='Reset',
                          font=('arial', 12, 'bold'),
                          bg='black', fg='gold',
                          width=9,
                          command=self.reset
                          )
        btnReset.grid(row=0, column=3, padx=1)
        # ====================right side image===================
        img3 = Image.open('.\\hotel_images\\bed.jpg')
        img3 = img3.resize((520, 200), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg = Label(self.root, image=self.photoimage3, bd=0, relief=RIDGE)
        lblimg.place(x=760, y=55, width=520, height=200)

        # ===================Table Frame Search====================================
        table_frame = LabelFrame(self.root,
                                 bd=2, relief=RIDGE,
                                 text='View Details And Search System',
                                 padx=2,
                                 font=('times new roman', 12, 'bold'))
        table_frame.place(x=435, y=280, width=860,
                          height=260)
        lblSearchby = Label(table_frame, text='Search By',
                            font=('arial', 12, 'bold'),
                            bg='red', fg='white')
        lblSearchby.grid(row=0, column=0,
                         sticky=W, padx=2)

        self.search_var = StringVar()

        combo_search = ttk.Combobox(table_frame,
                                    textvariable=self.search_var,
                                    font=('arial', 12, 'bold'),
                                    width=24,
                                    state='readonly'
                                    )
        combo_search['value'] = ('Contact',
                                 'Room')
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.text_search = StringVar()
        txtSearch = ttk.Entry(table_frame, width=24,
                              textvariable=self.text_search,
                              font=('arial', 13, 'bold'))
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(table_frame, text='Search',
                           font=('arial', 12, 'bold'),
                           bg='black', fg='gold',
                           width=9,
                           command=self.search
                           )
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(table_frame, text='ShowAll',
                            font=('arial', 12, 'bold'),
                            bg='black', fg='gold',
                            width=9,
                            command=self.fetch_data
                            )
        btnShowAll.grid(row=0, column=4, padx=1)
        #  ===================       show data table===================
        details_table = LabelFrame(table_frame,
                                   bd=2, relief=RIDGE,

                                   )
        details_table.place(x=0, y=50, width=860,
                            height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, column=("id",
            "contact", "checkin", "checkout", "roomtype", "roomavailable", "meal",
            "noOfdays"
        ), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading('id', text='Ref No')
        self.room_table.heading('contact', text='Mobile')
        self.room_table.heading('checkin', text='Check-in')
        self.room_table.heading('checkout', text='Check-out')
        self.room_table.heading('roomtype', text='Room Type')
        self.room_table.heading('roomavailable', text='Room NO')
        self.room_table.heading('meal', text='Meal')
        self.room_table.heading('noOfdays', text='NoOfDays')

        self.room_table['show']='headings'

        self.room_table.column('id', width=100)
        self.room_table.column('contact', width=100)
        self.room_table.column('checkin', width=100)
        self.room_table.column('checkout', width=100)
        self.room_table.column('roomtype', width=100)
        self.room_table.column('roomavailable', width=100)
        self.room_table.column('meal', width=100)
        self.room_table.column('noOfdays', width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind('<ButtonRelease-1>', self.get_cursor)
        self.fetch_data()








    #             fetch data

    def fetch_data(self):
        conn = mysql.connector.connect(
            host='localhost',
            username='root',
            password='1234',
            database='hotelmanagement',
            port = 3333
        )
        my_cursor = conn.cursor()
        my_cursor.execute('select * from room')
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                # self.Cust_Details_Table.insert("",END,values=i)
                self.room_table.insert("", END, values=i)

            conn.commit()
        conn.close()
    # get cursor
    def get_cursor(self, events=''):
        cursor_row = self.room_table.focus()


        content = self.room_table.item(cursor_row)
        row = content['values']

        self.var_customerRef.set(row[0])

        self.mydb = mysql.connector.connect(
            host="localhost",
            username="root",
            password="1234",
            database='hotelmanagement',
            port =3333
        )
        self.connmobile = self.mydb.cursor()
        self.connmobile.execute('select contact from room where id=' + self.var_customerRef.get())
        rowmobile = self.connmobile.fetchone()

        self.var_contact.set(rowmobile[0])
        self.var_checkin.set(row[2])
        self.var_checkout.set(row[3])
        self.var_roomtype.set(row[4])
        self.var_roomavailable.set(row[5])
        self.var_meal.set(row[6])
        self.var_noofdays.set(row[7])











    # update
    def update(self):
        if self.var_contact.get() == '':
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
            my_cursor.execute(
                'update room set checkin=%s,checkout=%s,roomtype=%s,roomavailable=%s,meal=%s,noofdays=%s'
                ' where id=%s',
                (self.var_checkin.get(),
                 self.var_checkout.get(),
                 self.var_roomtype.get(),
                 self.var_roomavailable.get(),
                 self.var_meal.get(),
                 self.var_noofdays.get(),
                 self.var_customerRef.get()
                 ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Update',
                                'Room details has been updated successfully', parent=self.root)

    def mDelete(self):

        mDelete = messagebox.askyesno('Hotel Management System',
                                      'Do you want to delete this customer',
                                      parent=self.root)

        if mDelete > 0:
            conn = mysql.connector.connect(
                host='localhost',
                username='root',
                password='1234',
                database='hotelmanagement'
            )
            my_cursor = conn.cursor()
            query = "delete from room where id=%s"
            value = (self.var_customerRef.get(),)

            query2 = "delete from customer where ref=%s"




            my_cursor.execute(query, value)
            my_cursor.execute(query2, value)
            conn.commit()
            conn.close()
        else:
            if not mDelete:
                return

        self.fetch_data()


    def reset(self):
        # self.var_ref.set('')

        self.var_customerRef.set('')
        self.var_contact.set('')
        self.var_checkin.set('')
        self.var_checkout.set('')
        self.var_roomtype.set('')
        self.var_roomavailable.set('')
        self.var_meal.set('')
        self.var_noofdays.set('')
        self.var_paidtax.set('')
        self.var_actualtotal.set('')
        self.var_total.set('')




    #    =========all fetch data==========
    def fetch_contact(self):
        if self.var_contact.get()=='' and self.var_customerRef.get()=='':
            messagebox.showerror('Error','Please,enter Contact Number or id Number',
                                 parent=self.root)
        else:
            showDataFrame = Frame(self.root, bd=4, relief=RIDGE,
                                  padx=2,

                                  )

            showDataFrame.place(x=450, y=55,
                                width=300, height=180)

            mydb = mysql.connector.connect(
                host='localhost',
                username='root',
                password='1234',
                database='hotelmanagement',
                port =3333
            )

            mycursor = mydb.cursor()




            if self.var_contact.get()=="":
                value=(self.var_customerRef.get(),)
                mycursor.execute('select * from customer where ref=%s',
                                 value)
            elif self.var_customerRef.get()=="":
                value=(self.var_contact.get(),)
                mycursor.execute('select * from customer where mobile=%s',
                                 value)
            else:
                value=(self.var_contact.get(),)
                mycursor.execute('select * from customer where mobile=%s',
                                 value)




            rows = mycursor.fetchone()
            mydb.commit()
            mydb.close()
            print(rows)
            print(type(rows))

            h = Scrollbar(showDataFrame, orient=HORIZONTAL)

            v = Scrollbar(showDataFrame, orient=VERTICAL)

            h.pack(side=BOTTOM, fill=X)
            v.pack(side=RIGHT, fill=Y)

            txt = Text(showDataFrame, width=15,
                       height=15,
                       # foreground='magenta',

                       font=('arial', 12, 'bold'),
                       xscrollcommand=h.set,
                       yscrollcommand=v.set)

            optionList = [
                "Id:"
                ,
                "Name:",
                "Mother's Name:",
                "Gender:",
                "Postcode:",
                "Contact Number:"
                ,
                "Email:",
                "Nationality:",
                "Id Proof:",
                "Id Number:",
                "Address:"
            ]

            for j in range(len(rows)):
                txt.insert(END, f'{optionList[j]} {rows[j]}\n')

            txt.pack(side=TOP, fill=X)

            h.config(command=txt.xview)
            v.config(command=txt.yview)

    # search system

    def search(self):
        conn = mysql.connector.connect(
            host='localhost',
            username='root',
            password='1234',
            database='hotelmanagement'
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room where "
                          + str(self.search_var.get()) + " LIKE '%" +
                          str(self.text_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

        # total
    def total(self):
        inData=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inData=datetime.strptime(inData,'%d/%m/%Y')
        outData = datetime.strptime(outDate, '%d/%m/%Y')
        self.var_noofdays.set((outData-inData).days)

        if (self.var_meal.get().lower()=='breakfast' or self.var_roomtype.get().lower()=='laxary'):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="BDT."+str("%.2f"%((q5)*0.1))
            ST="BDT."+str("%.2f"%((q5)))
            TT="BDT."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get().lower()=='launch' or self.var_roomtype.get().lower()=='single'):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="BDT."+str("%.2f"%((q5)*0.1))
            ST="BDT."+str("%.2f"%((q5)))
            TT="BDT."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


        elif (self.var_meal.get().lower() == 'breakfast' or self.var_roomtype.get().lower() == 'duplex'):
            q1 = float(500)
            q2 = float(1000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "BDT." + str("%.2f" % ((q5) * 0.1))
            ST = "BDT." + str("%.2f" % ((q5)))
            TT = "BDT." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)





if __name__ == '__main__':
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
