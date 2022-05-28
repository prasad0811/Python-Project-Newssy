import glob
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from turtle import left, right
from click import style
from markupsafe import string 
import requests
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl
import myproject1 as mm
import logo as lo
import webbrowser
import regex as re
import os
from datetime import date, timedelta
import sqlite3
from gnewsclient import gnewsclient
from sklearn.linear_model import Ridge
import myproject1 as my
today = date.today()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Does the url contain a downloadable resource
def is_downloadable(url):
     
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

#dictionary to give links to english newspaper
newspaper1 = dict({
'Economic Times':'https://dailyepaper.in/economic-times-newspaper-today/', 
'Times of India':'https://dailyepaper.in/times-of-india-epaper-pdf-download-2022/',
'Financial Express':'https://dailyepaper.in/financial-express-newspaper/', 
'Deccan Chronicle':'https://dailyepaper.in/deccan-chronicle-epaper/',
'The Telegraph':'https://dailyepaper.in/telegraph-newspaper/', 
'The Hindu':'https://dailyepaper.in/the-hindu-pdf-epaper-free-download-now-09-may-2022/',
'Statesman':'https://dailyepaper.in/statesman-newspaper-today/', 
'The Asian Age':'https://dailyepaper.in/the-asian-age-epaper/',
'The Tribune':'https://dailyepaper.in/the-tribune-epaper/',
})

#dictionary to give serial numbers to english newspaper
serial_num1 = dict({
1:'Economic Times', 
2:'Times of India', 
3:'Financial Express', 
4:'Deccan Chronicle', 
5:'The Telegraph', 
6:'The Hindu', 
7:'Statesman', 
8:'The Asian Age', 
9:'The Tribune', 
})

#dictionary to give links to hindi newspaper
newspaper2 = dict({
'Jansatta':'https://dailyepaper.in/jansatta-epaper-pdf/', 
'Dainik Jagran':'https://dailyepaper.in/dainik-jagran-newspaper-download-2022/',
'Amar Ujala':'https://dailyepaper.in/amar-ujala-news-paper-today/', 
'Navbharat Times':'https://dailyepaper.in/navbharat-times-epaper/',
'Punjab Kesari':'https://dailyepaper.in/punjab-kesari-epaper/', 
'Loksatta':'https://dailyepaper.in/loksatta-newspaper-download/',
'Jansatta':'https://dailyepaper.in/jansatta-epaper-pdf/', 
'Dainik Bhaskar':'https://dailyepaper.in/dainik-bhaskar-epaper/',
'Prabhat Khabar':'https://dailyepaper.in/prabhat-khabar-epaper/',
})

#dictionary to give serial numbers Hindi newspaper
serial_num2 = dict({
1:'Jansatta', 
2:'Dainik Jagran', 
3:'Amar Ujala', 
4:'Navbharat Times', 
5:'Punjab Kesari', 
6:'Loksatta', 
7:'Jansatta', 
8:'Dainik Bhaskar', 
9:'Prabhat Khabar', 
})


def news1(pno):
    
    ser_ind=int(pno)
    
    url = newspaper1[serial_num1[ser_ind]]

    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    list_paper = list()

    directory = serial_num1[ser_ind]
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, directory)

    #make a new directory for given newspaper, if that exists then do nothing
    try:
        os.mkdir(path)
    except OSError as error:
        pass
    os.chdir(path) #enter the directory for newspaper

    #storing links for given newspaper in a list
    for i in range(len(tags)):
        links = tags[i].get('href',None)
        li=str(links)
        x = re.search("^https://vk.com/", li)
        if x:
           list_paper.append(links)
    
    for_how_many_days = int(str(nos.get()))
    days=int(str(nos.get()))
    print(for_how_many_days)
    print(links)
    for i in range(for_how_many_days):
        url = list_paper[i]

        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('iframe')
        link =tags[0].get('src',None)      

        date_that_day = today - timedelta(days=i) #getting the date

        if is_downloadable(link):
            messagebox.showinfo("Information",'Please wait..! Downloading '+serial_num1[ser_ind]+'...')
            
            
            
            r = requests.get(link, allow_redirects=True)
            #to=int(r.headers['content-lengths'])
            #print(to)
            #messagebox.showinfo("Size of Downloading newspaper is " +to)
            with open(serial_num1[ser_ind]+"_"+str(date_that_day)+".pdf",'wb') as f:
                f.write(r.content)
                pb=ttk.Progressbar(ewindow,orient=HORIZONTAL,mode='determinate',length=208)
                pb.pack(expand=True,pady=15)
            messagebox.showinfo("Information",'Please check '+serial_num1[ser_ind]+' folder in current directory') 
        else:
            messagebox.showerror("Error",serial_num1[ser_ind] + ' newspaper not available for '+ str(date_that_day))  
    os.chdir('../') 

    messagebox.showinfo("general information","Thank You for using our Newspaper Scraper")
    #ewindow.destroy()

def news2(pno):
    
    ser_ind=int(pno)
    
    url = newspaper2[serial_num2[ser_ind]]

    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    list_paper = list()

    directory = serial_num2[ser_ind]
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, directory)

    #make a new directory for given newspaper, if that exists then do nothing
    try:
        os.mkdir(path)
    except OSError as error:
        pass
    os.chdir(path) #enter the directory for newspaper

    #storing links for given newspaper in a list
    for i in range(len(tags)):
        links = tags[i].get('href',None)
        li2=str(links)
        x = re.search("^https://vk.com/", li2)
        if x:
            list_paper.append(links)
    
    for_how_many_days = int(str(nos.get()))
    days=int(str(nos.get()))

    for i in range(for_how_many_days):
        url = list_paper[i]

        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('iframe')
        link = tags[0].get('src',None)      

        date_that_day = today - timedelta(days=i) 

        if is_downloadable(link):
            messagebox.showinfo("Information",'Please wait..! Downloading '+serial_num2[ser_ind]+'...')
            r = requests.get(link, allow_redirects=True)
            with open(serial_num2[ser_ind]+"_"+str(date_that_day)+".pdf",'wb') as f:
                f.write(r.content)
            messagebox.showinfo("Information",'Please check '+serial_num2[ser_ind]+' folder in current directory') 
        else:
            messagebox.showerror("Error",serial_num2[ser_ind] + ' newspaper not available for '+ str(date_that_day))  
    os.chdir('../') 

    messagebox.showinfo("general information","Thank You for using our Newspaper Scraper")
    #hwindow.destroy()

def next1():

	def sel():
		selection = "You selected : " + serial_num1[(int(str(var.get())))]
		label.config(text = selection,font=('Arial',15))

	def connect():
		try:
			urllib.request.urlopen('http://google.com') 
			return True
		except:
			messagebox.showerror("Error","Please check your internet connection")   
			connect()

	global ewindow
	ewindow = tk.Tk()
	ewindow.geometry('600x510')
	ewindow['background']='white'

	ewindow.resizable(0,0)
	ewindow.title('Newspaper Scraper')

	connect()

	var = tk.IntVar()

	l1 = tk.Label(ewindow, bg='black',fg='red', font=('Arial',15), width=60, text='English Newspapers')
	l1.pack()

	l2 = tk.Label(ewindow, bg='black',fg='yellow', font=('Arial',12), width=80, text='Please select your choice')
	l2.pack()

	R1 = tk.Radiobutton(ewindow,font=('Arial',15),bg='white', text="1. Economic Times", variable=var, value=1,command=sel)
	R1.pack( anchor = 'w' )

	R2 = tk.Radiobutton(ewindow,font=('Arial',15),bg='white', text="2. Times of India", variable=var, value=2,command=sel)
	R2.pack( anchor = 'w' )
	
	R3 = tk.Radiobutton(ewindow,font=('Arial',15),bg='white', text="3. Financial Express", variable=var, value=3,command=sel)
	R3.pack( anchor = 'w')

	R4 = tk.Radiobutton(ewindow,font=('Arial',15),bg='white', text="4. Deccan Chronicle", variable=var, value=4,command=sel)
	R4.pack( anchor = 'w')

	R5 = tk.Radiobutton(ewindow,font=('Arial',15),bg='white', text="5. The Telegraph", variable=var, value=5,command=sel)
	R5.pack( anchor = 'w')

	R6 = tk.Radiobutton(ewindow,font=('Arial',15),bg='white', text="6. The Hindu", variable=var, value=6,command=sel)
	R6.pack( anchor = 'w')

	R7 = tk.Radiobutton(ewindow,font=('Arial',15),bg='white', text="7. Statesman", variable=var, value=7,command=sel)
	R7.pack( anchor = 'w')

	R8 = tk.Radiobutton(ewindow,font=('Arial',15),bg='white', text="8. The Asian Age", variable=var, value=8,command=sel)
	R8.pack( anchor = 'w')
	
	R9 = tk.Radiobutton(ewindow,font=('Arial',15),bg='white', text="9. The Tribune", variable=var, value=9,command=sel)
	R9.pack( anchor = 'w')

	label = tk.Label(ewindow,bg='white',font=('Arial',15))
	label.pack()

	b1 = tk.Button(ewindow,font=('Arial',15), text = "Download",bg="#16F529",fg="white",command=lambda: news1(str(var.get())))
	b1.pack()
	
	b2 = tk.Button(ewindow,font=('Arial',15), text = "Close",bg="red",fg="white",command=ewindow.destroy)  
	b2.pack(pady=20,side = 'bottom')

	ewindow.mainloop()

def next2():

	def sel():
		selection = "You selected : " + serial_num2[(int(str(var.get())))]
		label.config(text = selection,font=('Arial',15))

	def connect():
		try:
			urllib.request.urlopen('http://google.com') 
			return True
		except:
			messagebox.showerror("Error","Please check your internet connection")
			connect()

	global hwindow
	hwindow = tk.Tk()
	hwindow.geometry('600x510')
	hwindow['background']='white'

	hwindow.resizable(0,0)
	hwindow.title('Newspaper Scraper')

	connect()

	var = tk.IntVar()

	l1 = tk.Label(hwindow, bg='black',fg='red', font=('Arial',15), width=60, text='Hindi Newspapers')
	l1.pack()

	l2 = tk.Label(hwindow, bg='black',fg='yellow', font=('Arial',12), width=80, text='Please select your choice')
	l2.pack()

	R1 = tk.Radiobutton(hwindow,font=('Arial',15), bg='white', text="1.जनसत्ता", variable=var, value=1,command=sel)
	R1.pack( anchor = 'w' )

	R2 = tk.Radiobutton(hwindow,font=('Arial',15), bg='white', text="2. दैनिक जागरण", variable=var, value=2,command=sel)
	R2.pack( anchor = 'w' )

	R3 = tk.Radiobutton(hwindow,font=('Arial',15), bg='white', text="3.अमर उजाला", variable=var, value=3,command=sel)
	R3.pack( anchor = 'w')

	R4 = tk.Radiobutton(hwindow,font=('Arial',15), bg='white', text="4.नवभारत टाइम्स ", variable=var, value=4,command=sel)
	R4.pack( anchor = 'w')

	R5 = tk.Radiobutton(hwindow,font=('Arial',15), bg='white', text="5.पंजाब केसरी", variable=var, value=5,command=sel)
	R5.pack( anchor = 'w')

	R6 = tk.Radiobutton(hwindow,font=('Arial',15), bg='white', text="6.लोकसत्ता", variable=var, value=6,command=sel)
	R6.pack( anchor = 'w')

	R7 = tk.Radiobutton(hwindow,font=('Arial',15), bg='white', text="7.जनसत्ता", variable=var, value=7,command=sel)
	R7.pack( anchor = 'w')

	R8 = tk.Radiobutton(hwindow,font=('Arial',15), bg='white', text="8. दैनिक भास्कर", variable=var, value=8,command=sel)
	R8.pack( anchor = 'w')

	R9 = tk.Radiobutton(hwindow,font=('Arial',15), bg='white', text="9. प्रभात खबर", variable=var, value=9,command=sel)
	R9.pack( anchor = 'w')

	label = tk.Label(hwindow, bg='white',font=('Arial',15))
	label.pack()

	b1 = tk.Button(hwindow,font=('Arial',15), text = "Download",bg="#16F529",fg="white",command= lambda: news2(str(var.get())))   
	b1.pack()

	b2 = tk.Button(hwindow,font=('Arial',15), text = "Close",bg="red",fg="white",command=hwindow.destroy)
	b2.pack(pady=20,side = 'bottom')

	hwindow.mainloop()

def seperate(n,c):

	nwindow.destroy()
	a=int(n)
	b=int(c)

	if(b==1):
		next1()
	elif(b==2):
		next2()

def no_of_days(c):

	cwindow.destroy()		

	def sel():
		selection = "You selected : " + str(nos.get())
		label.config(text = selection,font=('Arial',15))

	global nwindow
	nwindow = tk.Tk()
	nwindow.geometry('600x200')
	nwindow['background']='#ADFF2F'

	nwindow.resizable(0,0)
	nwindow.title('Newspaper Scraper')

	l1 = tk.Label(nwindow, bg='#282e33',fg='white', font=('Arial',15), width=60, text='Newspaper Scraper')
	l1.pack()

	l2 = tk.Label(nwindow, bg='#282e33',fg='white', font=('Arial',15), width=60, text='Please select your choice')
	l2.pack()

	global nos
	nos=tk.IntVar()

	N1 = tk.Radiobutton(nwindow,font=('Arial',15), bg='#ADFF2F', text="Todays newspaper", variable=nos, value=1,command=sel)
	N1.pack( anchor = 'w' )

	N2 = tk.Radiobutton(nwindow,font=('Arial',15), bg='#ADFF2F', text="Last 7 days newspaper", variable=nos, value=7,command=sel)
	N2.pack( anchor = 'w' )

	label = tk.Label(nwindow, bg='#ADFF2F',font=('Arial',15))
	label.pack()

	b1 = tk.Button(nwindow,font=('Arial',15), text = "Next", command=lambda: seperate(str(nos.get()),c))
	b1.pack()
	nwindow.mainloop()

def choose_lang():
    
	def sel():
		selection = "You selected option : " + str(choice.get())
        
		#label.config(text = selection,font=('Arial',15)
    
	global cwindow
	cwindow = tk.Tk()
	cwindow.geometry('600x270')
	cwindow['background']='#ADFF2F' 
    
	cwindow.resizable(0,0)
	cwindow.title('Newspaper Scraper')
    

	#messagebox.showinfo("general information","We are not the Publishers of these newspapers. We only use links of these Newspapers which are available on the social media and other internet platform. If it violates any policy or if anyone has a complaint about it please contact us at: abmm.group@gmail.com") 

	global choice
	choice = tk.IntVar()

	l1 = tk.Label(cwindow, bg='black',fg='red', font=('Arial Black',17), width=60, text='Newspaper Scraper')
	l1.pack()

	l2 = tk.Label(cwindow, bg='black',fg='yellow', font=('Arial',15), width=60, text='Please select your choice')
	l2.pack()	

	R1 = tk.Radiobutton(cwindow,font=('Arial',15), bg='#ADFF2F', text="1. English Newspapers", variable=choice, value=1,command=sel)
	R1.pack( anchor = 'w' )

	R2 = tk.Radiobutton(cwindow,font=('Arial',15), bg='#ADFF2F', text="2. Hindi Newspapers", variable=choice, value=2,command=sel)
	R2.pack( anchor = 'w' )

    
    
   
   
	#R3 = tk.Button(cwindow,font=('Arial Black',10),text="Serach",command=ser,bg="#FF1493",fg="white",highlightcolor="black",borderwidth=5,relief=GROOVE)
	#R3.pack(side=TOP  )
    

	b1 = tk.Button(cwindow,font=('Arial Black',10),bg="#FF1493", fg="white",borderwidth=5,relief=GROOVE,highlightcolor="black",text = "Next",command= lambda: no_of_days(str(choice.get()))) 
	b1.pack(side='right',padx=0,pady=2)

	b2 = tk.Button(cwindow,font=('Arial Black',10), bg="#FF1493",fg="white",borderwidth=5,relief=GROOVE,highlightcolor="black",text = "Close",command=cwindow.destroy)  
	b2.pack(side='left',padx=5,pady=2)
    
   
	cwindow.mainloop()
def news():
        global xwindow
        xwindow = tk.Tk()
        xwindow.geometry('1200x500')
        xwindow.resizable(0,0)
        xwindow['background']='black'
        def callback(url):
            webbrowser.open(url,new=0,autoraise=True)
        client = gnewsclient.NewsClient(
        language=lang.get(), location=loc.get(), topic=top.get(), max_results=5)
        global news_list
        news_list = client.get_news()
        #swindow.destroy()
        global result_title
        result_title = StringVar() 
        #print(lang.get()+"  "+loc.get() + top.get())
        label=Label(xwindow, text="", font=('Calibri 15'),
         bg="black",fg="white")
        label.config(text=""+"\n"+news_list[0]["title"] + "\n" )
        label.pack()
        label.bind("<Button-1>",lambda e:callback(news_list[0]['link']))
        label2=Label(xwindow, text="", font=('Calibri 15'),
         bg="black",fg="white")
        label2.config(text=""+"\n"+news_list[1]["title"] + "\n" )
        label2.pack()
        label2.bind("<Button-1>",lambda e:callback(news_list[1]['link']))
        label3=Label(xwindow, text="", font=('Calibri 15'),
         bg="black",fg="white")
        label3.config(text=""+"\n"+news_list[2]["title"] + "\n" )
        label3.pack()
        label3.bind("<Button-1>",lambda e:callback(news_list[2]['link']))
        label4=Label(xwindow, text="", font=('Calibri 15'),
         bg="black",fg="white")
        label4.config(text=""+"\n"+news_list[3]["title"] + "\n" )
        label4.pack()
        label4.bind("<Button-1>",lambda e:callback(news_list[3]['link']))
        label5=Label(xwindow, text="", font=('Calibri 15'),
         bg="black",fg="white")
        label5.config(text=""+"\n"+news_list[4]["title"] + "\n" )
        label5.pack()
        label5.bind("<Button-1>",lambda e:callback(news_list[4]['link']))
        b1=Button(xwindow,text="Close",fg="white",bg="red",command=xo1,relief=GROOVE,font=('Arial Black',15))
        b1.pack()
        xwindow.mainloop()
def xo1():
    xwindow.destroy()
    swindow.destroy()
    mm.my1()
def ser():

    #global news_list
    global swindow
    swindow = tk.Tk()
    swindow.geometry('600x270')
    swindow['background']='white'

    swindow.resizable(0,0)
    swindow.title('Search')
    global result_title
    result_title = StringVar()
    global result_link
    result_link = StringVar()
    Label(swindow, text="Choose language :", bg="white",font=('Arial Black',10)).grid(row=0, sticky=W)
    Label(swindow, text="Choose Location :", bg="white",font=('Arial Black',10)).grid(row=1, sticky=W)
    Label(swindow, text="Choose Topic :", bg="white",font=('Arial Black',10)).grid(row=2, sticky=W)
    global lang 
    n0=StringVar()
    lang= ttk.Combobox(swindow,width=25,textvariable=n0)
    lang['values']=("english","hindi","marathi","tamil","telugu","bengali")
    lang.grid(row=0, column=1)
 
    global loc
    n=tk.StringVar()
    loc = ttk.Combobox(swindow,width=25,textvariable=n)
    loc['values']=("India","Japan","Tiwan","china","Chile")
    loc.grid(row=1,column=1)
 
    global top
    n2=tk.StringVar()
    top = ttk.Combobox(swindow,width=25,textvariable=n2)
    top['values']=("Sports","Nation","World","Science","Health","Technology","Business","Entertainment")
    top.grid(row=2, column=1)
	    
    
 
# creating a button using the widget
# Button to call the submit function
    Button(swindow, text="Search", command=news, fg="white",bg="#FF1493",relief=GROOVE,font=('Arial Black',15)).grid(row=10,column=1)
    #result_title.set("hello"+"\n"+news_list[0]["title"] + "\n" +news_list[1]["title"] + "\n" + news_list[2]["title"]+"\n")
    Button(swindow,text="Close",fg="white",bg="#FF1493",command=swindow.destroy,relief=GROOVE,font=('Arial Black',15)).grid(row=10,column=15,padx=10,pady=5)
    swindow.mainloop()      
 

def Main_Login():

    root = Tk()
    root.title("Newspaper Scraper - Login/Register")

    Label(root, bg='black',fg='red', font=('Arial Black',15), width=80, text="Welcome to Newspaper Scraper").pack()
    Label(root, bg='black',fg='yellow', font=('Arial Black',12), width=80, text="Please Login to proceed further").pack()

    width = 640
    height = 520
    root.geometry("500x550")
    root['background']='#00FFFF'
    root.resizable(0,0)

    USERNAME = StringVar()
    PASSWORD = StringVar()
    FIRSTNAME = StringVar()
    LASTNAME = StringVar()

    def Database():
        global conn, cursor
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, firstname TEXT, lastname TEXT)")

    def LoginForm():
        global LoginFrame, lbl_result1
        LoginFrame = Frame(root)
        LoginFrame.pack(side=TOP,pady=40,padx=40)
        LoginFrame['background']='#00FFFF'
        lbl_username = Label(LoginFrame, text="Username:",  bg='#00FFFF', font=('Arial Black',15), bd=15)
        lbl_username.grid(row=1,column=1)
        lbl_password = Label(LoginFrame, text="Password:",  bg='#00FFFF', font=('Arial Black',15), bd=15)
        lbl_password.grid(row=2,column=1)
        lbl_result1 = Label(LoginFrame, text="", bg='#00FFFF', font=('Arial',15),bd=15)
        lbl_result1.grid(row=3,column=1, columnspan=2)
        username = Entry(LoginFrame, font=('arial', 15), textvariable=USERNAME, width=15)
        username.grid(row=1, column=2)
        password = Entry(LoginFrame, font=('arial', 15), textvariable=PASSWORD, width=15, show="*")
        password.grid(row=2, column=2)
        btn_login = Button(LoginFrame, text="Login", font=('arial ', 15), width=15,bg="#FF00FF",fg="white" ,command=Login)
        btn_login.grid(row=4,column=1)
        btn_login = Button(LoginFrame, text="Close", font=('arial ', 15), width=15,bg="#FF00FF",fg="white", command=root.destroy)
        btn_login.grid(row=4,column=2)
        lbl_register = Label(LoginFrame, text="Click to Create Account ", fg="#FF0000",  bg='#00FFFF', font=('Arial ',14))
        lbl_register.grid(row=7,column=2, sticky=W)
        lbl_register.bind('<Button-1>', ToggleToRegister)

    def RegisterForm():
        global RegisterFrame, lbl_result2
        RegisterFrame = Frame(root)
        RegisterFrame.pack(side=TOP, pady=40,padx=40)
        RegisterFrame['background']='#ADFF2F'
        lbl_username = Label(RegisterFrame, text="Username:", bg='#ADFF2F', font=('Arial',15), bd=15)
        lbl_username.grid(row=1,column=1)
        lbl_password = Label(RegisterFrame, text="Password:", bg='#ADFF2F', font=('Arial',15), bd=15)
        lbl_password.grid(row=2,column=1)
        lbl_firstname = Label(RegisterFrame, text="Firstname:", bg='#ADFF2F', font=('Arial',15), bd=15)
        lbl_firstname.grid(row=3,column=1)
        lbl_lastname = Label(RegisterFrame, text="Lastname:",  bg='#ADFF2F', font=('Arial',15), bd=15)
        lbl_lastname.grid(row=4,column=1)
        lbl_result2 = Label(RegisterFrame, text="",  bg='#ADFF2F', font=('Arial',15), bd=18)
        lbl_result2.grid(row=5,column=1, columnspan=2)
        username = Entry(RegisterFrame, font=('arial', 15), textvariable=USERNAME, width=15)
        username.grid(row=1, column=2)
        password = Entry(RegisterFrame, font=('arial', 15), textvariable=PASSWORD, width=15, show="*")
        password.grid(row=2, column=2)
        firstname = Entry(RegisterFrame, font=('arial', 15), textvariable=FIRSTNAME, width=15)
        firstname.grid(row=3, column=2)
        lastname = Entry(RegisterFrame, font=('arial', 15), textvariable=LASTNAME, width=15)
        lastname.grid(row=4, column=2)
        btn_login = Button(RegisterFrame, text="Register", font=('arial', 15), width=15, command=Register)
        btn_login.grid(row=6, column=1)
        btn_login = Button(RegisterFrame, text="Close", font=('arial', 15), width=15, command=root.destroy)
        btn_login.grid(row=6, column=2)
        lbl_login = Label(RegisterFrame, text="Login", fg="Blue",  bg='#ADFF2F', font=('Arial',15))
        lbl_login.grid(row=0, sticky=W)
        lbl_login.bind('<Button-1>', ToggleToLogin)


    def ToggleToLogin(event=None):
        RegisterFrame.destroy()
        LoginForm()

    def ToggleToRegister(event=None):
        LoginFrame.destroy()
        RegisterForm()

    def Register():
        Database()
        if USERNAME.get == "" or PASSWORD.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get == "":
            lbl_result2.config(text="Please complete the required field!")
        else:
            cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (USERNAME.get(),))
            if cursor.fetchone() is not None:
                lbl_result2.config(text="Username is already taken")
            else:
                cursor.execute("INSERT INTO `member` (username, password, firstname, lastname) VALUES(?, ?, ?, ?)", (str(USERNAME.get()), str(PASSWORD.get()), str(FIRSTNAME.get()), str(LASTNAME.get())))
                conn.commit()
                USERNAME.set("")
                PASSWORD.set("")
                FIRSTNAME.set("")
                LASTNAME.set("")
                lbl_result2.config(text="Registeration Successful!")
            cursor.close()
            conn.close()
    def Login():
        Database()
        if USERNAME.get == "" or PASSWORD.get() == "":
            lbl_result1.config(text="Please complete the required field!")
        else:
            cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?", (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                lbl_result1.config(text="Login Successful!")
                root.destroy()
                mm.my1()
            else:
                lbl_result1.config(text="Invalid Username or password")
    LoginForm()
    root.mainloop()
def my2():
    choose_lang()
def main():
    lo.nessy()
#calling function Loginform
    Main_Login()

if __name__ == "__main__":
    main()
    
    