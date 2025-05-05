new project client on react frontend and server side python django frame work employee management application with testimonials , feedback ,api and admin control and register
change_password ,configuration with admin 
create client--
create react project in client
npm uninstall -g create-react-app
npx create-react-app app 
cd app 
npm install axios react-router-dom
npm install react-bootstrap bootstrap table 
 or npm install react-bootstrap table 
npm i react-toastify
in app.js
import { ToastContainer, toast } from 'react-toastify';


npm start

djmyapp -> 


pip install django-cors-headers

in settings 

import os 
MEDIA_URL="/media/"
MEDIA_ROOT= os.path.join(BASE_DIR,'media')

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React frontend URL
]
----------------------
feed back and testimonials and 

ALL TABLE'S ARE 

 also CRUD  by admin pannel 

# Data tranfer from excel file into django_db.sqlite-3

pip install pandas openpyxl
in py shell->
import pandas as pd
from emp.models import Emp 
df= pd.read_csv('E:emp_db.csv')   
#To avoid duplicates, you can add .get_or_create() or .update_or_create() instead of .create().
for  _, row in df.iterrows():
...     Emp.objects.create(name=row['name'],phone=row['phone'],address=row['address'],sallary=row['sallary'],email=row['email'],department=row['department'])
#(if file in same directory)
>>> df=pd.read_csv('/emp_db.csv') 
>>> print(df)