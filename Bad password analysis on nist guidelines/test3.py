import pandas as pd
import matplotlib.backends.backend_pdf
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import warnings
from fpdf import FPDF
#import wkhtmltopdf
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
pdf = FPDF()
pdf.add_page()
font_size = 8
pdf.set_font('times','B',size=13)
txt =str(df)
print(txt)
cnt=1
pdf.cell(0, 10, txt='User Having Short Length Password:', ln=cnt ,align="L")
cnt+=1
ct=1
for row in df:
    pdf.cell(0, 10, txt=str(ct)+row, ln=cnt ,align="L")
    cnt+=1
    ct+=1
pdf.add_page()
pdf.output("User_detais.pdf")
