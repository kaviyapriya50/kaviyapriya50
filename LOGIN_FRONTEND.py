from tkinter import *
from tkinter import ttk
from LOGIN_BACKEND import INPUTS
from TRACKING_BACKEND import tracking
from tkinter import messagebox
from write import store
import csv

def main():
    global a
    
    a=tracking()
    filename = "csv1.csv"
	
# writing to csv file
    with open(filename, 'a') as csv1: 
            items=csv.reader(csv1)
            for i in items:
                if i==[]:
                    continue
                else:
                    tracking_num=[]
                    for j in range(2,len(i)):
                        tracking_num.append(i[j])
                    a.pushSS([i[0],i[1]],tracking_num)
            a._iter_()
    
    

def submit():
        a=INPUTS()
        details = [e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e11.get(),e12.get()]
        track = e10.get()

        a.push_(details)
        a.push(track)
        _tracking()
def _tracking():
        global screen
        
        screen=LabelFrame(a,bd=2,relief="groove")
           
        screen.place(x=300,y=300,height=100,width=755)
        screen_label=Label(
            screen,
            text="Would you like to TRACK THE STATUS of your parcel ?",
            font="arial 16",
            bg="White",
            fg="black"
            ).grid(row=0,column=1)

        yes=Button(
            screen,
            text="YES",
            command = lambda : s2()
            ).grid(row=3,column=1)

        no=Button(
            screen,
            text="No",
            command= lambda : _back()).grid(row=3,column=3) 
'''def proceed_2():
    if ee1.get() in'''      
        
def proceed():
    s=store()
    s.append_array()
    print(">>>>>>>")
    if e10.get()==ee1.get() and e9.get()==ee4.get() :
        print("*")
        main()
        track_num=[e10.get()]
        loc_pin=[e4.get(),e11.get()]
        #a.pushSS(loc_pin,track_num)

        p=a.getfront()
        status=0
    
        while a.getdest(p)[0]!=e9.get():
                p=a.getnext(p)
        p.t_s=True
        
        i=0
        while s.lst_p()[i][0]!=e9.get():
             i+=1
             
        if e10.get() not in s.lst_p()[i]:
                s.lst_p()[i].append(e10.get())
                p.t_n=s.lst_p()[i][2:len(s.lst_p()[i])]
                
                s=store(s.lst_p())
                s.append_array()
                status=1
        
        main()
        if status==1:
            for i in a.trackno(p):
                #print(i)
                pass
            messagebox.showinfo("STATUS OF THE PARCEL","PARCEL DELIVERED TO THE DESTINATION")
        else:
            print("Service not available")
            messagebox.showinfo("STATUS OF THE PARCEL","PARCEL IS YET TO BE  DELIVERED TO THE DESTINATION")
        print(a.getdest(p),a.trackno(p),a.track(p))
    else:
        no_track()
def find():
    
        
        main()
        
        p=a.getfront()
        for i in range(a.getlen()):
            #print(a.getlen())
            if a.getdest(p)[1]==eee1.get():
                
                print (a.getdest(p)[0],a.trackno(p))
            else:
                
                p=a.getnext(p)  
                continue
    
def no_track():
        messagebox.showinfo(" TRACKING NUMBER NOT FOUND!!" ,"PLEASE CHECK THE TRACKING NUMBER")

def _back():
    screen.destroy()
        
def s1(p):
    global a,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12
    if p is not None:
        p.destroy()
    a=Tk()
    a.title("CUSTOMER DETAILS")
    a.geometry("1080x1000")
    l1=Label(a,text="NAME OF THE CUSTOMER").grid(row=0,column=0)
    l2=Label(a,text="PHONE NUM").grid(row=1,column=0)
    l3=Label(a,text="ADDRESS").grid(row=2,column=0)
    l4=Label(a,text="SOURCE").grid(row=3,column=0)
    l5=Label(a,text="EMAIL").grid(row=4,column=0)
    l6=Label(a,text="NAME OF THE CUSTOMER").grid(row=5,column=0)
    l7=Label(a,text="PHONE NUM").grid(row=6,column=0)
    l8=Label(a,text="ADDRESS").grid(row=7,column=0)
    l9=Label(a,text="DESTINATION").grid(row=8,column=0)
    l10=Label(a,text="TRACKING NUMBER").grid(row=9,column=0)
    l11=Label(a,text="PINCODE OF THE SOURCE").grid(row=10,column=0)
    l12=Label(a,text="PINCODE OF THE DESTINATION").grid(row=11,column=0)


    

    e1=Entry(a)
    e2=Entry(a)
    e3=Entry(a)
    e4=Entry(a)
    e5=Entry(a)
    e6=Entry(a)
    e7=Entry(a)
    e8=Entry(a)
    e9=Entry(a)
    e10=Entry(a)
    e11=Entry(a)
    e12=Entry(a)
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    e3.grid(row=2,column=1)
    e4.grid(row=3,column=1)
    e5.grid(row=4,column=1)
    e6.grid(row=5,column=1)
    e7.grid(row=6,column=1)
    e8.grid(row=7,column=1)
    e9.grid(row=8,column=1)
    e10.grid(row=9,column=1)
    e11.grid(row=10,column=1)
    e12.grid(row=11,column=1)
    sub=Button(a,text="Submit",command=lambda : submit() )
    sub.grid(row=20,column=5)
    subj=Button(a,text="back",command=lambda : back(a) )
    subj.grid(row=20,column=7)
    filename = "csv1.csv"
    '''with open(filename, 'w') as csv1:
        items=csv.reader(csv1)
            for i in items:
                if i[0]==e9.get():'''
def back(a):
    frontpage(a)

def s2():
    global ee1,e2,e3,ee4
    main()
    '''if p is not None:
        p.destroy()'''
    a=Tk()
    a.title("TRACKING STATUS")
    a.geometry("1080x1000")
    l1=Label(a,text="ENTER THE TRACKING NUMBER").grid(row=12,column=0)
   
    l4=Label(a,text="ENTER THE LOCATION NAME OF THE DESTINATION ").grid(row=24,column=0)
    ee1=Entry(a)
    
    ee4=Entry(a)
    ee1.grid(row=12,column=1)
    
    ee4.grid(row=24,column=1)
    sub=Button(a,text="PROCEED",command=lambda : proceed() )
    sub.grid(row=50,column=5)
'''def PROCEED():
    if e10.get()==ee1.get() and e9.get()==ee4.get() :
        print("*")
        main()
        track_num=[e10.get()]
        loc_pin=[e4.get(),e11.get()]
        a.pushSS(loc_pin,track_num)

        p=a.getfront()
        status=0
        print("LEn",a.getlen())
        for i in range(a.getlen()):
            
            if a.getdest(p)[0]==e9.get():
                p.t_s=True
                if a.trackno(p)=='':
                    p.t_n=[]
                p.t_n.append(e10.get())
                status=1
            else:
                p=a.getnext(p)
        if status==1:
            for i in a.trackno(p):
                print(i)
            messagebox.showinfo("STATUS OF THE PARCEL","PARCEL DELIVERED TO THE DESTINATION")
        else:
            print("Service not available")
            messagebox.showinfo("STATUS OF THE PARCEL","PARCEL IS YET TO BE  DELIVERED TO THE DESTINATION")
        print(a.getdest(p),a.trackno(p),a.track(p))
    else:
        no_track()
def TRACK():
    filename="csv1.csv"
    with open(filename, 'r') as csv1: 
            items=csv.reader(csv1)
            for i in items:
                if i[]'''

def s3():
    global eee1
    a=Tk()
    a.title("DATEWISE LIST OF DELIVERIES")
    global e1,e2,e3
    a.geometry("1080x1000")
    l1=Label(a,text="ENTER THE PINCODE").grid(row=0,column=0)
    eee1=Entry(a)
    eee1.grid(row=0,column=1) 
    sub=Button(a,text="SEARCH",command=lambda :find() )
    sub.grid(row=50,column=5)

'''def chumma():
    global eeee1,e2,e3,eeee4
    main()
    if p is not None:
        p.destroy()
    r=Tk()
    r.title("TRACKING STATUS")
    r.geometry("1080x1000")
    l1=Label(r,text="ENTER THE TRACKING NUMBER").grid(row=12,column=0)
   
    l4=Label(r,text="ENTER THE LOCATION NAME OF THE DESTINATION ").grid(row=24,column=0)
    eeee1=Entry(r)
    eeee4=Entry(r)
    
    eeee1.grid(row=12,column=1)
    eeee4.grid(row=24,column=1)

    p=a.getfront()
    c=0
    while a.getnext(p) != None:
        if a.getdest(p)[0] == eeee4.get():
            c+=1
        p=a.getnext(p)
    if c==0:
        messagebox.showinfo("Destination",'Destination not valid !!')
    
    sub=Button(a,text="PROCEED",command=lambda : proceed1() )
    sub.grid(row=50,column=5)'''
def proceed1():
    filename="csv1.csv"
    
    # with open (filename,'r') as csv1:
    with open(filename, 'r') as csv1: 
            items=csv.reader(csv1)
            for i in items:
                print("hii",i)
                if i==[]:
                    continue
                elif i[0]==eeee4.get():
                        messagebox.showinfo("STATUS OF THE PARCEL","PARCEL DELIVERED TO THE DESTINATION")
            else:
                messagebox.showinfo("STATUS OF THE PARCEL","PARCEL YET TO BE DELIVERED ")
def s4():
        global eeee1,e2,e3,eeee4
        main()
        
        r=Tk()
        r.title("TRACKING STATUS")
        r.geometry("1080x1000")
        l1=Label(r,text="ENTER THE TRACKING NUMBER").grid(row=12,column=0)
    
        l4=Label(r,text="ENTER THE LOCATION NAME OF THE DESTINATION ").grid(row=24,column=0)
        eeee1=Entry(r)
        eeee4=Entry(r)
        
        
        eeee1.grid(row=12,column=1)
        eeee4.grid(row=24,column=1)

        p=a.getfront()
        c=0
        while a.getnext(p) != None:
            if a.getdest(p)[0] == eeee4.get():
                c+=1
            p=a.getnext(p)
        if c==0:
            messagebox.showinfo("Destination",'Destination not valid !!')
        
        sub=Button(r,text="PROCEED",command=lambda : proceed1() )
        sub.grid(row=50,column=5)
        

    

def frontpage(p=None):

    def log():
        s1(b)
    if p is not None:
        p.destroy()
    b=Tk()
    b.title("COURIER MANAGEMENT SYSTEM")
    b.geometry("300x275")
   
    def pincodes():
        s2()

    def pin_number():
        s3()

        p.destroy()
    '''def nnn():
        s4()'''
    '''def chumma():
        global eeee1,e2,e3,eeee4
        main()
        
        r=Tk()
        r.title("TRACKING STATUS")
        r.geometry("1080x1000")
        l1=Label(r,text="ENTER THE TRACKING NUMBER").grid(row=12,column=0)
    
        l4=Label(r,text="ENTER THE LOCATION NAME OF THE DESTINATION ").grid(row=24,column=0)
        eeee1=Entry(r)
        eeee4=Entry(r)
        
        eeee1.grid(row=12,column=1)
        eeee4.grid(row=24,column=1)

        p=a.getfront()
        c=0
        while a.getnext(p) != None:
            if a.getdest(p)[0] == eeee4.get():
                c+=1
            p=a.getnext(p)
        if c==0:
            messagebox.showinfo("Destination",'Destination not valid !!')
        
        sub=Button(a,text="PROCEED",command=lambda : proceed1() )
        sub.grid(row=50,column=5)'''
        
    bb1=Button(b,text="STATUS TRACKING ",command=lambda:s4()).grid(row=10,column=200)
    
    bb3=Button(b,text="UPDATES ",command=lambda:pin_number()).grid(row=60,column=200)
    bb2=Button(b,text="LOGIN MANAGEMENT",command=log).grid(row=30,column=200)




   
    
    
    



frontpage(p=None)
mainloop()
