import numpy as np
import pandas as pd
import chart_studio.plotly as pl
import plotly.offline as po
import cufflinks as cf

po.init_notebook_mode(connected = True)
cf.go_offline()

def createdata(data):
   if data == 1:
      x = np.random.rand(100,5)
      df1 = pd.DataFrame(x,columns=['A','B','C','D','E'])
   elif data == 2:
      x  = [0,0,0,0,0]
      r1  = [0,0,0,0,0]
      r2  = [0,0,0,0,0]
      r3  = [0,0,0,0,0]
      r4  = [0,0,0,0,0]
      print("Enter values for columns ")
      i = 0 
      for i in [0,1,2,3,4]:
          x[i] = input(">> ")
          i = i + 1
      print("Enter values for first row ")
      i = 0
      for i in [0,1,2,3,4]:
         r1[i] = int(input(">> "))
         i += 1
      print("Enter values for second row ")
      i = 0
      for i in [0,1,2,3,4]:
         r2[i] = int(input(">> "))
         i += 1
      print("Enter values for third row ")
      i = 0
      for i in [0,1,2,3,4]:
         r3[i] = int(input(">> "))
         i += 1
      print("Enter values for fourth row ")
      i = 0
      for i in [0,1,2,3,4]:
         r4[i] = int(input(">> "))
         i += 1
      df1 = pd.DataFrame([r1,r2,r3,r4], columns= x)
   elif(data == 3):
      file = input("Enter file's name: ")
      x = pd.read_csv(file)
      df1 = pd.DataFrame(x)
   else:
      print("Input Error ! Try again")
   return df1


def plotter(plot):
   pass


def plotter2(plot):
   pass


def main(cat):
   if cat == 1:
      print("Select the type of plot you need [Type_1 - 6] :")
      print("1 > Line Plot")
      print("2 > Scatter plot")
      print("3 > Bar plot")
      print("4 > Histogram")
      print("5 > Box plot")
      print("6 > surface plot")
      plot = int(input())
      output = plotter(plot)
   elif cat ==2:
      print("Select the type of plot you need [Type_1 - 7] :")
      print("1 > Line Plot")
      print("2 > Scatter plot")
      print("3 > Bar plot")
      print("4 > Histogram")
      print("5 > Box plot")
      print("6 > surface plot")
      print("7 > Bubble plot")
      plot = int(input())
      output = plotter2(plot)
   else:
      print("Please enter correct value !")


   
print("Select the type of data you need to plot [ By writing 1,2 or 3]\n1- Random data with 100 rows and 5 colums\n2- Customize dataframe with 5 columns and 4 rows\n3- Upload csv/json/txt file")
data = int(input())
df1 = createdata(data)
print("DataFrame head is below, check all the columns for further process and ploting.","\n",df1.head())

print("What kind of plot you need ?")
cat = int(input("Press '1' -- Plotting all columns","\n","Press '2' -- Specifing columns to plot"))
