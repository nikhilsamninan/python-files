def word(a):
    s = a.split()
    print(s)
    if(s[0][0] == s[1][0]):
        print("True")
    else:
        print("False")

a = input("enter the string")
word(a)
