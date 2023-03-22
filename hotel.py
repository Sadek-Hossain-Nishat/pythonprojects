from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1550x800+0+0')
        #=======1st image =========
        img1=Image.open('.\hotel_images\hotel1.png')
        img1=img1.resize((1550, 140), Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root, image=self.photoimage1, bd=4, relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        #===========logo image===========
        img2 = Image.open('.\hotel_images\logohotel.png')
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimage2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)
        #=============title===============
        lbl_title=Label(self.root,text='HOTEL MANAGEMENT SYSTEM',
                        font=('times new roman',40,'bold'),
                        bg='black',fg='gold',bd=4,
                        relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        # =============main frame =====================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)
        #=================menu==========================
        lbl_menu = Label(main_frame, text='MENU',
                          font=('times new roman', 20, 'bold'),
                          bg='black', fg='gold', bd=4,
                          relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)
        # =============btn frame =====================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=222,height=190)

        cust_btn=Button(btn_frame,text='CUSTOMER',
                        font=('times new roman', 14, 'bold'),
                        bg='black', fg='gold',
                        bd=0,width=22,
                        cursor='hand2',
                        command=self.cust_details
                        )
        cust_btn.grid(row=0,column=0)

        room_btn = Button(btn_frame, text='ROOM',
                          font=('times new roman', 14, 'bold'),
                          bg='black', fg='gold',
                          bd=0, width=22,
                          cursor='hand2',
                          command=self.roombooking
                          )
        room_btn.grid(row=1, column=0)

        details_btn = Button(btn_frame, text='DETAILS',
                          font=('times new roman', 14, 'bold'),
                          bg='black', fg='gold',
                          bd=0, width=22,
                          cursor='hand2',
                             command=self.details_room
                          )
        details_btn.grid(row=2, column=0)

        report_btn = Button(btn_frame, text='REPORT',
                          font=('times new roman', 14, 'bold'),
                          bg='black', fg='gold',
                          bd=0, width=22,
                          cursor='hand1'
                          )
        report_btn.grid(row=3, column=0)
        logout_btn = Button(btn_frame, text='LOGOUT',
                          font=('times new roman', 14, 'bold'),
                          bg='black', fg='gold',
                          bd=0, width=22,
                          cursor='hand1',
                            command=self.logout
                          )
        logout_btn.grid(row=4, column=0)
        #===========right side image================
        img3 = Image.open('.\hotel_images\slide3.jpg')
        img3 = img3.resize((1310,590), Image.ANTIALIAS)
        self.photoimage3= ImageTk.PhotoImage(img3)
        lblimg = Label(main_frame, image=self.photoimage3, bd=4, relief=RIDGE)
        lblimg.place(x=225, y=0, width=1310, height=590)
        # ===========down images================
        img4 = Image.open('.\hotel_images\myh.jpg')
        img4 = img4.resize((230, 210), Image.ANTIALIAS)
        self.photoimage4 = ImageTk.PhotoImage(img4)
        lblimg = Label(main_frame, image=self.photoimage4, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=225, width=230, height=210)

        img5 = Image.open('./hotel_images/food.jpg')
        img5 = img5.resize((230, 190), Image.ANTIALIAS)
        self.photoimage5 = ImageTk.PhotoImage(img5)
        lblimg = Label(main_frame, image=self.photoimage5, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=420, width=230, height=190)
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)


    def details_room(self):
        self.new_window = Toplevel(self.root)
        self.app =DetailsRoom(self.new_window)


    def logout(self):
        self.root.destroy()





if __name__ == '__main__':
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()