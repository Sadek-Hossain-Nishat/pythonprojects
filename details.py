from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import mysql.connector
from time import strftime
from datetime import datetime
from tkinter import messagebox


class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title('Hotel Management System')
        self.root.geometry('1295x550+230+220')

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
                                    text='New Room Add',
                                    padx=2,
                                    font=('times new roman', 12, 'bold'))
        labelframeleft.place(x=0, y=50, width=540,
                             height=350)

        # ================labels and entries=======================
        # =============== Floor ==============

        label_floor = Label(labelframeleft,
                                   text='Floor',
                                   font=('arial', 12, 'bold'),
                                   padx=2, pady=6)
        label_floor.grid(row=0, column=0,
                                sticky=W)

        self.var_floor = StringVar()

        enty_floor = ttk.Entry(labelframeleft,
                               textvariable=self.var_floor,
                                 width=20,
                                 font=('arial', 13, 'bold'),

                                 )
        enty_floor.grid(row=0, column=1,
                          sticky=W)

        # =============== Room No ==============

        label_RoomNo = Label(labelframeleft,
                            text='Room No',
                            font=('arial', 12, 'bold'),
                            padx=2, pady=6)
        label_RoomNo.grid(row=1, column=0,
                         sticky=W)

        self.var_roomNo = StringVar()

        enty_RoomNo = ttk.Entry(labelframeleft,
                               width=20,
                               font=('arial', 13, 'bold'),
                                textvariable=self.var_roomNo

                               )
        enty_RoomNo.grid(row=1, column=1,
                        sticky=W)

        # =============== Room Type ==============

        label_RoomType = Label(labelframeleft,
                            text='Room Type',
                            font=('arial', 12, 'bold'),
                            padx=2, pady=6)
        label_RoomType.grid(row=2, column=0,
                         sticky=W)

        self.var_RoomType = StringVar()

        enty_RoomType = ttk.Entry(labelframeleft,
                               width=20,
                               font=('arial', 13, 'bold'),
                                  textvariable=self.var_RoomType

                               )
        enty_RoomType.grid(row=2, column=1,
                        sticky=W)

        #         ====================btn========================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE,
                          )
        btn_frame.place(x=00, y=200, width=412,
                        height=40)
        btnAdd = Button(btn_frame, text='Add',
                         font=('arial', 12, 'bold'),
                         bg='black', fg='gold',
                         width=9,
                        command=self.add_data

                         )
        btnAdd.grid(row=0, column=0, padx=1)

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

        # ===================Table Frame Search====================================
        table_frame = LabelFrame(self.root,
                                 bd=2, relief=RIDGE,
                                 text='Show Room Details',
                                 padx=2,
                                 font=('times new roman', 12, 'bold'))
        table_frame.place(x=600, y=55, width=600,
                          height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(table_frame, column=("floor","roomno","roomType"
                                                              ), xscrollcommand=scroll_x.set,
                                       yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading('floor', text='Floor')
        self.room_table.heading('roomno', text='Room No ')
        self.room_table.heading('roomType', text='Room Type')


        self.room_table['show'] = 'headings'

        self.room_table.column('floor', width=100)
        self.room_table.column('roomno', width=100)
        self.room_table.column('roomType', width=100)


        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind('<ButtonRelease-1>', self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get() == "" or self.var_RoomType.get() == "":
            messagebox.showerror('Error', 'All fields are required', parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost',
                                               username='root',
                                               password='1234',
                                               database='hotelmanagement',
                                               port=3333)
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values"
                                  "(%s,%s,%s)", (
                                      self.var_floor.get(),
                                      self.var_roomNo.get(),
                                      self.var_RoomType.get()
                                  ))


                conn.commit()
                self.fetch_data()

                conn.close()

                messagebox.showinfo('Success', 'New Room Added Successfully',
                                    parent=self.root)

            except Exception as e:
                messagebox.showwarning('Warning',
                                       f'Some thing Went Wrong{e}',
                                       parent=self.root)

        #             fetch data

    def fetch_data(self):
        conn = mysql.connector.connect(
            host='localhost',
            username='root',
            password='1234',
            database='hotelmanagement',
            port =3333
        )
        my_cursor = conn.cursor()
        my_cursor.execute('select * from details')
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

        self.var_floor.set(row[0])
        self.var_roomNo.set(row[1])
        self.var_RoomType.set(row[2])




    # update
    def update(self):
        if self.var_floor.get() == '':
            messagebox.showerror('Error',
                                 'Please Enter Mobile Number',
                                 parent=self.root)
        else:
            conn = mysql.connector.connect(
                host='localhost',
                username='root',
                password='1234',
                database='hotelmanagement',
                port =3333
            )
            my_cursor = conn.cursor()
            my_cursor.execute(
                'update details set floor=%s,roomtype=%s'
                ' where roomno=%s',
                (self.var_floor.get(),
                 self.var_RoomType.get(),
                 self.var_roomNo.get()
                 ))
            conn.commit()
            self.fetch_data()
            conn.close()
            self.fetch_data()
            messagebox.showinfo('Update',
                                'New Room details has been updated successfully', parent=self.root)



    def mDelete(self):

        mDelete = messagebox.askyesno('Hotel Management System',
                                      'Do you want to delete this Room Details Data',
                                      parent=self.root)

        if mDelete > 0:
            conn = mysql.connector.connect(
                host='localhost',
                username='root',
                password='1234',
                database='hotelmanagement',
                port =3333
            )
            my_cursor = conn.cursor()
            query = "delete from details where roomno=%s"
            value = (self.var_roomNo.get(),)





            my_cursor.execute(query, value)

            conn.commit()
            conn.close()
        else:
            if not mDelete:
                return

        self.fetch_data()


    def reset(self):
        # self.var_ref.set('')

        self.var_floor.set('')
        self.var_roomNo.set('')
        self.var_RoomType.set('')



if __name__ == '__main__':
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()