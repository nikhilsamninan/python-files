def name(a):
    if(len(a)%2==0):
        return("even")
    else:
        return(a[0])


a=['nova','sreerag','orange','apple']     
# name(a)       
print(list(map(name,a)))