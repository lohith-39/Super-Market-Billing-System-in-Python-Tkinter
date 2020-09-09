from tkinter import *
import tkinter.messagebox
from PIL import ImageTk
import productdb
import customerdb
import billdb
import random
import datetime
import sqlite3
x=0
tot=0.0

def billrec(event):
    global sd3
    searchB=billlist.curselection()[0]
    sd2=billlist.get(searchB)
    sd3=sd2.split()
    pnotxt.delete(0,END)
    quatxt.delete(0,END)
    quatxt.insert(END,sd3[2])
def modbill():
    global tot
    if(len(bno.get())!=0):
        billdb.delete(bno.get(),sd3[1])
    if(len(bno.get())!=0):
        cost=float(sd3[3])*float(qua.get())
        dcost=cost-(cost*int(sd3[4])/100)
        tot+=float(dcost)
        tottxt.delete(0,END)
        tott.set(str("{:.2f}".format(tot)))
        billdb.addB(bno.get(),time.get(),cno.get(),name,qua.get(),tott.get())
        #billlist.insert(END,str(x).ljust(25,' ')+name.ljust(36,' ')+qua.get().ljust(27,' ')+price.ljust(30,' ')+dis.ljust(15,' ')+str("{:.2f}".format(dcost)).ljust(10,' '))

    

def Print():
    total=tott.get()
    print("Bill No:",bno.get())
    print("Date and Time",time.get())
    print("Total=",float(total))
def clear():
    pnotxt.delete(0,END)
    quatxt.delete(0,END)



def search():
    try:
        global x
        global tot
        global name
        global price
        global dis
        global dcost
        con=sqlite3.connect("productdb.sqlite")
        cur=con.cursor()
        sql="SELECT * FROM product WHERE pid='%s'"%pno.get()
        cur.execute(sql)
        result=cur.fetchone()
        sno=result[0]
        name=result[2]
        price=result[3]
        dis=result[4]
        cost=float(price)*float(qua.get())
        dcost=cost-(cost*int(dis)/100)
        x=x+1 
        #billlist.insert(END,str("{0:<25}".format(x))+str("{0:<36}".format(name))+str("{0:<27}".format(qua.get()))+str("{0:<30}".format(price))+str("{0:<17}".format(dis))+str("{0:<27.2f}".format(dcost))+"\n")  
        billlist.insert(END,str(x).ljust(25,' ')+name.ljust(36,' ')+qua.get().ljust(27,' ')+price.ljust(30,' ')+dis.ljust(15,' ')+str("{:.2f}".format(dcost)).ljust(10,' '))
        tot+=float(dcost)
        tott.set(str("{:.2f}".format(tot)))
        billdb.addB(bno.get(),time.get(),cno.get(),name,qua.get(),tott.get())
        clear()
    except:
        tkinter.messagebox.showinfo("No Data","No Product Found")
        clear()

def bill():
    screen3=Toplevel(screen)
    screen3.title("BILL")
    screen3.geometry("1350x7500+0+0")
    screen3.config(bg="silver")
    main3_Frame=Frame(screen3,bg="silver")
    main3_Frame.grid()

    global pno
    global qua
    global pnotxt
    global quatxt
    global datatxt
    global tott
    global tottxt
    global bno
    global time
    global billlist
    global cno
    bno=StringVar()
    time=StringVar()
    cno=StringVar()
    pno=StringVar()
    qua=StringVar()
    tott=StringVar()

    x=random.randint(10903,600873)
    randomNu=str(x)
    bno.set(randomNu)
    now=datetime.datetime.now()
    time1=now.strftime("%d-%m-%Y %H:%M:%S")
    time2=time1
    time.set(time2)
    

    TitleFrame2=Frame(main3_Frame,bd=2,padx=54,pady=8,bg="silver",relief=RIDGE)
    TitleFrame2.pack(side=TOP)

    Titlelbl2=Label(TitleFrame2,font=("Calibiri",15,"bold"),text="BILL",bg="silver")
    Titlelbl2.grid()

    ButtonFrame2=Frame(main3_Frame,bd=2,width=1350,height=170,padx=18,pady=10,bg="silver",relief=RIDGE)
    ButtonFrame2.pack(side=TOP)
    DataFrame2=Frame(main3_Frame,bd=1,width=1300,height=400,padx=20,pady=20,bg="Ghost White",relief=RIDGE)
    DataFrame2.pack(side=TOP)

    ButtonFrame3=Frame(main3_Frame,bd=1,width=1350,height=70,padx=18,pady=10,bg="silver",relief=RIDGE)
    ButtonFrame3.pack(side=BOTTOM)

    bnolbl=Label(ButtonFrame2,font=("Calibiri",10,"bold"),text="BILL NO:",padx=2,pady=2,bg="silver")
    bnolbl.grid(row=0,column=0,sticky=W)
    bnotxt=Entry(ButtonFrame2,font=("Calibiri",10,"bold"),textvariable=bno,width=15)
    bnotxt.grid(row=0,column=1,sticky=W)

    timelbl=Label(ButtonFrame2,font=("Calibiri",10,"bold"),text="Date and Time",padx=2,pady=2,bg="silver")
    timelbl.grid(row=3,column=0,sticky=W)
    timetxt=Entry(ButtonFrame2,font=("Calibiri",10,"bold"),textvariable=time,width=35)
    timetxt.grid(row=3,column=1,sticky=W)
    
    cnolbl=Label(ButtonFrame2,font=("Calibiri",10,"bold"),text="Customer Phno",padx=2,pady=2,bg="silver")
    cnolbl.grid(row=4,column=0,sticky=W)
    cnotxt=Entry(ButtonFrame2,font=("Calibiri",10,"bold"),textvariable=cno,width=15)
    cnotxt.grid(row=4,column=1,sticky=W)

    pnolbl=Label(ButtonFrame2,font=("Calibiri",10,"bold"),text="Enter Product Number",padx=2,pady=2,bg="silver")
    pnolbl.grid(row=5,column=0,sticky=W)
    pnotxt=Entry(ButtonFrame2,font=("Calibiri",10,"bold"),textvariable=pno,width=15)
    pnotxt.grid(row=5,column=1)

    qualbl=Label(ButtonFrame2,font=("Calibiri",10,"bold"),text="Quauntity",padx=2,pady=2,bg="silver")
    qualbl.grid(row=5,column=2,sticky=W)
    quatxt=Entry(ButtonFrame2,font=("Calibiri",10,"bold"),textvariable=qua,width=15)
    quatxt.grid(row=5,column=3)

    btnAdd=Button(ButtonFrame2,text="Add",font=("Calibiri",10,"bold"),height=1,width=8,bd=2,command=search)
    btnAdd.grid(row=5,column=5,sticky=NW)

    btndel=Button(ButtonFrame2,text="Modify",font=("Calibiri",10,"bold"),height=1,width=8,bd=2,command=modbill)
    btndel.grid(row=5,column=6)
    

    datalbl=Label(DataFrame2,font=("Calibiri",10,"bold"),pady=10,text="S.NO\t ProductName\t\t Quauntity\t Price\t\t Discount\t Cost",bd=7)
    datalbl.grid(row=0,column=0,columnspan=4)
    #datatxt=Text(DataFrame2,height=16,width=110,font=("Calibiri",10,"bold"))
    #datatxt.grid(row=1,column=0,columnspan=4)

    scrollbar=Scrollbar(DataFrame2)
    scrollbar.grid(row=1,column=1,sticky='ns')

    billlist=Listbox(DataFrame2,width=73,height=16,font=("Calibiri",12,"bold"),yscrollcommand=scrollbar.set)
    billlist.bind("<<ListboxSelect>>",billrec)
    billlist.grid(row=1,column=0,padx=8)
    scrollbar.config(command=billlist.yview)
    totlbl=Label(ButtonFrame3,text="Total",font=("Calibiri",10,"bold"),pady=10,bg="silver")
    totlbl.grid(row=0,column=1)
    tottxt=Entry(ButtonFrame3,font=("Calibiri",10,"bold"),textvariable=tott,width=10)
    tottxt.grid(row=0,column=2)
    
    btnprint=Button(ButtonFrame3,text="Print Bill",font=("Calibiri",10,"bold"),height=1,width=8,bd=2,command=Print)
    btnprint.grid(row=1,column=1)

    
    

    
    

    
def iExitc():
    iExit=tkinter.messagebox.askyesno("Customer ADMIN","DO YOU WANT TO EXIT")
    if iExit>0:
        screen2.destroy()
        return
def clearc():
    Cidtxt.delete(0,END)
    Cnametxt.delete(0,END)
    Phnotxt.delete(0,END)
def addc():
    if(len(Cid.get())!=0):
        customerdb.addCustomer(Cid.get(),Cname.get(),Phno.get())
        customerlist.delete(0,END)
        customerlist.insert(END,(Cid.get(),Cname.get(),Phno.get()))
            
def displayc():
    customerlist.delete(0,END)
    for row in customerdb.viewData():
        customerlist.insert(END,row,str(""))
def customerrec(event):
    global sd1
    searchC=customerlist.curselection()[0]
    sd1=customerlist.get(searchC)
    Cidtxt.delete(0,END)
    Cidtxt.insert(END,sd1[1])
    Cnametxt.delete(0,END)
    Cnametxt.insert(END,sd1[2])
    Phnotxt.delete(0,END)
    Phnotxt.insert(END,sd1[3])
def deletec():
    if(len(Cid.get())!=0):
        customerdb.delete(sd1[0])
        clearc()
        displayc()
def searchc():
    customerlist.delete(0,END)
    for row in customerdb.search(Cid.get(),Cname.get(),Phno.get()):
        customerlist.insert(END,row,str(""))
def modifyc():
    if(len(Cid.get())!=0):
        customerdb.delete(sd[0])
    if(len(Cid.get())!=0):
        customerdb.addCustomer(Cid.get(),Cname.get(),Phno.get())
        customerlist.delete(0,END)
        customerlist.insert(END,(Cid.get(),Cname.get(),Phno.get()))


def customer_admin():
    global screen2
    screen2=Toplevel(screen)
    screen2.title("Customer Admin")
    screen2.geometry("1350x7500+0+0")
    screen2.config(bg="cadet blue")

    global Cid
    global Cname
    global Phno

    global Cidtxt
    global Cnametxt
    global Phnotxt
    global customerlist

    Cid=StringVar()
    Cname=StringVar()
    Phno=StringVar()
    
    main2_Frame=Frame(screen2,bg="cadet blue")
    main2_Frame.grid()

    TitleFrame1=Frame(main2_Frame,bd=2,padx=54,pady=8,bg="Ghost White",relief=RIDGE)
    TitleFrame1.pack(side=TOP)

    Titlelbl1=Label(TitleFrame1,font=("Calibiri",47,"bold"),text="Customer ADMIN",bg="yellow")
    Titlelbl1.grid()

    ButtonFrame1=Frame(main2_Frame,bd=2,width=1350,height=70,padx=18,pady=10,bg="red",relief=RIDGE)
    ButtonFrame1.pack(side=BOTTOM)

    DataFrame1=Frame(main2_Frame,bd=1,width=1300,height=400,padx=20,pady=20,bg="light green",relief=RIDGE)
    DataFrame1.pack(side=BOTTOM)

    DataFrameLEFT1=LabelFrame(DataFrame1,font=("Calibiri",20,"bold"),text="Customer Info\n",bd=1,width=1000,height=600,padx=20,relief=RIDGE,bg="Ghost White")
    DataFrameLEFT1.pack(side=LEFT)

    DataFrameRIGHT1=LabelFrame(DataFrame1,font=("Calibiri",20,"bold"),text="Customer Details\n",bd=1,width=450,height=300,padx=31,pady=3,relief=RIDGE,bg="Ghost White")
    DataFrameRIGHT1.pack(side=RIGHT)

    Cidlbl=Label(DataFrameLEFT1,font=("Calibiri",20,"bold"),text="Customer ID",padx=2,pady=2,bg="Ghost White")
    Cidlbl.grid(row=0,column=0,sticky=W)
    Cidtxt=Entry(DataFrameLEFT1,font=("Calibiri",20,"bold"),textvariable=Cid,width=39)
    Cidtxt.grid(row=0,column=1)


    Cnamelbl=Label(DataFrameLEFT1,font=("Calibiri",20,"bold"),text="Customer Name",padx=2,pady=2,bg="Ghost White")
    Cnamelbl.grid(row=1,column=0,sticky=W)
    Cnametxt=Entry(DataFrameLEFT1,font=("Calibiri",20,"bold"),textvariable=Cname,width=39)
    Cnametxt.grid(row=1,column=1)

    Phnolbl=Label(DataFrameLEFT1,font=("Calibiri",20,"bold"),text="Customer Phno",padx=2,pady=2,bg="Ghost White")
    Phnolbl.grid(row=2,column=0,sticky=W)
    Phnotxt=Entry(DataFrameLEFT1,font=("Calibiri",20,"bold"),textvariable=Phno,width=39)
    Phnotxt.grid(row=2,column=1)

    
    scrollbar=Scrollbar(DataFrameRIGHT1)
    scrollbar.grid(row=0,column=1,sticky='ns')

    customerlist=Listbox(DataFrameRIGHT1,width=41,height=16,font=("Calibiri",12,"bold"),yscrollcommand=scrollbar.set)
    customerlist.bind("<<ListboxSelect>>",customerrec)
    customerlist.grid(row=0,column=0,padx=8)
    scrollbar.config(command=customerlist.yview)

    btnAdd=Button(ButtonFrame1,text="Add Customer",font=("Calibiri",20,"bold"),height=1,width=10,bd=4,command=addc)
    btnAdd.grid(row=0,column=0)

    btnDisplay=Button(ButtonFrame1,text="Display",font=("Calibiri",20,"bold"),height=1,width=10,bd=4,command=displayc)
    btnDisplay.grid(row=0,column=1)

    btnClear=Button(ButtonFrame1,text="Clear",font=("Calibiri",20,"bold"),height=1,width=10,bd=4,command=clearc)
    btnClear.grid(row=0,column=2)

    btnDel=Button(ButtonFrame1,text="Delete",font=("Calibiri",20,"bold"),height=1,width=10,bd=4,command=deletec)
    btnDel.grid(row=0,column=3)

    btnSearch=Button(ButtonFrame1,text="Search",font=("Calibiri",20,"bold"),height=1,width=10,bd=4,command=searchc)
    btnSearch.grid(row=0,column=4)

    btnMod=Button(ButtonFrame1,text="Modify",font=("Calibiri",20,"bold"),height=1,width=10,bd=4,command=modifyc)
    btnMod.grid(row=0,column=5)

    btnExit=Button(ButtonFrame1,text="Exit",font=("Calibiri",20,"bold"),height=1,width=10,bd=4,command=iExitc)
    btnExit.grid(row=0,column=6)


def iExitp():
    iExit=tkinter.messagebox.askyesno("Product Admin","DO YOU WANT TO EXIT")
    if iExit>0:
        screen1.destroy()
        return
def clearp():
    Pidtxt.delete(0,END)
    Pnametxt.delete(0,END)
    Pricetxt.delete(0,END)
    Distxt.delete(0,END)
def addp():
    if(len(Pid.get())!=0):
        productdb.addProduct(Pid.get(),Pname.get(),Price.get(),Dis.get())
        productlist.delete(0,END)
        productlist.insert(END,(Pid.get(),Pname.get(),Price.get(),Dis.get()))
def displayp():
    productlist.delete(0,END)
    for row in productdb.viewData():
        productlist.insert(END,row,str(""))
def productrec(event):
    global sd
    searchP=productlist.curselection()[0]
    sd=productlist.get(searchP)
    Pidtxt.delete(0,END)
    Pidtxt.insert(END,sd[1])
    Pnametxt.delete(0,END)
    Pnametxt.insert(END,sd[2])
    Pricetxt.delete(0,END)
    Pricetxt.insert(END,sd[3])
    Distxt.delete(0,END)
    Distxt.insert(END,sd[4])
def deletep():
    if(len(Pid.get())!=0):
        productdb.delete(sd[0])
        clearp()
        displayp()
def searchp():
    productlist.delete(0,END)
    for row in productdb.search(Pid.get(),Pname.get(),Price.get(),Dis.get()):
        productlist.insert(END,row,str(""))
def modifyp():
    if(len(Pid.get())!=0):
        productdb.delete(sd[0])
    if(len(Pid.get())!=0):
        productdb.addProduct(Pid.get(),Pname.get(),Price.get(),Dis.get())
        productlist.delete(0,END)
        productlist.insert(END,(Pid.get(),Pname.get(),Price.get(),Dis.get()))
    
def product_admin():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Product Admin")
    screen1.geometry("1350x7500+0+0")
    screen1.config(bg="cadet blue")

    global Pid
    global Pname
    global Price
    global Dis

    global Pidtxt
    global Pnametxt
    global Pricetxt
    global Distxt
    global productlist

    Pid=StringVar()
    Pname=StringVar()
    Price=StringVar()
    Dis=StringVar()

    main1_Frame=Frame(screen1,bg="cadet blue")
    main1_Frame.grid()

    TitleFrame=Frame(main1_Frame,bd=2,padx=54,pady=8,bg="Ghost White",relief=RIDGE)
    TitleFrame.pack(side=TOP)

    Titlelbl=Label(TitleFrame,font=("Calibiri",47,"bold"),text="PRODUCT ADMIN",bg="yellow")
    Titlelbl.grid()

    ButtonFrame=Frame(main1_Frame,bd=2,width=1350,height=70,padx=18,pady=10,bg="red",relief=RIDGE)
    ButtonFrame.pack(side=BOTTOM)

    DataFrame=Frame(main1_Frame,bd=1,width=1300,height=400,padx=20,pady=20,bg="light green",relief=RIDGE)
    DataFrame.pack(side=BOTTOM)

    DataFrameLEFT=LabelFrame(DataFrame,font=("Calibiri",20,"bold"),text="Product Info\n",bd=1,width=1000,height=600,padx=20,relief=RIDGE,bg="Ghost White")
    DataFrameLEFT.pack(side=LEFT)

    DataFrameRIGHT=LabelFrame(DataFrame,font=("Calibiri",20,"bold"),text="Product Details\n",bd=1,width=450,height=300,padx=31,pady=3,relief=RIDGE,bg="Ghost White")
    DataFrameRIGHT.pack(side=RIGHT)

    Pidlbl=Label(DataFrameLEFT,font=("Calibiri",20,"bold"),text="Product ID",padx=2,pady=2,bg="Ghost White")
    Pidlbl.grid(row=0,column=0,sticky=W)
    Pidtxt=Entry(DataFrameLEFT,font=("Calibiri",20,"bold"),textvariable=Pid,width=39)
    Pidtxt.grid(row=0,column=1)


    Pnamelbl=Label(DataFrameLEFT,font=("Calibiri",20,"bold"),text="Product Name",padx=2,pady=2,bg="Ghost White")
    Pnamelbl.grid(row=1,column=0,sticky=W)
    Pnametxt=Entry(DataFrameLEFT,font=("Calibiri",20,"bold"),textvariable=Pname,width=39)
    Pnametxt.grid(row=1,column=1)

    Pricelbl=Label(DataFrameLEFT,font=("Calibiri",20,"bold"),text="Product Price",padx=2,pady=2,bg="Ghost White")
    Pricelbl.grid(row=2,column=0,sticky=W)
    Pricetxt=Entry(DataFrameLEFT,font=("Calibiri",20,"bold"),textvariable=Price,width=39)
    Pricetxt.grid(row=2,column=1)

    Dislbl=Label(DataFrameLEFT,font=("Calibiri",20,"bold"),text="Product Discount",padx=2,pady=2,bg="Ghost White")
    Dislbl.grid(row=3,column=0,sticky=W)
    Distxt=Entry(DataFrameLEFT,font=("Calibiri",20,"bold"),textvariable=Dis,width=39)
    Distxt.grid(row=3,column=1)

    scrollbar=Scrollbar(DataFrameRIGHT)
    scrollbar.grid(row=0,column=1,sticky='ns')

    productlist=Listbox(DataFrameRIGHT,width=41,height=16,font=("Calibiri",12,"bold"),yscrollcommand=scrollbar.set)
    productlist.bind("<<ListboxSelect>>",productrec)
    productlist.grid(row=0,column=0,padx=8)
    scrollbar.config(command=productlist.yview)

    btnAdd=Button(ButtonFrame,text="Add Product",font=("Calibiri",20,"bold"),height=1,width=10,bd=4,command=addp)
    btnAdd.grid(row=0,column=0)

    btnDisplay=Button(ButtonFrame,text="Display",font=("Calibiri",20,"bold"),height=1,width=10,bd=4,command=displayp)
    btnDisplay.grid(row=0,column=1)

    btnClear=Button(ButtonFrame,text="Clear",font=("Calibiri",20,"bold"),height=1,width=10,bd=4,command=clearp)
    btnClear.grid(row=0,column=2)

    btnDel=Button(ButtonFrame,text="Delete",font=("Calibiri",20,"bold"),height=1,width=10,bd=4,command=deletep)
    btnDel.grid(row=0,column=3)

    btnSearch=Button(ButtonFrame,text="Search",font=("Calibiri",20,"bold"),height=1,width=10,bd=4,command=searchp)
    btnSearch.grid(row=0,column=4)

    btnMod=Button(ButtonFrame,text="Modify",font=("Calibiri",20,"bold"),height=1,width=10,bd=4,command=modifyp)
    btnMod.grid(row=0,column=5)

    btnExit=Button(ButtonFrame,text="Exit",font=("Calibiri",20,"bold"),height=1,width=10,bd=4,command=iExitp)
    btnExit.grid(row=0,column=6)

    


def main_screen():
    global screen
    screen=Tk()
    screen.geometry("1000x750")
    screen.title("SuperMarket")
    bg_icon=ImageTk.PhotoImage(file="bg.jpg")
    bg_lbl=Label(screen,image=bg_icon).pack()
    title=Label(screen,text="SUPER MARKET",font=("Calibiri",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
    title.place(x=0,y=0,relwidth=1)
    main_Frame=Frame(screen)
    main_Frame.place(x=400,y=150)
    P=Button(main_Frame,text="PRODUCT ADMIN",height="2",width="20",font=("Calibiri",12,"bold"),bg="lightgreen",fg="red",bd=5,relief=GROOVE,activebackground="pink",command=product_admin).grid(row=0,column=1,padx=10,pady=10)
    C=Button(main_Frame,text="CUSTOMER ADMIN",height="2",width="20",font=("Calibiri",12,"bold"),bg="lightgreen",fg="red",bd=5,relief=GROOVE,activebackground="pink",command=customer_admin).grid(row=10,column=1,padx=10,pady=10)
    E=Button(main_Frame,text="BILL",height="2",width="20",font=("Calibiri",12,"bold"),bg="lightgreen",fg="red",bd=5,relief=GROOVE,activebackground="pink",command=bill).grid(row=20,column=1,padx=10,pady=10)

    
    screen.mainloop()
main_screen()
