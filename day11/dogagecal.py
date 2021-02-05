# human_year = int(input("Enter the year in humans"))
# dog_age = 0
# for i in range(human_year):
#     if(i==1):
#         dog_age = dog_age + 10.5
#     elif(i==2):
#         dog_age = dog_age + 10.5
#     else:
#         dog_age = dog_age + 4
# print("Dog age is",dog_age)


human_year = int(input("Enter the year in humans"))
if(human_year<0):
    print("Give positive value")
elif(human_year <= 2):
    dog_age = human_year * 10.5
else:
    dog_age = 21 + (human_year - 2) * 4
print("The dog's age in dog's years is",dog_age)