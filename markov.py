from dictogram import Dictogram
from sample import freq
import random

# lis = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'one', 'pac', 
# 'tupac', 'red', 'pac', 'blue', 'pac']

def markov(lis): 
    dic = {}
    for index in range(len(lis) - 1):
        word = lis[index]
        next_word = lis[index + 1]
        if word not in dic:
            add_to_dic = Dictogram([next_word])
            dic[word] = add_to_dic
        else:
            dic[word].add_count(next_word)

    return dic

def next_word(dic, word):
    ''' Get the next word based '''
    inner_dic = dic[word]
    rand_word = freq(inner_dic)
    return rand_word

def gen_sentences(dic):
    first_word = list(dic.keys())[0]
    sec_word = next_word(dic, first_word)
    sentence = first_word + ' ' + sec_word + ' '
    prev_word = sec_word

    for word in range(0, random.randint(1, 101)):
        new_word = next_word(dic, prev_word)
        prev_word = new_word
        sentence += new_word + ' '
    return sentence

def second_order_markov(lis):
    list_of_tup = []
    dic = {}
    for index in range(len(lis) - 2):
        first_word = lis[index]
        second_word = lis[index + 1]
        third_word = lis[index + 2]
        tup = (first_word, second_word)
        if tup not in dic:
            add_to_dic = Dictogram([third_word])
            dic[tup] = add_to_dic
        else:
            dic[tup].add_count(third_word)
    return dic

def second_sentences(dic):
    #tup is first and second word 
    tup = list(dic.keys())[0]
    # third_word = list(dic.keys())[2]
    third_word = next_word(dic, tup)
    # print('This is tuple:', tup, 'This is third word', third_word)
    sentence = tup[0] + ' ' + tup[1] + ' ' + third_word + ' '
    prev_word = (tup[1], third_word)
    # print('DICTIONARY:', dic)
    for word in range(0, random.randint(1, 101)):
        # print('This is prev word:', prev_word)
        
        new_word = next_word(dic, prev_word)
        prev_word = (prev_word[1], new_word)
        sentence += new_word + ' '
        if (prev_word not in dic):
            return sentence
    return sentence

if __name__ == "__main__":
    # m = markov(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'one', 'pac', 'tupac', 'red', 'pac', 'blue', 'pac'])
    # m = markov(['i', 'like', 'cats', 'you', 'like', 'dogs', 'but', 'we', 'both', 'hate', 'trump'])
    m2 = second_order_markov(['one', 'fish', 'red', 'pac', 'blue', 'pac', 'one', 'fish', 'two', 'blue', 'fish', 'one', 'pac', 'tupac', 'red', 'pac', 'blue', 'pac', 'one', 'fish', 'two', 'blue', 'fish', 'one', 'pac', 'tupac', 'red', 'pac', 'blue', 'pac'])
    # s = gen_sentences(m)
    s2 = second_sentences(m2)

    print(s2)
