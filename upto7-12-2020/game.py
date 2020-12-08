import random
access=True
while access:
    g=input("Are you ready to play y/n:\n")
    if(g=="y"):
        a=int(input("Enter the lower Bound"))
        b=int(input("Enter the upper Bound"))
        k=random.randint(a,b)
        print(k)
        lt=0
        x=a
        y=b
        while (lt<9):
            guess=int(input("Enter the Guess"))
            if(guess==k):
                print("Congrats you won the game")
                break
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
            if(lt==9):
                print("you failed")  
        print("PLAY Again!!")        
    elif(g=="n"):
        print("QUIT from the game")
        access= False         
        print("OK Byee")
