#problem 1

f = open("lab07data.txt")

count = 0

for line in f:
    fline = line.lower()

    if fline.find("lol") >= 0:
        count += 1

print(count)

#problem 2

def dict_to_string(d):

    for key, value in d.items():
        print(str(key) + ", " + str(value))

# problem 3

def dict_to_string_sorted(d):
    l = sorted(d.keys())

    for val in l:
        print(str(val) + ", " + str(d[val]))

# problem 4



if __name__ == "__main__":
    d = {1:2,3:4,2:5}
    dict_to_string(d)
    dict_to_string_sorted(d)

