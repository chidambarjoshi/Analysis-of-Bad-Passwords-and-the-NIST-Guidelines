from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
import csv
import warnings
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email_validator import validate_email, EmailNotValidError

root = Tk()
def exit_btt(*args):
    root.destroy()
def check (*args):
    try:
        warnings.filterwarnings("ignore")
        uname=username.get()
        emailid=email.get()
        passw=password.get()
        try:
            if(uname==""):                
                messagebox.showinfo("MESSAGE","Enter UserName")
                username.delete(first=0,last=100)
                emailtx.delete(first=0,last=100)
                pass1.delete(first=0,last=100)
            elif(passw==""):                
                messagebox.showinfo("MESSAGE","Enter Password")
                username.delete(first=0,last=100)
                emailtx.delete(first=0,last=100)
                pass1.delete(first=0,last=100)
            elif(emailid==""):                
                messagebox.showinfo("MESSAGE","Enter EmailID")
                username.delete(first=0,last=100)
                emailtx.delete(first=0,last=100)
                pass1.delete(first=0,last=100)
            
            else:
                
                v = validate_email(emailid)
                print("Valid Email ")
                pass_very(uname,emailid,passw)
        
        except EmailNotValidError as e:
            messagebox.showinfo("MESSAGE","Email id is not valid")
            username.delete(first=0,last=100)
            emailtx.delete(first=0,last=100)
            pass1.delete(first=0,last=100)
         
           
    except ValueError:
        pass
def send_mail(uname,emailid,passw,Status):
    #print(hi)
    try:
        mail_content=""
        sender_address = '17p2848@math.git.edu'
        sender_pass = 'Chidu@123'
        receiver_address = emailid
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Password Verification'
        if(Status=="Bad password"):
            mail_content = '''Hello,%s
your password %s, is Bad password please change your Password
your Should include the following :
1.Password should have more than 8 character
2.Password should not have Common Password
3.Password should not have Common Words
4.Password should not include your User_Name
5.password should not include Repitative character



Thank You

sent by
passwordcheckingsystem

'''%(uname,passw)
           # print(mail_content)
        if(Status=="Good Password"):
        
            mail_content = '''Hello,%s
your password %s, is Stong password ...
Change your Password Frequently, which makes your account be more secure 

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
        username.delete(first=0,last=100)
        emailtx.delete(first=0,last=100)
        pass1.delete(first=0,last=100)
        username.focus()
    except :
        msg='''Detected : %s 
        Could not send Email
        check network connection '''%(Status)
        messagebox.showinfo("MESSAGE",msg)
        username.delete(first=0,last=100)
        emailtx.delete(first=0,last=100)
        pass1.delete(first=0,last=100)
        username.focus()
        
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

username = ttk.Entry(mainframe, width=15, textvariable=username)
ttk.Label(mainframe, text="User Name").grid(column=1, row=1, sticky=W)
username.grid(column=2, row=1, sticky=(W, E))

emailtx= ttk.Entry(mainframe, width=15, textvariable=email)
ttk.Label(mainframe, text="Email ID").grid(column=1, row=2, sticky=W)
emailtx.grid(column=2, row=2, sticky=(W, E))

pass1 = ttk.Entry(mainframe, width=15, textvariable=password,show="*")
ttk.Label(mainframe, text="Password" ).grid(column=1, row=3, sticky=W)
pass1.grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Exit", command=exit_btt).grid(column=1, row=4, sticky=W)
ttk.Button(mainframe, text="Check Password", command=check).grid(column=2, row=4, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.mainloop()
