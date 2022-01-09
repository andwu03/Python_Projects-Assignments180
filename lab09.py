import urllib.request

word_counts = {}

#list_of_words = open("text.txt", encoding="latin-1").read().split()

#problem 1a)
def appear_times(l):
    global word_counts

    for i in range(len(list)):
        if (not (l[i] in word_counts)):
            word_counts[l[i]] = 1
        else:
            word_counts[l[i]] += 1

#problem 1b)
def top10_nums(l):
    top10 = []
    sorted_l = sorted(l)

    for i in range(10):
        top10.append(sorted_l[-1 - i])

    return top10

#problem 1c)
def top10_words(freq):
    top10_word = []
    inv_dict = {}

    for key, value in freq.items():
        inv_dict[value] = key #note that if a specific key is repeated, we have a problem, but we can ignore it for now
    sorted_inv_dict = sorted(inv_dict.keys(), reverse = True)

    for num in sorted_inv_dict:
        if len(top10_word) == 10:
            break
        for key in freq.keys():
            if freq[key] == num:
                top10_word.append(key)
            if len(top10_word) == 10:
                break
    
    return top10_word

# problem 2
# to change what we are searching, we need to modify the this line:
# <p>Here's the link to a Yahoo! search with the keyword "engineering science": <a href="https://ca.search.yahoo.com/search?p=engineering+science&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8">click here</a></p>
# for completeness, we change this line to:
# <p>Here's the link to a Yahoo! search with the keyword "": <a href="https://ca.search.yahoo.com/search?&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8">click here</a></p>
# we got rid of the p=engineering+science, which leads to a blank yahoo search box page
# if we add p=(whatever we want with words separated by "+") then we can put a link to search whatever we want into the html file

# problem 3
def choose_variant(variants):
    for item in variants:
        temp = item.split(" ")
        new_str = temp[0]
        for i in range(len(temp) - 1):
            new_str = new_str + "+" + temp[i + 1]
        search = urllib.request.urlopen("https://ca.search.yahoo.com/search?p=" + new_str + "&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8")
        page = search.read().decode("utf-8")
        print(page)


if __name__ == "__main__":
    list = ["I", "I", "Andre", "am", "smart"]
    num = [1,3,5,6543,32,3,4,6,7,5,4,4,3,3,6,7,8,4,34,3,56,6,56,7,7,6,5,4,3,32,7,56]
    dict = {"hello": 6, "a": 2, "b":7, "c":8, "d":0, "e":4, "f":3, "g":11, "h":11, "i":13, "j":100, "k":12, "l":10}

    print(top10_words(dict))

    choose_variant("nba raptors")
    

