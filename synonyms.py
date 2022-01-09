
'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
Completed by Andre Rodrigues and Andrew Wu on Dec 9, 2021
'''
import math

def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''
    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)

def cosine_similarity(vec1, vec2): #done
    # find dot product
    list1 = list(vec1.keys())
    sum = 0

    for keys in vec2.keys():
        if not (keys in vec1.keys()): list1.append(keys)
    for keys in list1:
        if (keys in vec1.keys()) and (keys in vec2.keys()): #if it is in both
            sum += vec1[keys] * vec2[keys]

    # find the magnitudes
    mag1 = 0
    mag2 = 0

    for value in vec1.values():
        mag1 += math.pow(value, 2)
    for value in vec2.values():
        mag2 += math.pow(value, 2)

    mag1 = math.pow(mag1, 0.5)
    mag2 = math.pow(mag2, 0.5)

    return round(sum/(mag1*mag2), 5)

def build_semantic_descriptors(sentences):
    d = {}
    for i in sentences: #go through each sentence
        L = list(set(i))
        for j in L: #go through each sentence word
            if j not in d: #new words added to dictionary
                d[j] = {}
            for k in L: #add words to the subdictionaries
                if k == j: #exclude key in counting
                    continue
                if k not in d[j]:
                    d[j][k] = 0
                d[j][k] += 1
    return d

def build_semantic_descriptors_from_files(filenames):
    sentence_list = []
    for word_string in filenames:
        sentence = []
        word_string = open(word_string, 'r', encoding = 'latin1')
        word_string = word_string.read().lower()
        word_string = word_string.replace(",", " ").replace("-", " ").replace("--", " ").replace(":", " ").replace(";", " ").replace('!', '.').replace('?', '.').split(".")
        for i in word_string:
            sentence.append(i.split())
        sentence_list += sentence
    return build_semantic_descriptors(sentence_list)

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    best = choices[0] #initially set best choice to be the first choice
    max_sim = -1
    if word in semantic_descriptors:
        for i in choices:
            if i in semantic_descriptors and similarity_fn(semantic_descriptors[word], semantic_descriptors[i]) > max_sim:
                max_sim = similarity_fn(semantic_descriptors[word], semantic_descriptors[i])
                best = i
    return best

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    b_string = open(filename, "r", encoding="latin1")
    string = b_string.read().lower().split('\n')
    cor_count = 0
    questions = []
    for i in string:
        if i != "":
            questions.append(i.split())
    for i in questions:
        if most_similar_word(i[0], i[2:], semantic_descriptors, similarity_fn) == i[1]:
            cor_count += 1
    count = len(questions)
    return 100.0*cor_count / count