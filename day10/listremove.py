# a = [1,2,2,3,4,5]
# # print(list(set(a)))
# def correct_list(a):
#     return(list(set(a)))


# print(correct_list(a))
a = [1,2,2,3,4,5]

def correct_list(a):
    s = []
    for i in a:
        if i not in s:
            s.append(i)
    return(s)

print(correct_list(a))