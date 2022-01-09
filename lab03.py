#problem1
import lab02, math
#check test_calc.py

#problem2
def sum_of_cubes1(n):
    sum = 0
    for i in range(n):
        sum += math.pow((i+1), 3)
    return sum

def sum_of_cubes2(n):
    sum = 0
    for i in range(n):
        sum += i+1
    return math.pow(sum, 2)

def check_sum(n):
    return sum_of_cubes1(n) == sum_of_cubes2(n)

def check_sums_up_to_n(N):
    for i in range (N):
        if not check_sum (i+1):
            return False
    return True

#problem3
def leibniz_pi (n):
    val = 0
    for i in range (n+1):
        val += math.pow(-1, i)/(2*i + 1)
    return 4*val

if __name__ == "__main__":
    print(check_sum(3))
    print(check_sums_up_to_n(3))
    print("pi =",leibniz_pi(1530010))
