def matrix_form():
    r = int(input("Enter the no of rows"))
    c = int(input("Enter the no of columns"))

    matrix=[]
    print("Enter the enteries")

    for i in range(r):
        a = []
        for j in range(c):
            a.append(int(input()))
        matrix.append(a)
    return(matrix)

def check_matrix(first_matrix,sec_matrix):
    if(first_matrix==sec_matrix):
        print("same")
    else:
        print("not same")


print("Enter the 1st matrix")
first_matrix = matrix_form()
print(first_matrix)
print("Enter the 2nd matrix")
sec_matrix = matrix_form()
print(sec_matrix)
check_matrix(first_matrix,sec_matrix)