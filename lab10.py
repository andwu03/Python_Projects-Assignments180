import copy

#problem 1
def power(x, n):
    if (n == 0):
        return 1
    return x * power(x, n - 1)

#problem 2
def interleave(L1, L2):
    if (len(L1) == 0):
        return []
    return [L1[0]] + [L2[0]] + interleave(L1[1:], L2[1:])

#problem 3
def reverse_rec(L):
    if (len(L) == 1):
        return L
        
    return [L[len(L) - 1]] + reverse_rec(L[:len(L) - 1]) 

def reverse_rec_no_slice(L):
    if (len(L) == 1):
        return L
    
    new = copy.deepcopy(L)
    new.pop(len(L) - 1)

    return [L[len(L) - 1]] + reverse_rec(new)

#problem 4
def zigzag(L):
    if len(L) == 0:
        print(" ")
    elif len(L) == 1:
        print(L[0], end = " ")
    else:
        zigzag(L[1:-1])
        print(L[0], L[-1], end = " ")

#problem 5
def is_balanced(s):
    cfirst = s.find(")")
    ofirst = s.find("(")
    if (cfirst == -1 and ofirst == -1): #this means that both are not present
        return True
    else:
        if (cfirst != -1):
            open = s[:cfirst].rfind("(")
            if (open != -1):
                return is_balanced(s[:open] + s[cfirst + 1:])
            else:
                return False
        else:
            return False

if __name__ == "__main__":
    # print(power(3,3))
    
    L1 = [1,2,3,4,5]
    # L2 = [6,7,8,9,10]
    # print(interleave(L1, L2))

    print(reverse_rec(L1))
    print(reverse_rec_no_slice(L1))

    zigzag(L1)

    # str = "(hello(j(jk))ii)"
    str = "((()(()())))"
    str = "((()()))(()(()))"
    # str = "())(()"
    # str = "well (I think), recursion works like that (as far as I know))"
    # #str = "(()()"
    print (str)

    print(is_balanced(str))