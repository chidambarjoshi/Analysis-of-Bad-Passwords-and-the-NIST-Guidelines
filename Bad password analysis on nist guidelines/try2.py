import pandas as pd
import matplotlib.backends.backend_pdf
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import warnings
users = pd.read_csv('datasets/users.csv')
print("Dataset shape  :",users.shape)
warnings.filterwarnings("ignore")
total_data=982
common_passwords = pd.read_csv('datasets/10_million_password_list_top_10000.txt', header=None, squeeze=True)
users['length'] = users['password'].str.len()
users['too_short'] = users['length']<8
print("Number of users using Short length password ",sum(users['too_short']))
df=users[users['too_short']==True]['user_name'].head(25)
print(df)
too_short=sum(users['too_short'])



users['common_password'] = users['password'].isin(common_passwords)
print("Number of users Having Common Passwords "+str(sum(users['common_password'])))
common_password=sum(users['common_password'])
df=users[users['common_password']==True]['user_name']
print(df.head(25))


out_pdf = r'test3.pdf'

pdf = matplotlib.backends.backend_pdf.PdfPages(out_pdf)
fig = plt.figure()

cnt=321
plt.subplot(cnt)
fig = plt.figure(figsize=(10, 10))
labels1 = 'Too_Short', 'Total_Users'
total1=total_data-too_short
sizes = [too_short, total1 ]
colors = ['gold', 'yellowgreen']
plt.pie(sizes,  labels=labels1, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140,radius=0.8)
plt.axis('equal')
plt.title("Number of Users Having Short Password", bbox={'facecolor':'0.8', 'pad':5})
plt.rcParams.update({'font.size': 8})
cnt+=1
pdf.savefig(fig)


plt.subplot(cnt)
fig = plt.figure(figsize=(10, 10))
labels2 = 'Common_Password', 'Total_Users'
total2=total_data-common_password
sizes = [common_password, total2 ]
colors = ['gold', 'yellowgreen']
plt.pie(sizes,  labels=labels2, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title("Number of Users Having Common Password", bbox={'facecolor':'0.8', 'pad':5})
plt.rcParams.update({'font.size': 8})
cnt+=1
pdf.savefig(fig)
pdf.close()
print("done")

#plt.show()



