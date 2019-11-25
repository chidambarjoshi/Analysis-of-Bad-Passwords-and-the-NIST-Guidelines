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


words = pd.read_csv('datasets/google-10000-english.txt', header=None, squeeze=True)
users['common_word'] = users['password'].str.lower().isin(words)
print("Number of users Containing Common Words in their Passwords   :"+str(sum(users['common_word'])))
common_word=sum(users['common_word'])
users[users['common_word']==True]['user_name'].head(25)


users['first_name'] = users['user_name'].str.extract(r'(^\w+)', expand=False)
users['last_name'] = users['user_name'].str.extract(r'(\w+$)', expand=False)
users['uses_name'] = (users['first_name'].str.lower() == users['password']) | ((users['last_name']).str.lower()== users['password'])
print("Number of users Containing  User Name as their Password   :"+str(sum(users['uses_name'])))
uses_name=sum(users['uses_name'])
users[users['uses_name']==True]['user_name'].head(25)



users['too_many_repeats'] = users['password'].str.contains(r'(.)\1\1\1')
#print(users[users['too_many_repeats']==True])
print("Number of users  having Repetative  Passwords     :"+str(sum(users['too_many_repeats'])))
too_many_repeat=sum(users['too_many_repeats'])
users[users['too_many_repeats']==True]['user_name']




users['bad_password'] = ((users['too_short'])|(users['common_password'])|(users['common_word'])|(users['uses_name'])|(users['too_many_repeats']))
print("Number of Users having Bad Passwords     :"+str(sum(users['bad_password'])))
users[users['uses_name']==True]['user_name'].head(25)
bad_password=sum(users['bad_password'])

objects = ('too_many_repeat', 'uses_name',' common_word', 'common_password',' too_short','total_data' )
x_pos = np.arange(len(objects))
performance = [too_many_repeat, uses_name, common_word, common_password, too_short,total_data]



#Ploting maps:


#plot too short
out_pdf = r'OUTPUT.pdf'

pdf = matplotlib.backends.backend_pdf.PdfPages(out_pdf)
fig = plt.figure()

cnt=321
plt.subplot(cnt)
fig = plt.figure(figsize=(5, 5))
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
fig = plt.figure(figsize=(5, 5))
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
fig = plt.figure(figsize=(5, 5))
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
fig = plt.figure(figsize=(5, 5))
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
fig = plt.figure(figsize=(5, 5))
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
fig = plt.figure(figsize=(5, 5))
plt.barh(x_pos, performance, align='center', alpha=0.5)
plt.yticks(x_pos, objects)
plt.xlabel('Number Of users')
plt.title('Users Having Bad passwords In Diffrent Ways')
cnt+=1
plt.rcParams.update({'font.size': 8})
pdf.savefig(fig)
pdf.close()
#plt.show()
