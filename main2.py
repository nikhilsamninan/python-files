import random
a=int(input("Enter the lower Bound"))
b=int(input("Enter the upper Bound"))
k=random.randint(a,b)
s=int(input("Enter the Guess"))
guess_lt=9
guess_count=0
while(guess_count<guess_lt):
    if(s<a or s>b):
        print("you are out of the limit")
        print("Do you want to continue or not")
    elif(k+5<s or s<k-5):
        print("Try Again you are near")
    elif(s<=k-5):
        print("Too Small")
    elif(s>=k+5):
        print("Too High")
    else:
        print("Congrats You Win The Game")


elif(k<s+5 or k<s-5):
        print("Try Again you are near")


        elif(k>s-5):
        print("Too small")
elif(k<s+5):
        print("Too high")