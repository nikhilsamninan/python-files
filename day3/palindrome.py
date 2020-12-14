n=int(input("Enter the Number"))
a=n
s=0
while(n>0):
  b= n%10
  s= s*10+b
  n= n//10
if(s==a):
    print("It is palindrome")
else:
    print("it is not palindrome")    
