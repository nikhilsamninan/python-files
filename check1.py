import random
access=False
while access=False:        
a=int(input("Enter the lower Bound"))
b=int(input("Enter the upper Bound"))
k=random.randint(a,b)
print(k)
lt=0

while (lt<9):
        s=(input("Do you Want to continue y/n"))
        y="y"
        n="n"
        if(s==n):
                print("Quit From Game!!!!")
                break
        x=a
        y=b
        while(y==s):
                guess=int(input("Enter the Guess"))
                if(guess==k):
                        print("Congrats you won the game")
                elif(guess<a or guess>b):
                        print("you are out of the limit")
                
                elif(guess+5>=k and guess-5<=k):
                        print("Try Again you are near")  
                elif(guess<=x):
                        print("Hey! Poor Entry Try Again\n Too low")        
                elif(guess<k):
                        print("Too Low",guess)
                        x=int(guess)
                elif(guess>=y):
                        print("Hey! Poor Entry Try Again\n Too high")          
                elif(guess>k):
                        print("Too high",guess) 
                        y=int(guess)
                lt=lt+1  
                
        
                

                
        

   
     
