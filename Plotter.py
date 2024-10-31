import numpy as np
import pandas as pd
import chart_studio.plotly as pl
import plotly.offline as po
import cufflinks as cf
import matplotlib.pyplot as plt

pd.options.plotting.backend="plotly"
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
   if plot == 1:
      finalplot = df1.plot(kind='scatter')
   elif plot == 2:
      finalplot = df1.plot(kind='scatter', mode='markers', symbol='x', colorscale='paired')
   elif plot == 3:
      finalplot = df1.plot(kind='bar')
   elif plot == 4:
      finalplot = df1.plot(kind='hist')
   elif plot == 5:
      finalplot = df1.plot(kind='box')
   elif plot == 6:
      finalplot = df1.plot(kind='surface')
   else:
      finalplot = print('Select only between 1 to 7')
   return finalplot


def plotter2(plot):
   col = int(input('Enter the number of columns you want to plot by selecting only 1 , 2 or 3 : '))
   if(col==1):
      colm = input('Enter the column you want to plot by selecting any column from dataframe head')
      if(plot==1):
          finalplot = df1[colm].plot(kind='scatter')
      elif(plot==2):
          finalplot = df1[colm].plot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')
      elif(plot==3):
          finalplot = df1[colm].plot(kind='bar')
      elif(plot==4):
          finalplot = df1[colm].plot(kind='hist')
      elif(plot==5):
          finalplot = df1[colm].plot(kind='box')
      elif(plot==6 or plot==7):
          finalplot = print('Bubble plot and surface plot require more than one column arguments')
      else:
          finalplot = print('Select only between 1 to 7')
   elif(col==2):
      print('Enter the columns you want to plot by selecting from dataframe head')
      x = input('First column')
      y = input('Second column')
      if(plot==1):
          finalplot = df1[[x,y]].plot(kind='scatter')
      elif(plot==2):
          finalplot = df1[[x,y]].plot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')
      elif(plot==3):
          finalplot = df1[[x,y]].plot(kind='bar')
      elif(plot==4):
          finalplot = df1[[x,y]].plot(kind='hist')
      elif(plot==5):
          finalplot = df1[[x,y]].plot(kind='box')
      elif(plot==6):
          finalplot = df1[[x,y]].plot(kind='surface')
      elif(plot==7):
          size = input('Please enter the size column for bubble plot')
          finalplot = df1.plot(kind='bubble' , x=x,y=y,size=size)
      else:
          finalplot = print('Select only between 1 to 7')
   elif(col==3):
      print('Enter the columns you want to plot')
      x=input('First column')
      y=input('Second column')
      z=input('Third column')
      if(plot==1):
          finalplot = df1[[x,y,z]].plot(kind='scatter')
      elif(plot==2):
          finalplot = df1[[x,y,z]].plot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')
      elif(plot==3):
          finalplot = df1[[x,y,z]].plot(kind='bar')
      elif(plot==4):
          finalplot = df1[[x,y,z]].plot(kind='hist')
      elif(plot==5):
          finalplot = df1[[x,y,z]].plot(kind='box')
      elif(plot==6):
          finalplot = df1[[x,y,z]].plot(kind='surface')
      elif(plot==7):
          size = input('Please enter the size column for bubble plot')
          finalplot = df1.plot(kind='bubble' , x=x,y=y,z=z,size=size )
      else:
          finalplot = print('Select only between 1 to 7')
   else:
        finalplot = print('Please enter only 1 , 2 or 3')
   return finalplot


def main(cat):
   if cat == 1:
      print("Select the type of plot you need [Type_1 - 6]")
      print("1 > Line Plot")
      print("2 > Scatter plot")
      print("3 > Bar plot")
      print("4 > Histogram")
      print("5 > Box plot")
      print("6 > surface plot")
      plot = int(input())
      output = plotter(plot)
      plt.show()
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
      plt.show()
   else:
      print("Please enter correct value !")


   
print("Select the type of data you need to plot [ By writing 1,2 or 3]\n1- Random data with 100 rows and 5 colums\n2- Customize dataframe with 5 columns and 4 rows\n3- Upload csv/json/txt file")
data = int(input())
df1 = createdata(data)
print("DataFrame head is below, check all the columns for further process and ploting.","\n",df1.head())

print("What kind of plot you need ?")
print(" Press 1 -- Plotting all columns","\n","Press 2 -- Specifing columns to plot : ")
cat = int(input(">> "))
main(cat)
