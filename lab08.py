# import numpy as np

# # Printing matrices using NumPy:

# # Convert a list of lists into an array:
# M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
# M = np.array(M_listoflists)
# # Now print it:
# print(M)

# #Compute M*x for matrix M and vector x by using
# #dot. To do that, we need to obtain arrays
# #M and x
# M = np.array([[1,-2,3],[3,10,1],[1,5,3]])
# x = np.array([75,10,-11])
# b = np.matmul(M,x)        

# print(M)
# #[[ 1 -2  3]
# # [ 3 10  1]
# # [ 1  5  3]]

# # To obtain a list of lists from the array M, we use .tolist()
# M_listoflists = M.tolist() 

# print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]

import numpy as np

def print_matrix(M_lol):
    M = np.array(M_lol)
    print(M)

def get_lead_ind(row):
    for i in range(len(row)):
        if (row[i] != 0):
            return i
    
    return len(row)

def get_row_to_swap(M, start_i):
    max_row = start_i

    for i in range(len(M) - start_i - 1): #4 - 0 - 1 = 3
        if (get_lead_ind(M[start_i + 1 + i]) < get_lead_ind(M[max_row])):
            max_row = start_i + 1 + i

    return max_row
        
def add_rows_coefs(r1, c1, r2, c2):
    M = [0]*len(r1)

    for i in range(len(r1)):
        M[i] = c1*r1[i] + c2*r2[i]

    return M

def eliminate_forward(M, row_to_sub, best_lead_ind):
    new = [0]*len(M[0])
    coeff = 1
    for i in range(len(M) - row_to_sub - 1):
        coeff = -1*M[row_to_sub + i + 1][best_lead_ind]/M[row_to_sub][best_lead_ind]
        new = add_rows_coefs(M[row_to_sub], coeff, M[row_to_sub + i + 1], 1)
        M[row_to_sub + i + 1] = new

def eliminate_backward(M, row_to_sub, best_lead_ind):
    new = [0]*len(M[0])
    coeff = 1
    for i in range(row_to_sub):
        coeff = -1*M[row_to_sub - i - 1][best_lead_ind]/M[row_to_sub][best_lead_ind]
        new = add_rows_coefs(M[row_to_sub], coeff, M[row_to_sub - i - 1], 1)
        M[row_to_sub - i - 1] = new

def forward_step(M):
    for i in range(len(M)):
        swap = get_row_to_swap(M, i)
        print("row to swap",swap)
        M[swap], M[i] = M[i], M[swap] #this swaps the rows

        print("after swap")
        print_matrix(M)

        eliminate_forward(M, i, get_lead_ind(M[i]))

        print("after eliminate")
        print_matrix(M)

def backward_step(M):
    for i in range(len(M)):
        eliminate_backward(M, len(M) - i - 1, get_lead_ind(M[len(M) - i - 1]))

        print("after eliminate")
        print_matrix(M)

    for i in range(len(M)):
        coeff = M[i][get_lead_ind(M[i])]
        new = [0]*len(M[0])
        
        for j in range(len(M[0])):
            new[j] = M[i][j]/coeff
        
        M[i] = new
    
    print("divide leading coeff")
    print_matrix(M)

def augment(M, b):
    new = [[0 for x in range(len(M[0]) + 1)] for y in range(len(M))]

    for i in range(len(M)):
        for j in range(len(M[0])):
            new[i][j] = M[i][j]
        
        new[i][-1] = b[i][0]

    return new

def solve(M, b): #make sure that b is 3 x 1
    augmented = augment(M, b)

    forward_step(augmented)
    backward_step(augmented)

    ans = [[0] for y in range(len(b))] 
    
    for i in range(len(b)):
        ans[i] = augmented[i][-1]

    return ans

def test(M, x):
    array_M = np.array(M)
    array_x = np.array(x)

    return np.matmul(array_M, array_x)

if __name__ == "__main__":
    # M = [[ 1, -2, 3, 22],
    #      [ 3, 10, 1, 314],
    #      [ 1, 5, 3, 92,]]
    # print("forward")
    # forward_step(M)


    # print("backward")
    # backward_step(M)

    M = [[ 2, 3, -5],
         [ 1, -1, 1],
         [ 10, -8, 21]]
    
    b = [[0], [1], [23]]

    print_matrix(augment(M, b))
    
    ans = solve (M, b)

    print_matrix(ans)

    print_matrix(test(M, ans))

    
