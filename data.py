#data.py
import pandas as pd
expense=[]
item=[]
category=[]
date=[]
def data():
   
   c=int(input("Enter Expense amount:"))
   i=input("Enter item description:")
   print("Enter category :" )
   print(" Enter 1 for food")
   print(" Enter 2 for utilities")
   print(" Enter 3 for transport")
   print(" Enter 4 for miscellaneous")
   t=int(input("=>"))
   if (t==1):
     t='food'
   elif (t==2):
     t='utilities'
   elif (t==3):
     t='transport'
   elif (t==4):
     t='miscellaneous'
   yyyy,mm,dd=map(int,input("Enter date(yyyy mm dd):").split())
   da=yyyy
   expense.append(c)
   category.append(t)
   date.append(da)
   item.append(i)
h=input("Do you want to add entry ? (y/n):")

while (h=='y'):

  data()
  h=input("Do you want to add entry ? (y/n):")
data=list(zip( expense , item , category , date ))
df=pd.DataFrame(data,
                  columns=[' Expense Amount ', ' Item     Description ',' Category ',' Date '])
print(df)
