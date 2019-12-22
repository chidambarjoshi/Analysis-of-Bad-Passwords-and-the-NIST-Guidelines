import pandas as pd
import matplotlib.backends.backend_pdf
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import warnings
from fpdf import FPDF
import glob
from PyPDF2 import PdfFileWriter, PdfFileReader
users = pd.read_csv('datasets/users.csv')
#print("Dataset shape  :",users.shape)
warnings.filterwarnings("ignore")
total_data=982
common_passwords = pd.read_csv('datasets/10_million_password_list_top_10000.txt', header=None, squeeze=True)
users['length'] = users['password'].str.len()
users['too_short'] = users['length']<8
#print("Number of users using Short length password ",sum(users['too_short']))
df=users[users['too_short']==True]['user_name'].head(25)
#print(df)
too_short=sum(users['too_short'])
pdf = FPDF()
pdf.add_page()
font_size = 8
pdf.set_font('times','B',size=18)
txt =str(df)
#print(txt)
cnt=1
pdf.cell(0, 10, txt='User Details', ln=cnt ,align="C")
cnt+=1
pdf.set_font('times','B',size=14)
pdf.cell(0, 10, txt='User Having Short Length Password:', ln=cnt ,align="L")
pdf.set_font('times',size=10)
cnt+=1
ct=1
for row in df:
    pdf.cell(0, 5, txt=str(ct)+' '+row, ln=cnt ,align="L")
    cnt+=1
    ct+=1
pdf.add_page()




users['common_password'] = users['password'].isin(common_passwords)
#print("Number of users Having Common Passwords "+str(sum(users['common_password'])))
common_password=sum(users['common_password'])
df=users[users['common_password']==True]['user_name']
print(df.head(25))
pdf.set_font('times','B',size=14)
pdf.cell(0, 10, txt='User Having Common Passwords as their Password:', ln=cnt ,align="L")
cnt+=1
pdf.set_font('times',size=10)
ct=1
for row in df:
    pdf.cell(0, 5, txt=str(ct)+row, ln=cnt ,align="L")
    cnt+=1
    ct+=1
pdf.add_page()

words = pd.read_csv('datasets/google-10000-english.txt', header=None, squeeze=True)
users['common_word'] = users['password'].str.lower().isin(words)
#print("Number of users Containing Common Words in their Passwords   :"+str(sum(users['common_word'])))
common_word=sum(users['common_word'])
df=users[users['common_word']==True]['user_name'].head(25)
pdf.set_font('times','B',size=14)
pdf.cell(0, 10, txt='User Having Common Words as their Password:', ln=cnt ,align="L")
cnt+=1
pdf.set_font('times',size=10)
ct=1
for row in df:
    pdf.cell(0, 5, txt=str(ct)+row, ln=cnt ,align="L")
    cnt+=1
    ct+=1
pdf.add_page()


users['first_name'] = users['user_name'].str.extract(r'(^\w+)', expand=False)
users['last_name'] = users['user_name'].str.extract(r'(\w+$)', expand=False)
users['uses_name'] = (users['first_name'].str.lower() == users['password']) | ((users['last_name']).str.lower()== users['password'])
#print("Number of users Containing  User Name as their Password   :"+str(sum(users['uses_name'])))
uses_name=sum(users['uses_name'])
df=users[users['uses_name']==True]['user_name'].head(25)
pdf.set_font('times','B',size=14)
pdf.cell(0, 10, txt='User Containing  User Name as their Password:', ln=cnt ,align="L")
cnt+=1
pdf.set_font('times',size=10)
ct=1
for row in df:
    pdf.cell(0, 5, txt=str(ct)+row, ln=cnt ,align="L")
    cnt+=1
    ct+=1
pdf.add_page()



users['too_many_repeats'] = users['password'].str.contains(r'(.)\1\1\1')
#print(users[users['too_many_repeats']==True])
#print("Number of users  having Repetative  Passwords     :"+str(sum(users['too_many_repeats'])))
too_many_repeat=sum(users['too_many_repeats'])
df=users[users['too_many_repeats']==True]['user_name']
pdf.set_font('times','B',size=14)
pdf.cell(0, 10, txt='User Containing  Repetative Characters as their Password:', ln=cnt ,align="L")
cnt+=1
pdf.set_font('times',size=10)
ct=1
for row in df:
    pdf.cell(0, 5, txt=str(ct)+row, ln=cnt ,align="L")
    cnt+=1
    ct+=1
pdf.add_page()




users['bad_password'] = ((users['too_short'])|(users['common_password'])|(users['common_word'])|(users['uses_name'])|(users['too_many_repeats']))
#print("Number of Users having Bad Passwords     :"+str(sum(users['bad_password'])))
df=users[users['uses_name']==True]['user_name'].head(25)
bad_password=sum(users['bad_password'])
pdf.set_font('times',size=14)
pdf.cell(0, 10, txt='User BAD Password:', ln=cnt ,align="L")
cnt+=1
pdf.set_font('times',size=10)
ct=1
for row in df:
    pdf.cell(0, 5, txt=str(ct)+row, ln=cnt ,align="L")
    cnt+=1
    ct+=1

objects = ('too_many_repeat', 'uses_name',' common_word', 'common_password',' too_short','total_data' )
x_pos = np.arange(len(objects))
performance = [too_many_repeat, uses_name, common_word, common_password, too_short,total_data]
pdf.add_page()
pdf.output("User_List.pdf")

#Ploting maps:


#plot too short
out_pdf = r'User_detais.pdf'

pdf = matplotlib.backends.backend_pdf.PdfPages(out_pdf)
fig = plt.figure()

cnt=321
plt.subplot(cnt)
fig = plt.figure(figsize=(8, 8))
labels = 'Too_Short', 'Total_Users'
total1=total_data-too_short
sizes = [too_short, total1 ]
colors = ['gold', 'yellowgreen']
plt.pie(sizes,  labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title("Number of Users Having Short Password", bbox={'facecolor':'0.8', 'pad':5})
#plt.show()

cnt+=1
plt.rcParams.update({'font.size': 8})
pdf.savefig(fig)

plt.subplot(cnt)
fig = plt.figure(figsize=(8, 8))
labels = 'Common_Password', 'Total_Users'
total2=total_data-common_password
sizes = [common_password, total2 ]
colors = ['gold', 'yellowgreen']
plt.pie(sizes,  labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title("Number of Users Having Common Password", bbox={'facecolor':'0.8', 'pad':5})
#plt.show()
cnt+=1
plt.rcParams.update({'font.size': 8})
pdf.savefig(fig)

plt.subplot(cnt)
fig = plt.figure(figsize=(8, 8))
labels = 'Common_Word', 'Total_Users'
total3=total_data-common_word
sizes = [common_word, total3 ]
colors = ['gold', 'yellowgreen']
plt.pie(sizes,  labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title("Number of Users having Common Words in their Password", bbox={'facecolor':'0.8', 'pad':5})
#plt.show()
cnt+=1
plt.rcParams.update({'font.size': 8})
pdf.savefig(fig)




plt.subplot(cnt)
fig = plt.figure(figsize=(8, 8))
labels = 'Uses_Name', 'Total_Users'
total4=total_data-uses_name
sizes = [uses_name, total4 ]
colors = ['gold', 'yellowgreen']
plt.pie(sizes,  labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title("Number of users having Common Words in their Password", bbox={'facecolor':'0.8', 'pad':5})
#plt.show()
cnt+=1
plt.rcParams.update({'font.size': 8})
pdf.savefig(fig)



plt.subplot(cnt)
fig = plt.figure(figsize=(8, 8))
labels = 'too_many_repeats', 'Total_Users'
total5=total_data-too_many_repeat
sizes = [too_many_repeat, total5 ]
colors = ['gold', 'yellowgreen']
plt.pie(sizes,  labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title("Number of users having repetative words in their Password", bbox={'facecolor':'0.8', 'pad':5})
plt.tight_layout()
#plt.show()
cnt+=1
plt.rcParams.update({'font.size': 8})
pdf.savefig(fig)
plt.subplot(cnt)
fig = plt.figure(figsize=(8, 8))
plt.barh(x_pos, performance, align='center', alpha=0.5)
plt.yticks(x_pos, objects)
plt.xlabel('Number Of users')
plt.title('Users Having Bad passwords In Diffrent Ways')
cnt+=1
plt.rcParams.update({'font.size': 8})
pdf.savefig(fig)
pdf.close()
#plt.show()


pdf_writer = PdfFileWriter()
paths = glob.glob('User*.pdf')
paths.sort()
output_path=r'User_List_grapic.pdf'
for path in paths:
    
    pdf_reader = PdfFileReader(path)
    for page in range(pdf_reader.getNumPages()):
        
        pdf_writer.addPage(pdf_reader.getPage(page))
 
with open(output_path, 'wb') as fh:
    pdf_writer.write(fh)


