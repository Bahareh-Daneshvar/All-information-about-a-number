import math
number=int(input("This program shows you the information of numbers.\nPlease enter an integer number:  "))
sumdevisor=0    
prime=False
perfect=False
primetest=False
numdigit=0
sumdigit=0
wholesum=0
evensum=0
oddsum=0
sum1=0
if number<0:
  number*=-1
  n=number
  n1=number
  n2=number
else:
  n=number 
  n1=number
  n2=number
#Prime or not
if number>1:
 for i in range(2,number):
  if(number%i==0):
   primetest=True
   prime=False
   break
  else:
   prime=True
#Perfect or not
for i in range(1,number):
 if(number%i==0):
   sumdevisor+=i
   if number==sumdevisor:
        perfect=True
   else:
        perfect=False
#The number of digits and sum of digits
while number>0:
    r=number%10
    sumdigit+=r
    number=number//10
    numdigit+=1
#The sum of numbers from 1 to number
for j in range (1,n+1):
  wholesum+=j
#The sum of even and odd digits of numbers
if n==0:
  evensum=0
  oddsum=0
else: 
     while n>0:
       digit = n % 10
       n = n//10
       if digit == 1 or digit == 3 or digit == 5 or digit == 7 or digit == 9:
            oddsum+=digit
       else:
            evensum+=digit
#Palindrom or not
temp=n1    
while n1>0:    
  r=n1%10    
  sum1=(sum1*10)+r    
  n1=n1//10   
if(temp==sum1):    
  palindrome=True    
else:   
  palindrome=False 
#The last digit is zero or not
if n2%5==0 and n2%2==0:
    Lastdigit0=True
else:
     Lastdigit0=False
print("*** information about the number you enterd ***\nThis number is: ") 
print("Prime") if prime==True else print("Not Prime")
print("Perfect") if perfect==True else print("Not Perfect")
print("Palindrom") if palindrome==True else print("Not Palindrom")
print("The last digit of this number is zero") if Lastdigit0==True else print("The last digit of this number is not zero")
print("The number of its digits: ",numdigit)    
print("The total of its digits: ",sumdigit)    
print("The total numbers from 1 to this number is: ",wholesum)    
print("The total of even digits of this number is: ",evensum)
print("The total of odd digits of this number is: ",oddsum)



        
      

 
    
   

    
