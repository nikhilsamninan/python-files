# using filter
def even(a):
    return(a%2==0)
        # print("It is even")
  


a=[1,2,3,4,5,6]
print(list(filter(even,a)))


#using lambda
li = list(range(1,100))
print(list(filter(lambda even:even % 2==0,li)))
