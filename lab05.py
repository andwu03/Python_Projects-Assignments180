import numpy

#problem1
def list1_starts_with_list2(list1, list2):
    flag = True
    
    if (len(list1) < len(list2)):
        flag = False

    #flag = list1[:len(list2)] == list2

    counter = 0
    while(flag and counter < len(list2)):
        if (list1[counter] != list2[counter]):
            flag = False
        counter += 1
    
    return flag

#problem2
def match_pattern(list1, list2):
    flag = True
    track = False

    if (len(list1) < len(list2)):
        flag = False
    
    counter1 = 0

    while(flag):
        check = True
        counter2 = 0

        while(check and counter2 < len(list2)):
            if (list1[counter1 + counter2] != list2[counter2]):
                check = False
            counter2 += 1

        if (check):
            flag = False
            track = True 
        counter1 += 1
        if (counter1 == (len(list1) - len(list2) + 1)):
            flag = False

    if (track == True):
        flag = True

    return flag

#problem3
def repeats(list0):
    flag = False
    count = 0

    while(not flag and count < len(list0) - 1):
        if (list0[count] == list0[count + 1]):
            flag = True
        count += 1

    return flag


#problem4a
#Note: this assumes that M is a rectangular list of lists
def print_matrix_dim(M):
    row = len(M)
    col = len(M[0])

    return str(row) + "x" + str(col)

#problem4b
def mult_M_v(M, v):
    row = len(M)
    col = len(M[0])

    for i in range(row):
        for j in range(col):
            M[i][j] = float(M[i][j]*v[j])

#problem4c
def matrix_mult(M,N):

    print("lenM" + str(len(M)))
    if (len(M[0]) != len(N)):
        print("Matrix multiplication is not defined for the dimensions of these two matrices.")
        return

    new = [[0 for x in range(len(M))] for y in range(len(N[0]))]

    a,b = 0,0
    for i in range(len(M)):
        for j in range(len(N[0])):
            for k in range (len(M[0])):
                new[i][j] += M[i][k]*N[k][j]

    return new

if __name__ == "__main__":
    list1 = [[1,2],
             [3,4],
             [5,6]]
    list2 = [[1,2,3],
             [4,5,6]]

    print(matrix_mult(list1, list2))