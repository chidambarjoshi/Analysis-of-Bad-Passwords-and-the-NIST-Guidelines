from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
import csv
import warnings
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re

root = Tk()
def check (*args):
    try:
        warnings.filterwarnings("ignore")
        uname=username.get()
        emailid=email.get()
        passw=password.get()
        email1='chidambar.joshigmail.com'
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if(re.search(regex,email1)==False):
            
            
            print(uname)
        print(uname)
        
        pass_very(uname,emailid,passw)
           
    except ValueError:
        pass
def send_mail(uname,emailid,passw,Status):
    #print(hi)
    try:
        mail_content=""
        sender_address = '17p2848@math.git.edu'
        sender_pass = '99631@git'
        receiver_address = emailid
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Password verification'
        if(Status=="Bad password"):
            mail_content = '''Hello,%s
your password %s, is Bad password please change its as soon as possible
your password must contain 8 charecters and it shoud be alphanumric. 

Thank You

sent by
passwordcheckingsystem

'''%(uname,passw)
            print(mail_content)
        if(Status=="Good Password"):
        
            mail_content = '''Hello,%s
your password %s, is Stong password ...
change the password frequently. 

Thank You

sent by
passwordcheckingsystem

'''%(uname,passw)
            print(mail_content)        
        message.attach(MIMEText(mail_content, 'plain'))
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        msg='''Detected : %s 
        check your email for further instructions'''%(Status)
        messagebox.showinfo("MESSAGE",msg)
    except :
        msg='''Detected : %s 
        Could not send Email
        check network connection '''%(Status)
        messagebox.showinfo("MESSAGE",msg)
        #messagebox.showinfo("MESSAGE","Could not connect to server - is it down? ")
        #print("Could not connect to server - is it down? ")

def pass_very (uname,emailid,passw):
    #users = pd.read_csv('datasets/userscheck.csv', index_col='user_name')
    common_passwords = pd.read_csv('datasets/10_million_password_list_top_10000.txt', header=None, squeeze=True)
    data = [[uname,str(passw)]]
    users = pd.DataFrame(data,columns=['user_name','password'])
    common_passwords = pd.read_csv('datasets/10_million_password_list_top_10000.txt', header=None, squeeze=True)
    Status="null"
    users['length'] = users['password'].str.len()
    users['too_short'] = users['length']<8
    users['common_password'] = users['password'].isin(common_passwords)
    words = pd.read_csv('datasets/google-10000-english.txt', header=None, squeeze=True)
    users['common_word'] = users['password'].str.lower().isin(words)
    users['first_name'] = users['user_name'].str.extract(r'(^\w+)', expand=False)
    users['last_name'] = users['user_name'].str.extract(r'(\w+$)', expand=False)
    users['uses_name'] = (users['first_name'].str.lower() == users['password']) | ((users['last_name']).str.lower()== users['password'])
    users['too_many_repeats'] = users['password'].str.contains(pat=r'(.)\1\1\1')
    users['bad_password'] = ((users['too_short'])|(users['common_password'])|(users['common_word'])|(users['uses_name'])|(users['too_many_repeats']))
    if(users['bad_password'].any(axis=0)==True):
        
        Status="Bad password"
        print(Status)
        
    else :
        Status="Good Password"
        #messagebox.showinfo("MESSAGE", "Good password Detected check your Mail")
    send_mail(uname,emailid,passw,Status)
    

root.title("Password Checking")
mainframe = ttk.Frame(root, padding="3 3 12 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

username=StringVar()
email =StringVar()
password=StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=username)
ttk.Label(mainframe, text="User Name").grid(column=1, row=1, sticky=W)
feet_entry.grid(column=2, row=1, sticky=(W, E))

feet_entry = ttk.Entry(mainframe, width=7, textvariable=email)
ttk.Label(mainframe, text="Email ID").grid(column=1, row=2, sticky=W)
feet_entry.grid(column=2, row=2, sticky=(W, E))

feet_entry = ttk.Entry(mainframe, width=7, textvariable=password,show="*")
ttk.Label(mainframe, text="Password").grid(column=1, row=3, sticky=W)
feet_entry.grid(column=2, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Check Password", command=check).grid(column=2, row=4, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.mainloop()
