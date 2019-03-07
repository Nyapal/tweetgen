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

if __name__ == "__main__":
    m = markov(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'one', 'pac', 
'tupac', 'red', 'pac', 'blue', 'pac'])
    n = next_word(m, 'fish')
    s = gen_sentences(m)

    # print('Markov: {}'.format(m))
    # print('Next Word: {}'.format(n))
    print(s)