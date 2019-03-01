from dictogram import Dictogram
lis = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'one', 'pac', 
'tupac', 'red', 'pac', 'blue', 'pac']

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

print(markov(lis))