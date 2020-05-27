from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import sqlite3
import csv

#First View
shoot_root=Tk()
shoot_root.title("Welcome")
shoot_root.geometry('1180x580')
shoot_root.configure(bg='aquamarine')

shoot_root_label_title=Label(shoot_root,text="Welcome to the Hotel Management System",bg='azure',font=("Palatino",42,'bold','italic'))
shoot_root_label_title.place(x=90,y=100)

welcome_text=""""My name is Muhammad Usman Pervaiz. Welcome to the
Hotel Managemnet System. I would like to thankyou
for choosing our hotel. May you love our servics
and Enjoy your stay"
"""
shoot_root_welcome_text_label=Label(shoot_root,text=welcome_text,font=("Georgia",16,"italic"),bg='aquamarine')
shoot_root_welcome_text_label.place(x=290,y=220)

#Create table for customers
conn=sqlite3.connect("Hotel Management.db")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS customers_data(
          Name text,
          PhoneNo text,
          City text,
          Room_Type text,
          No_Of_Rooms int,
          No_of_days int,
          Price int)""")
conn.commit()
conn.close()





class Hotel_Management_System:
    def __init__(self):
        self.root=Tk()
        self.root.title("Hotel Managemnet System")
        self.root.geometry("1030x685")
        self.root.resizable(False, False)
        #self.root.minsize(width=1030,height=680)
        #self.root.maxsize(width=1030,height=680)
        self.root.configure(background='brown')

    def Booked(self,room_name):
        Price=self.Set_Price(room_name)
        #print(Price)
        conn=sqlite3.connect("Hotel Management.db")
        c=conn.cursor()
        c.execute("INSERT INTO customers_data VALUES(:name,:Phone_no,:city,:Roomtype,:NoofRoom,:for_how_many_day,:price)",
                  {
                      'name':Name.get(),
                      'Phone_no':PhoneNo.get(),
                      'city':city.get(),
                      'Roomtype':room_name,
                      'NoofRoom':NoOfRoom.get(),
                      'for_how_many_day':for_how_many_days.get(),
                      'price':Price
                      })
                  
        conn.commit()
        conn.close()

        #Message Popup
        response=messagebox.showinfo("Your Booking is Confirm","Thankyou")
        reserve_root.destroy()
    def reserve(self,room_name):
        global reserve_root
        reserve_root=Tk()
        reserve_root.title("Reserve Your Room")
        #reserve_root.geometry(str(300+len(room_name)*12+20)+"x400")
        reserve_root.geometry('670x450')
        reserve_root.configure(background='light cyan')

        #Title
        title_label=Label(reserve_root,text="RESERVE YOUR {} ROOM".format(room_name),font=("Times","18","italic","bold"),bg='paleTurquoise2')
        title_label.grid(row=0,column=0,columnspan=4,padx=20,pady=(4,8))
        
        #Entry box
        global Name
        global PhoneNo
        global city
        global NoOfRoom
        global for_how_many_days
        Name=Entry(reserve_root,width=40,font=("Times 13 italic"),fg='saddle brown')
        Name.grid(row=1,column=1,padx=(0,20),pady=15)
        PhoneNo=Entry(reserve_root,width=40,font=("Times 13 italic"),fg='saddle brown')
        PhoneNo.grid(row=2,column=1,padx=(0,20),pady=15)
        city=Entry(reserve_root,width=40,font=("Times 13 italic"),fg='saddle brown')
        city.grid(row=3,column=1,padx=(0,20),pady=15)
        NoOfRoom=Entry(reserve_root,width=40,font=("Times 13 italic"),fg='saddle brown')
        NoOfRoom.grid(row=4,column=1,padx=(0,20),pady=15)
        for_how_many_days=Entry(reserve_root,width=40,font=("Times 13 italic"),fg='saddle brown')
        for_how_many_days.grid(row=5,column=1,padx=(0,20),pady=15)
        

        #Labels
        name_label=Label(reserve_root,text="Name:",font=("Candara 13 bold italic"),bg='light cyan')
        name_label.grid(row=1,column=0,padx=(0,20),pady=15)
        PhoneNo_label=Label(reserve_root,text="Phone Number:",font=("Candara 13 bold italic"),bg='light cyan')
        PhoneNo_label.grid(row=2,column=0,padx=(0,20),pady=15)
        city_label=Label(reserve_root,text="City:",font=("Candara 13 bold italic"),bg='light cyan')
        city_label.grid(row=3,column=0,padx=(0,20),pady=15)
        NoOfRoom_label=Label(reserve_root,text="How many room you want:",font=("Candara 13 bold italic"),bg='light cyan')
        NoOfRoom_label.grid(row=4,column=0,padx=(0,20),pady=15)
        for_how_many_days_label=Label(reserve_root,text="How many days you want to stay:",font=("Candara 13 bold italic"),bg='light cyan')
        for_how_many_days_label.grid(row=5,column=0,padx=(5,20),pady=15)
        
        Booking_btn=Button(reserve_root,text="Booking",font=("Helvitica 12"),width=30,borderwidth=3,bg='mint cream',command=lambda:self.Booked(room_name))
        Booking_btn.grid(row=7,column=0,columnspan=2,pady=6,padx=10)

    def Set_Price(self,room_name):
        price_dict={"STANDARD":12000,"DELUXE":14000,"EXECUTIVE":16000,"BUSINESS SUITE":18000,"DELUXE SUITE":20000,"PRESIDENTIAL SUITE":24000}
        price_set=price_dict[room_name]*int(NoOfRoom.get())*int(for_how_many_days.get())
        return price_set
    def Standard_detail(self):
        top=Toplevel()
        top.title("Standard Room Deatil")
        top.geometry("930x630")
        top.configure(background='peachpuff')

        #Standard Title
        Title_Stadard=Label(top,text='Standard',font=("Time 18 bold italic"),bg='AntiqueWhite1')
        Title_Stadard.grid(row=0,column=0,pady=(10,0))

        #For Standard Image
        img = Image.open("images/Standard Room.PNG")
        width, height = img.size
        Standard_room_image=ImageTk.PhotoImage(Image.open("images/Standard Room.PNG").resize((round(320/height*width) , round(300))))
        Standard_room_image_label=Label(top,image=Standard_room_image,bg='black')
        Standard_room_image_label.grid(row=0,column=1,padx=20,pady=20,rowspan=4)
        
        Standrad_welcome="Combining a neutral-colour palette with chic\nfurnishings, the compact-size Standard Room\nwelcomes you to a pleasant stay."
        Standrad_welcome_Label=Label(top,text=Standrad_welcome,font=("Helvetica 12 italic"),bg='peachpuff')
        Standrad_welcome_Label.grid(row=1,column=0,stick=N)

        #Frame Work
        frm=LabelFrame(top,padx=10,pady=10,bg='peachpuff2')
        frm.grid(row=2,column=0,padx=10,pady=10,stick=N)
        Room_size_label=Label(frm,text="Room size",font=("Helvetica 11 bold"),bg='peachpuff2')
        Room_size_label.grid(row=0,column=0,padx=10)
        bed_size_label=Label(frm,text="Bed Size(s)",font=("Helvetica 11 bold"),bg='peachpuff2')
        bed_size_label.grid(row=0,column=1,padx=10)
        view_label=Label(frm,text="View",font=("Helvetica 11 bold"),bg='peachpuff2')
        view_label.grid(row=0,column=2,padx=10)
        room_size_detail_label=Label(frm,text="322 Sq feet",font=("Helvetica 10"),bg='peachpuff2')
        room_size_detail_label.grid(row=1,column=0,padx=10)
        bed_size_detail_label=Label(frm,text="1 King/Queen or Twin",font=("Helvetica 10"),bg='peachpuff2')
        bed_size_detail_label.grid(row=1,column=1,padx=10)
        view_size_detail_label=Label(frm,text="City View, Pool View",font=("Helvetica 10"),bg='peachpuff2')
        view_size_detail_label.grid(row=1,column=2,padx=10)
    
        #Features Details
        Features_Label=Label(top,text="FEATURES",font=('Helvetica 13 bold'),bg='AntiqueWhite1')
        Features_Label.grid(row=3,column=0)
        Features_detail_label=Label(top,text=""">Air-conditioning
 >Bathroom amenities
 >Hair dryer
 >Safe in room
 >Writing Desk and chair
 >Iron and ironing board on request
 >Room service
 >Complimentary bottled water
 >Phone
 >Wireless Internet Access
 >Flat screen TV
 >LCD/LED TV
 >Cable/satellite channels""",relief=SUNKEN,anchor=W,font=('Helvetica 11 italic'),bg='peachpuff')
        Features_detail_label.grid(row=4,column=0,sticky=N)
        price_frame=LabelFrame(top,padx=100,pady=50,bg='peachpuff')

        #Frame Box
        price_frame.grid(row=4,column=1,padx=10,pady=10)
        price_label=Label(price_frame,text="Rs: 12000",font=('Helvetica 11'),bg='peachpuff')
        price_label.pack(padx=(0,20),pady=15)
        No_of_room_label=Label(price_frame,text="No of Room Avaliable: 50",font=('Helvetica 11'),bg='peachpuff')
        No_of_room_label.pack(padx=(0,20),pady=15)

        #close_Button
        close_btn=Button(top,text="Close",width=24,borderwidth=4,font=('Helvetica 12 italic'),bg='azure',command=top.destroy)
        close_btn.grid(row=5,column=0,columnspan=5,pady=(6,0))

        top.mainloop()

    def deluxe_detail(self):
        top=Toplevel()
        top.title("Deluxe Deatil")
        top.geometry("930x630")
        top.configure(background='peachpuff')

        #Deluxe Title
        Title_Deluxe=Label(top,text='Deluxe',font=("Time 18 bold italic"),bg='AntiqueWhite1')
        Title_Deluxe.grid(row=0,column=0,pady=(10,0))

        #For Deluxe Image
        img = Image.open("images/DELUXE.PNG")
        width, height = img.size
        Deluxe_image=ImageTk.PhotoImage(Image.open("images/DELUXE.PNG").resize((round(320/height*width) , round(300))))
        Deluxe_image_label=Label(top,image=Deluxe_image,bg='black')
        Deluxe_image_label.grid(row=0,column=1,padx=20,pady=20,rowspan=4)
        
        Deluxe_welcome="Inspired by the rich cultural heritage of Lahore,\n the spacious Deluxe Room furnishes modern\n furniture in earthen tones."
        Deluxe_welcome_Label=Label(top,text=Deluxe_welcome,font=("Helvetica 12 italic"),bg='peachpuff')
        Deluxe_welcome_Label.grid(row=1,column=0,stick=N)

        #Frame Work
        frm=LabelFrame(top,padx=10,pady=10,bg='peachpuff2')
        frm.grid(row=2,column=0,padx=10,pady=10,stick=N)
        Room_size_label=Label(frm,text="Room size",font=("Helvetica 11 bold"),bg='peachpuff2')
        Room_size_label.grid(row=0,column=0,padx=10)
        bed_size_label=Label(frm,text="Bed Size(s)",font=("Helvetica 11 bold"),bg='peachpuff2')
        bed_size_label.grid(row=0,column=1,padx=10)
        view_label=Label(frm,text="View",font=("Helvetica 11 bold"),bg='peachpuff2')
        view_label.grid(row=0,column=2,padx=10)
        room_size_detail_label=Label(frm,text="420 Sq feet",font=("Helvetica 10"),bg='peachpuff2')
        room_size_detail_label.grid(row=1,column=0,padx=10)
        bed_size_detail_label=Label(frm,text="1 King or Twin",font=("Helvetica 10"),bg='peachpuff2')
        bed_size_detail_label.grid(row=1,column=1,padx=10)
        view_size_detail_label=Label(frm,text="City View, Pool View,",font=("Helvetica 10"),bg='peachpuff2')
        view_size_detail_label.grid(row=1,column=2,padx=10)
        view_size_detail_label2=Label(frm,text="Atrium View, Garden View",font=("Helvetica 10"),bg='peachpuff2')
        view_size_detail_label2.grid(row=2,column=2,padx=10)
    
        #Features Details
        Features_Label=Label(top,text="FEATURES",font=('Helvetica 13 bold'),bg='AntiqueWhite1')
        Features_Label.grid(row=3,column=0)
        Features_detail_label=Label(top,text=""">Air-conditioning
>Bathroom amenities
>Hair dryer
>Writing Desk and chair
>Iron and ironing board on request
>Room service
>Complimentary bottled water
>Phone
>Wireless Internet Access
>Flat screen TV
>Cable/satellite channels""",relief=SUNKEN,anchor=W,font=('Helvetica 11 italic'),bg='peachpuff')
        Features_detail_label.grid(row=4,column=0,sticky=N)
        price_frame=LabelFrame(top,padx=100,pady=50,bg='peachpuff')

        #Frame Box
        price_frame.grid(row=4,column=1,padx=10,pady=10)
        price_label=Label(price_frame,text="Rs: 14000",font=('Helvetica 11'),bg='peachpuff')
        price_label.pack(padx=(0,20),pady=15)
        No_of_room_label=Label(price_frame,text="No of Room Avaliable: 42",font=('Helvetica 11'),bg='peachpuff')
        No_of_room_label.pack(padx=(0,20),pady=15)

        #close_Button
        close_btn=Button(top,text="Close",width=24,borderwidth=5,font=('Helvetica 12 italic'),bg='azure',command=top.destroy)
        close_btn.grid(row=5,column=0,columnspan=5,pady=(6,0))

        top.mainloop()

    def Executive_detail(self):
        top=Toplevel()
        top.title("Executive Deatil")
        top.geometry("930x610")
        top.configure(background='peachpuff')

        #Executive Title
        Title_Executive=Label(top,text='Executive',font=("Time 18 bold italic"),bg='AntiqueWhite1')
        Title_Executive.grid(row=0,column=0,pady=(10,0))

        #For Executive Image
        img = Image.open("images/Executive.PNG")
        width, height = img.size
        Executive_image=ImageTk.PhotoImage(Image.open("images/Executive.PNG").resize((round(300/height*width) , round(280))))
        Executive_room_image_label=Label(top,image=Executive_image,bg='black')
        Executive_room_image_label.grid(row=0,column=1,padx=20,pady=20,rowspan=4)
        
        Executive_welcome="""Furnishing chic and contemporary décor, the
Executive Room offers spacious interiors
designed to your comfort. Avail exclusive check-
in and check-out facilities on the same ﬂoor, as
well as free access to the Executive Lounge."""
        Executive_welcome_Label=Label(top,text=Executive_welcome,font=("Helvetica 12 italic"),bg='peachpuff')
        Executive_welcome_Label.grid(row=1,column=0,stick=N)

        #Frame Work
        frm=LabelFrame(top,padx=10,pady=10,bg='peachpuff2')
        frm.grid(row=2,column=0,padx=10,pady=10,stick=N)
        Room_size_label=Label(frm,text="Room size",font=("Helvetica 11 bold"),bg='peachpuff2')
        Room_size_label.grid(row=0,column=0,padx=10)
        bed_size_label=Label(frm,text="Bed Size(s)",font=("Helvetica 11 bold"),bg='peachpuff2')
        bed_size_label.grid(row=0,column=1,padx=10)
        view_label=Label(frm,text="View",font=("Helvetica 11 bold"),bg='peachpuff2')
        view_label.grid(row=0,column=2,padx=10)
        room_size_detail_label=Label(frm,text="322 Sq feet",font=("Helvetica 10"),bg='peachpuff2')
        room_size_detail_label.grid(row=1,column=0,padx=10)
        bed_size_detail_label=Label(frm,text="1 King/Queen or Twin",font=("Helvetica 10"),bg='peachpuff2')
        bed_size_detail_label.grid(row=1,column=1,padx=10)
        view_size_detail_label=Label(frm,text="City View, Pool View,",font=("Helvetica 10"),bg='peachpuff2')
        view_size_detail_label.grid(row=1,column=2,padx=10)
        view_size_detail_label2=Label(frm,text="Atrium View, Garden View",font=("Helvetica 10"),bg='peachpuff2')
        view_size_detail_label2.grid(row=2,column=2,padx=10)
    
        #Features Details
        Features_Label=Label(top,text="FEATURES",font=('Helvetica 13 bold'),bg='AntiqueWhite1')
        Features_Label.grid(row=3,column=0)
        Features_detail_label=Label(top,text=""">Air-conditioning
>Bathroom amenities
>Hair dryer
>Safe in room
>Writing Desk and chair
>Iron and ironing board on request
>Room service
>Complimentary bottled water
>Mini-refrigerator
>Phone
>Wireless Internet Access
>Flat screen TV
>Cable/satellite channels""",relief=SUNKEN,anchor=W,font=('Helvetica 11 italic'),bg='peachpuff')
        Features_detail_label.grid(row=4,column=0,sticky=N)
        price_frame=LabelFrame(top,padx=100,pady=50,bg='peachpuff')

        #Frame Box
        price_frame.grid(row=4,column=1,padx=10,pady=10)
        price_label=Label(price_frame,text="Rs: 16000",font=('Helvetica 11'),bg='peachpuff')
        price_label.pack(padx=(0,20),pady=15)
        No_of_room_label=Label(price_frame,text="No of Room Avaliable: 36",font=('Helvetica 11'),bg='peachpuff')
        No_of_room_label.pack(padx=(0,20),pady=15)

        #close_Button
        close_btn=Button(top,text="Close",width=24,borderwidth=5,font=('Helvetica 12 italic'),bg='azure',command=top.destroy)
        close_btn.grid(row=5,column=0,columnspan=5,pady=(6,0))

        top.mainloop()

    def BUSINESS_SUITE_detail(self):
        top=Toplevel()
        top.title("Business Suite Deatil")
        top.geometry("930x650")
        top.configure(background='peachpuff')

        #Business Suite Title
        Title_Business_Suite=Label(top,text='Business Suite',font=("Time 18 bold italic"),bg='AntiqueWhite1')
        Title_Business_Suite.grid(row=0,column=0,pady=(10,0))

        #For Business Suite Image
        img = Image.open("images/BUSINESS SUITE.PNG")
        width, height = img.size
        Business_Suite_image=ImageTk.PhotoImage(Image.open("images/BUSINESS SUITE.PNG").resize((round(320/height*width) , round(300))))
        Business_Suite_image_label=Label(top,image=Business_Suite_image,bg='black')
        Business_Suite_image_label.grid(row=0,column=1,padx=20,pady=20,rowspan=4)
        
        Business_Suite_welcome="""Equipping you to meet all your business needs,
        the suite furnishes a workspace connecting to
        high-speed internet and surroundings that ensure
        optimum focus and productivity."""
        Business_Suite_welcome_Label=Label(top,text=Business_Suite_welcome,font=("Helvetica 12 italic"),bg='peachpuff')
        Business_Suite_welcome_Label.grid(row=1,column=0,stick=N)

        #Frame Work
        frm=LabelFrame(top,padx=10,pady=10,bg='peachpuff2')
        frm.grid(row=2,column=0,padx=10,pady=10,stick=N)
        Room_size_label=Label(frm,text="Room size",font=("Helvetica 11 bold"),bg='peachpuff2')
        Room_size_label.grid(row=0,column=0,padx=10)
        bed_size_label=Label(frm,text="Bed Size(s)",font=("Helvetica 11 bold"),bg='peachpuff2')
        bed_size_label.grid(row=0,column=1,padx=10)
        view_label=Label(frm,text="View",font=("Helvetica 11 bold"),bg='peachpuff2')
        view_label.grid(row=0,column=2,padx=10)
        room_size_detail_label=Label(frm,text="484 Sq feet",font=("Helvetica 10"),bg='peachpuff2')
        room_size_detail_label.grid(row=1,column=0,padx=10)
        bed_size_detail_label=Label(frm,text="1 King",font=("Helvetica 10"),bg='peachpuff2')
        bed_size_detail_label.grid(row=1,column=1,padx=10)
        view_size_detail_label=Label(frm,text="City View, Pool View,",font=("Helvetica 10"),bg='peachpuff2')
        view_size_detail_label.grid(row=1,column=2,padx=10)
        view_size_detail_label2=Label(frm,text="Atrium View, Garden View",font=("Helvetica 10"),bg='peachpuff2')
        view_size_detail_label2.grid(row=2,column=2,padx=10)
    
        #Features Details
        Features_Label=Label(top,text="FEATURES",font=('Helvetica 13 bold'),bg='AntiqueWhite1')
        Features_Label.grid(row=3,column=0)
        Features_detail_label=Label(top,text=""">Air-conditioning
>Separate Living Room
>Bathroom amenities
>Hair dryer
>Safe in room
>Writing Desk and chair
>Iron and ironing board on request
>Room service
>Complimentary bottled water
>Coffee maker / tea service
>Mini-refrigerator
>Phone
>Flat screen TV
>Cable/satellite channels""",relief=SUNKEN,anchor=W,font=('Helvetica 11 italic'),bg='peachpuff')
        Features_detail_label.grid(row=4,column=0,sticky=N)
        price_frame=LabelFrame(top,padx=100,pady=50,bg='peachpuff')

        #Frame Box
        price_frame.grid(row=4,column=1,padx=10,pady=10)
        price_label=Label(price_frame,text="Rs: 18000",font=('Helvetica 11'),bg='peachpuff')
        price_label.pack(padx=(0,20),pady=15)
        No_of_room_label=Label(price_frame,text="No of Room Avaliable: 24",font=('Helvetica 11'),bg='peachpuff')
        No_of_room_label.pack(padx=(0,20),pady=15)

        #close_Button
        close_btn=Button(top,text="Close",width=24,borderwidth=5,font=('Helvetica 12 italic'),bg='azure',command=top.destroy)
        close_btn.grid(row=5,column=0,columnspan=5,pady=(6,0))

        top.mainloop()

    def DELUXE_SUITE_detail(self):
        top=Toplevel()
        top.title("Deluxe Suite Deatil")
        top.geometry("930x660")
        top.configure(background='peachpuff')

        #Deluxe Suite Title
        Title_Deluxe_Suite=Label(top,text='Deluxe Suite',font=("Time 18 bold italic"),bg='AntiqueWhite1')
        Title_Deluxe_Suite.grid(row=0,column=0,pady=(10,0))

        #For Deluxe Suite Image
        img = Image.open("images/DELUXE SUITE.PNG")
        width, height = img.size
        Deluxe_Suite_image=ImageTk.PhotoImage(Image.open("images/DELUXE SUITE.PNG").resize((round(320/height*width) , round(300))))
        Deluxe_Suite_image_label=Label(top,image=Deluxe_Suite_image,bg='black')
        Deluxe_Suite_image_label.grid(row=0,column=1,padx=20,pady=20,rowspan=4)
        
        Deluxe_Suite_welcome="""Overlooking the beautiful city of Lahore,
spacious Deluxe Suite is a blend of comfort and
magnificence. The impeccably-designed suite
provides you all the comforts of home."""
        Deluxe_Suite_welcome_Label=Label(top,text=Deluxe_Suite_welcome,font=("Helvetica 12 italic"),bg='peachpuff')
        Deluxe_Suite_welcome_Label.grid(row=1,column=0,stick=N)

        #Frame Work
        frm=LabelFrame(top,padx=10,pady=10,bg='peachpuff2')
        frm.grid(row=2,column=0,padx=10,pady=10,stick=N)
        Room_size_label=Label(frm,text="Room size",font=("Helvetica 11 bold"),bg='peachpuff2')
        Room_size_label.grid(row=0,column=0,padx=10)
        bed_size_label=Label(frm,text="Bed Size(s)",font=("Helvetica 11 bold"),bg='peachpuff2')
        bed_size_label.grid(row=0,column=1,padx=10)
        view_label=Label(frm,text="View",font=("Helvetica 11 bold"),bg='peachpuff2')
        view_label.grid(row=0,column=2,padx=10)
        room_size_detail_label=Label(frm,text="877 Sq feet",font=("Helvetica 10"),bg='peachpuff2')
        room_size_detail_label.grid(row=1,column=0,padx=10)
        bed_size_detail_label=Label(frm,text="1 King",font=("Helvetica 10"),bg='peachpuff2')
        bed_size_detail_label.grid(row=1,column=1,padx=10)
        view_size_detail_label=Label(frm,text="City View, Pool View",font=("Helvetica 10"),bg='peachpuff2')
        view_size_detail_label.grid(row=1,column=2,padx=10)
        view_size_detail_label2=Label(frm,text="Atrium View, Garden View",font=("Helvetica 10"),bg='peachpuff2')
        view_size_detail_label2.grid(row=2,column=2,padx=10)
    
        #Features Details
        Features_Label=Label(top,text="FEATURES",font=('Helvetica 13 bold'),bg='AntiqueWhite1')
        Features_Label.grid(row=3,column=0)
        Features_detail_label=Label(top,text=""">Air-conditioning
>Separate Living Area
>Bathroom amenities
>Hair dryer
>Safe in room
>Writing Desk and chair
>Iron and ironing board on request
>Room service
>Complimentary bottled water
>Coffee maker / tea service
>Mini-refrigerator
>Phone
>Wireless Internet Access
>TV features: 40 inch
>Cable/satellite channels""",relief=SUNKEN,anchor=W,font=('Helvetica 11 italic'),bg='peachpuff')
        Features_detail_label.grid(row=4,column=0,sticky=N)
        price_frame=LabelFrame(top,padx=100,pady=50,bg='peachpuff')

        #Frame Box
        price_frame.grid(row=4,column=1,padx=10,pady=10)
        price_label=Label(price_frame,text="Rs: 20000",font=('Helvetica 11'),bg='peachpuff')
        price_label.pack(padx=(0,20),pady=15)
        No_of_room_label=Label(price_frame,text="No of Room Avaliable: 16",font=('Helvetica 11'),bg='peachpuff')
        No_of_room_label.pack(padx=(0,20),pady=15)

        #close_Button
        close_btn=Button(top,text="Close",width=24,borderwidth=5,font=('Helvetica 12 italic'),bg='azure',command=top.destroy)
        close_btn.grid(row=5,column=0,columnspan=5,pady=(6,0))

        top.mainloop()
    def PRESIDENTIAL_SUITE_detail(self):
        top=Toplevel()
        top.title("Presidential Suite Deatil")
        top.geometry("930x630")
        top.configure(background='peachpuff')

        #Presidential Suite Title
        Title_Presidential_Suite=Label(top,text='Presidential Suite',font=("Time 18 bold italic"),bg='AntiqueWhite1')
        Title_Presidential_Suite.grid(row=0,column=0,columnspan=2,pady=(10,0))

        #For Presidential Suite Image
        img = Image.open("images/PRESIDENTIAL SUITE.PNG")
        width, height = img.size
        Presidential_Suite_image=ImageTk.PhotoImage(Image.open("images/PRESIDENTIAL SUITE.PNG").resize((round(320/height*width) , round(300))))
        Presidential_Suite_image_label=Label(top,image=Presidential_Suite_image,bg='black')
        Presidential_Suite_image_label.grid(row=0,column=3,padx=20,pady=20,rowspan=4)
        
        Presidential_Suite_welcome="Luxuriate yourself in our elegantly-designed\n Presidential Suite, and unwind in the master\n bedroom that offers views of the cityscape."
        Presidential_Suite_welcome_Label=Label(top,text=Presidential_Suite_welcome,font=("Helvetica 12 italic"),bg='peachpuff')
        Presidential_Suite_welcome_Label.grid(row=1,column=0,columnspan=2,stick=N)

        #Frame Work
        frm=LabelFrame(top,padx=10,pady=10,bg='peachpuff2')
        frm.grid(row=2,column=0,columnspan=2,padx=10,pady=10,stick=N)
        Room_size_label=Label(frm,text="Room size",font=("Helvetica 11 bold"),bg='peachpuff2')
        Room_size_label.grid(row=0,column=0,padx=10)
        bed_size_label=Label(frm,text="Bed Size(s)",font=("Helvetica 11 bold"),bg='peachpuff2')
        bed_size_label.grid(row=0,column=1,padx=10)
        view_label=Label(frm,text="View",font=("Helvetica 11 bold"),bg='peachpuff2')
        view_label.grid(row=0,column=2,padx=10)
        room_size_detail_label=Label(frm,text="1,162 Sq feet",font=("Helvetica 10"),bg='peachpuff2')
        room_size_detail_label.grid(row=1,column=0,padx=10)
        bed_size_detail_label=Label(frm,text="1 King",font=("Helvetica 10"),bg='peachpuff2')
        bed_size_detail_label.grid(row=1,column=1,padx=10)
        view_size_detail_label=Label(frm,text="City View, Mall Road View",font=("Helvetica 10"),bg='peachpuff2')
        view_size_detail_label.grid(row=1,column=2,padx=10)
    
        #Features Details
        Features_Label=Label(top,text="FEATURES",font=('Helvetica 13 bold'),bg='AntiqueWhite1')
        Features_Label.grid(row=3,column=0)
        Features_detail_label=Label(top,text=""">Air-conditioning
>Separate Living area
>2 Washrooms
>Tub/Jacuzzi/Shower
>Bathroom amenities
>Hair dryer
>Safe in room
>Writing Desk and chair
>Iron and ironing board on request
>Room service
>Complimentary bottled water
>Laundry Area
>Kitchenette""",relief=SUNKEN,anchor=W,font=('Helvetica 11 italic'),bg='peachpuff')
        Features_detail_label.grid(row=4,column=0,padx=(10,0),sticky=N)
        Features_detail_label2=Label(top,text=""">Coffee maker/tea service
>Mini-refrigerator
>Cordless phone, voicemail and
speaker phone
>Wireless Internet Access
>TV features: 65 inch
>Cable/satellite channels""",relief=SUNKEN,anchor=W,font=('Helvetica 11 italic'),bg='peachpuff')
        Features_detail_label2.grid(row=4,column=1,sticky=N)
        price_frame=LabelFrame(top,padx=100,pady=50,bg='peachpuff')

        #Frame Box
        price_frame.grid(row=4,column=3,padx=10,pady=10)
        price_label=Label(price_frame,text="Rs: 24000",font=('Helvetica 11'),bg='peachpuff')
        price_label.pack(padx=(0,20),pady=15)
        No_of_room_label=Label(price_frame,text="No of Room Avaliable: 6",font=('Helvetica 11'),bg='peachpuff')
        No_of_room_label.pack(padx=(0,20),pady=15)

        #close_Button
        close_btn=Button(top,text="Close",width=24,borderwidth=5,font=('Helvetica 12 italic'),bg='azure',command=top.destroy)
        close_btn.grid(row=5,column=0,columnspan=5,pady=(6,0))

        top.mainloop()
    def Quary(self):
        conn=sqlite3.connect("Hotel Management.db")
        c=conn.cursor()
        c.execute("SELECT *,oid FROM customers_data")
        global records
        records=c.fetchall()
        conn.commit()
        conn.close()

    def Save_csv(self):
        head=["Name","Phone Number","City","Room Type","No of Rooms","No of Days","Price","ID"]
        with open('Hotel Management.csv','a') as i:
            z=csv.writer(i,dialect='excel')
            z.writerow(head)
        with open('Hotel Management.csv','a',newline='') as f:
            w=csv.writer(f,dialect='excel')
            for x in records:
                w.writerow(x)

    def show_table(self):
        top_pop=Toplevel()
        top_pop.title("Customers Data")
        top_pop.geometry("1390x650")
        top_pop.configure(background='mint cream')
        
        #Menu Bars
        table_menu = Menu(top_pop)
        top_pop.config(menu=table_menu)

        save_menu = Menu(table_menu)
        table_menu.add_cascade(label='Save',menu=save_menu)
        save_menu.add_command(label="Save to Excel",command=self.Save_csv)
        
        close_menu = Menu(table_menu)
        table_menu.add_cascade(label="Exit",menu=close_menu)
        close_menu.add_command(label="Close",command=top_pop.destroy)
        
        
        self.Quary()
        frm=Frame(top_pop)
        frm.grid(row=0,column=0,columnspan=6)#side=tk.LEFT,padx=20)

        tv=ttk.Treeview(frm,column=(1,2,3,4,5,6,7),show="headings",height=len(records))
        tv.pack()
        tv.heading(1,text="Name")
        tv.heading(2,text="PhoneNo")
        tv.heading(3,text="City")
        tv.heading(4,text="Room Type")
        tv.heading(5,text="No Of Rooms")
        tv.heading(6,text="No Of Days")
        tv.heading(7,text="Price")

        for record in records:
            tv.insert('','end',values=record)

            
        
    def Customer_View(self):
        #Title Label
        Title_Label=Label(self.root,text="Hotel Management System",font=("Helvetica 24 bold italic"),bg='floral white')
        Title_Label.grid(row=0,column=0,columnspan=6,padx=(20,0),pady=10)

        #Menu Bars
        my_menu = Menu(self.root)
        self.root.config(menu=my_menu)

        ##Craete a Open table manu item

        open_menu = Menu(my_menu)
        my_menu.add_cascade(label="Show",menu=open_menu)
        open_menu.add_command(label="Open Table",command=self.show_table)

        #Create a Exit Menu
        option_menu = Menu(my_menu)
        my_menu.add_cascade(label="Exit",menu=option_menu)
        option_menu.add_command(label="Close",command=self.root.destroy)
                

        
        #For standard room
        Standard_room_title_label=Label(self.root,text="Standard Room",fg='white',bg='black',font=("Helvetica 18 bold italic"))
        Standard_room_title_label.grid(row=1,column=0,columnspan=2,padx=20,pady=(5,0))
        img = Image.open("images/Standard Room.PNG")
        width, height = img.size
        Standard_room_image=ImageTk.PhotoImage(Image.open("images/Standard Room.PNG").resize((round(230/height*width) , round(230))))
        Standard_room_image_label=Label(image=Standard_room_image,bg='black')
        Standard_room_image_label.grid(row=2,column=0,columnspan=2,padx=10)
        Standard_room_reserve_btn=Button(self.root,text="Reserve",width=20,borderwidth=4,bg='azure',command=lambda:self.reserve("STANDARD"))
        Standard_room_reserve_btn.grid(row=3,column=0,padx=(10,0),pady=2)
        Standard_room_detail_btn=Button(self.root,text="Detail",width=20,borderwidth=4,bg='azure',command=self.Standard_detail)
        Standard_room_detail_btn.grid(row=3,column=1,padx=(0,10),pady=2)


        #For DELUXE room
        DELUXE_title_label=Label(self.root,text="Deluxe Room",fg='white',bg='black',font=("Helvetica 18 bold italic"))
        DELUXE_title_label.grid(row=1,column=2,columnspan=2,padx=20,pady=(5,0))
        img = Image.open("images/DELUXE.PNG")
        width, height = img.size
        DELUXE_image=ImageTk.PhotoImage(Image.open("images/DELUXE.PNG").resize((round(230/height*width) , round(230))))
        DELUXE_image_label=Label(image=DELUXE_image,bg='black')
        DELUXE_image_label.grid(row=2,column=2,columnspan=2,padx=10)
        DELUXE_reserve_btn=Button(self.root,text="Reserve",width=20,borderwidth=4,bg='azure',command=lambda:self.reserve("DELUXE"))
        DELUXE_reserve_btn.grid(row=3,column=2,padx=(10,0),pady=2)
        DELUXE_detail_btn=Button(self.root,text="Detail",width=20,borderwidth=4,bg='azure',command=self.deluxe_detail)
        DELUXE_detail_btn.grid(row=3,column=3,padx=(0,10),pady=2)

        #For EXECUTIVE room
        EXECUTIVE_title_label=Label(self.root,text="Executive Room",fg='white',bg='black',font=("Helvetica 18 bold italic"))
        EXECUTIVE_title_label.grid(row=1,column=4,columnspan=2,padx=20,pady=(5,0))
        img = Image.open("images/Executive.PNG")
        width, height = img.size
        EXECUTIVE_image=ImageTk.PhotoImage(Image.open("images/Executive.PNG").resize((round(230/height*width) , round(230))))
        EXECUTIVE_image_label=Label(image=EXECUTIVE_image,bg='black')
        EXECUTIVE_image_label.grid(row=2,column=4,columnspan=2,padx=10)
        EXECUTIVE_reserve_btn=Button(self.root,text="Reserve",width=20,borderwidth=4,bg='azure',command=lambda:self.reserve("EXECUTIVE"))
        EXECUTIVE_reserve_btn.grid(row=3,column=4,padx=(10,0),pady=2)
        EXECUTIVE_detail_btn=Button(self.root,text="Detail",width=20,borderwidth=4,bg='azure',command=self.Executive_detail)
        EXECUTIVE_detail_btn.grid(row=3,column=5,padx=(0,10),pady=2)

        #For BUSINESS SUITE
        BUSINESS_SUITE_title_label=Label(self.root,text="Business Suite Room",fg='white',bg='black',font=("Helvetica 18 bold italic"))
        BUSINESS_SUITE_title_label.grid(row=4,column=0,columnspan=2,padx=20,pady=(5,0))
        img = Image.open("images/BUSINESS SUITE.PNG")
        width, height = img.size
        BUSINESS_SUITE_image=ImageTk.PhotoImage(Image.open("images/BUSINESS SUITE.PNG").resize((round(230/height*width) , round(230))))
        BUSINESS_SUITE_image_label=Label(image=BUSINESS_SUITE_image,bg='black')
        BUSINESS_SUITE_image_label.grid(row=5,column=0,columnspan=2,padx=10)
        BUSINESS_SUITE_reserve_btn=Button(self.root,text="Reserve",width=20,borderwidth=4,bg='azure',command=lambda:self.reserve("BUSINESS SUITE"))
        BUSINESS_SUITE_reserve_btn.grid(row=6,column=0,padx=(10,0),pady=2)
        BUSINESS_SUITE_detail_btn=Button(self.root,text="Detail",width=20,borderwidth=4,bg='azure',command=self.BUSINESS_SUITE_detail)
        BUSINESS_SUITE_detail_btn.grid(row=6,column=1,padx=(0,10),pady=2)

        #For DELUXE SUITE
        DELUXE_SUITE_title_label=Label(self.root,text="Deluxe Suit",fg='white',bg='black',font=("Helvetica 18 bold italic"))
        DELUXE_SUITE_title_label.grid(row=4,column=2,columnspan=2,padx=20,pady=(5,0))
        img = Image.open("images/DELUXE SUITE.PNG")
        width, height = img.size
        DELUXE_SUITEE_image=ImageTk.PhotoImage(Image.open("images/DELUXE SUITE.PNG").resize((round(230/height*width) , round(230))))
        DELUXE_SUITE_image_label=Label(image=DELUXE_SUITEE_image,bg='black')
        DELUXE_SUITE_image_label.grid(row=5,column=2,columnspan=2,padx=10)
        DELUXE_SUITE_reserve_btn=Button(self.root,text="Reserve",width=20,borderwidth=4,bg='azure',command=lambda:self.reserve("DELUXE SUITE"))
        DELUXE_SUITE_reserve_btn.grid(row=6,column=2,padx=(10,0),pady=2)
        DELUXE_SUITE_detail_btn=Button(self.root,text="Detail",width=20,borderwidth=4,bg='azure',command=self.DELUXE_SUITE_detail)
        DELUXE_SUITE_detail_btn.grid(row=6,column=3,padx=(0,10),pady=2)

        #For PRESIDENTIAL SUITE
        PRESIDENTIAL_SUITE_title_label=Label(self.root,text="Presidential Suite",fg='white',bg='black',font=("Helvetica 18 bold italic"))
        PRESIDENTIAL_SUITE_title_label.grid(row=4,column=4,columnspan=2,padx=20,pady=(5,0))
        img = Image.open("images/PRESIDENTIAL SUITE.PNG")
        width, height = img.size
        PRESIDENTIAL_SUITE_image=ImageTk.PhotoImage(Image.open("images/PRESIDENTIAL SUITE.PNG").resize((round(230/height*width) , round(230))))
        PRESIDENTIAL_SUITE_image_label=Label(image=PRESIDENTIAL_SUITE_image,bg='black')
        PRESIDENTIAL_SUITE_image_label.grid(row=5,column=4,columnspan=2,padx=10)
        PRESIDENTIAL_SUITE_reserve_btn=Button(self.root,text="Reserve",width=20,borderwidth=4,bg='azure',command=lambda:self.reserve("PRESIDENTIAL SUITE"))
        PRESIDENTIAL_SUITE_reserve_btn.grid(row=6,column=4,padx=(10,0),pady=2)
        PRESIDENTIAL_SUITE_detail_btn=Button(self.root,text="Detail",width=20,borderwidth=4,bg='azure',command=self.PRESIDENTIAL_SUITE_detail)
        PRESIDENTIAL_SUITE_detail_btn.grid(row=6,column=5,padx=(0,10),pady=2)
        
        self.root.mainloop()

def shoot():
    shoot_root.destroy()
    h=Hotel_Management_System()
    h.Customer_View()
shoot_root.after(2000,shoot)
shoot_root.mainloop()
