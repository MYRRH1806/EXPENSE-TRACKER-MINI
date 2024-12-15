# pie chart 
import matplotlib.pyplot as plt
import numpy as np

def pie():
  fig = plt.figure(figsize=(10, 7))
  plt.pie(expense, labels=category)


  plt.show()
ans=input("Do you want to see the pie chart ?(y/n):")
if (ans=='y'):
    print(pie())
print("Thank you and have a nice day !")
  
