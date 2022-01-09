import math, time

#problem1
def count_evens(L):
    count = 0
    for i in L:
        if (i%2 == 0):
            count+=1
    
    return count

#problem2
def list_to_str(lis):
    val = ""
    val += "[" + str(lis[0])
    
    for i in range(len(lis) - 1):
       val += ", " + str(lis[i+1])

    val += "]"
    
    return val

#problem3
def lists_are_the_same(list1, list2):
    val = True

    if (len(list1) != len(list2)):
        print("Lists are not the same length:")
        return not val
    else:
        i = 0      
        while(val and i < len(list1)):
            if (list1[i] != list2[i]):
                val = not val #return False using a for loop
            i += 1
        return val
        
#problem4
def gcd(n,m):
    rem = 0
    while (n != 0 and m != 0):
        if (n < m):
            n,m=m,n
        rem = n % m #note that rem is guaranteed to be smaller than m
        n = rem
    
    if (n == 0):
        return m
    else:
        return n

def rec_gcd(n,m): #recursive formula
    if (m == 0):
        return n
    else:
        return rec_gcd(m, n % m) #note if n < m, this line basically switches n and m

def simplify_fraction(n,m):
    num = gcd(n,m)
    return str(int(n/num)) + "/" + str(int(m/num))

#problem5
def how_many(n):
    counter = 0
    check = True
    val = 0

    while(check):
        val += (-1)**counter/(2*counter + 1)

        if (math.floor(math.pi*(10**(n-1))) == math.floor(4*val*(10**(n-1)))):
            check = not check
        else:
            counter += 1

    return counter

#problem6
def naive_algorithm(n,m):
    min = n
    if (m < n):
        min = m
    N,M = n,m
    num = 1
    
    for i in range(min - 1):
        check = True
        while(check):
            if (N%(min - i) == 0 and M%(min - i) == 0):
                num *= (min - i)
                N /= (min - i)
                M /= (min - i)
            else:
                check = not check

    return str(int(n/num)) + "/" + str(int(m/num))

def another_algorithm(n,m):
    if (n < m):
        n,m=m,n
    N,M = n,m
    gcd = 1

    for i in range(m - 1):
        if (N % (m - 1 - i) == 0 and M % (m - 1 - i) == 0):
            N /= (m - 1 - i)
            M /= (m - 1 - i)
            gcd *= (m - 1 - i)
    
    return gcd

if __name__ == "__main__":
    L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

    print(rec_gcd(61776000000000, 257400))
    print(gcd(61776000000000, 257400))

    print(count_evens(L))
    print(list_to_str(L))

    print(how_many(7))

    start = time.time()
    print("simplify_fraction",simplify_fraction(61776000000000, 257400))
    middle = time.time()
    print("naive_algorithm",naive_algorithm(61776000000000, 257400))
    end = time.time()
    print("another_algorithm",another_algorithm(61776000000000, 257400))

    print("Time for simplify_fraction:", middle - start)
    print("Time for naive_algorithm:", end - middle)
    print("simplify_fraction is",(end - middle)/(middle - start),"times faster than naive_algorithm.")