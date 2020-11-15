#squares all numbers provided in input data set and gives output, using for loop
def square(lst):
    for idx in range(len(lst)):
        lst[idx] = lst[idx]**2
    return lst

#importing math module to display the value of pi
#others include sin, sinh, sqrt, tan, tau, trunc, values
import math
print("The approximation for the value of pi is",math.pi)

#Class that calculates the inverse of the sum of two numbers
class Advanced(Simple):
  def Inverse(self,x,y):
    return (1/Simple.Add(self,x,y))

#Converts currency based on exchange rate
def Calc(currency,*rates):
  for i in rates:
    print(currency*i)
    
#Script that prints 3
a=1
b=2
def func():
    global b
    b=a+b
func()
print(b)

#class called Person that has parameters in the initialize function called name, age, and sex
class Person:
  def __initialize__(self, name, age, sex):
    self.name = name
    self.age = age
    self.sex = sex
    
#Script that prints 4
def inc(a,b=1):
    return(a+b)
a=inc(1)
a=inc(a,a)
print(a)

#set the annual payment in one function and print the respective monthly payment in a separate function
def SetAnnual():
  global annual
  annual=1000
def PrintMonthly():
  print("Your monthly payment is "+str(annual/12)+" USD.")
SetAnnual()
PrintMonthly()

#prints number of digits based on number
def main():
    number=31
    if (number>=1000):
      print(4)
    elif (number>=100):
      print(3)
    elif (number>=10):
      print(2)
    else:
      print(1)

#Returns the sum of the first item in the data list and every tenth item after
def Sum10th(data):
  sum=0
  for i,d in enumerate(data):
    if (i % 10 == 0): sum=sum+d
  return sum

#displays current date and time in console
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#outputs last name, first name for input first name and last name in console
firstname=input("Enter your first name")
lastname=input("Enter your last name")
print(lastname,firstname)

#generate a list and tuple with comma-separated numbers
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

#Prints the extension of a file name (e.g. abc.java, prints java)
filename=input("Filename: ")
filetype=filename.split(".")
print("The file type is",filetype[-1])

#Displays first and last color from provided list
colors=input("Type in comma separated colors")
colorterms=colors.split(",")
print(colorterms[0],colorterms[-1])
#alternatively:
exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)

#Prints the sum of the square, cube, and initial number of input
a=input("Type in a number: ")
numone=int(a)
numtwo=int(a)*int(a)
numthree=int(a)*int(a)*int(a)
print(numone+numtwo+numthree)

#Returns the absolute value of an inputted number
num=input("Type a number: ")
absnum=abs(int(num))
print(absnum)

#display current time
import calendar
from datetime import date
from datetime import time
from datetime import datetime
def main():
    t=datetime.time(datetime.now())
    print(t)
#display current date
def main():
    today=date.today()
    print("Today's date is ",today)
#display individual components of today's date--day, month, and year
    print("Date components: ", today.day,today.month,today.year)

#Print calendar of a given month and year
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

#Multiline string with " in middle
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

#finds the number of days between 2 dates
from datetime import date
f_date = date(2020, 6, 3)
l_date = date(2020, 7, 11)
delta = l_date - f_date
print(delta.days)

#volume of a sphere of area r
import math
def volumesphere(r):
    volume=r**3*4/3*math.pi
    print("The volume of this sphere of radius ",r,"is ",volume)

#Computes the difference between a number and 17. If number>17, prints double the absolute difference.
def main(a):
    if a<=17:
        print(17-a)
    else:
        print(abs(17-a)*2)
    
def main(a):
    if a<=1100 and a>=1000:
        print("Close to 1000")
    elif a<=2100 and a>=1900:
        print("Close to 2000")
    else:
        print("Not close to either 1000 or 2000")
#Alternatively:
def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))



