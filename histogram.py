with open('sample.words', 'r') as f:
    lines = f.read().split(" ")

def histogram(lines):
    # LIST OF TUPLES
    tup_list = []

    for word in lines:
        found = False 
        for inner_tuple in tup_list:
            if word == inner_tuple[0]:
                count = inner_tuple[1] + 1
                tup_list.remove(inner_tuple)
                tup_list.append((word, count))
                found = True 
                break
        if not found:
            tup_list.append((word, 1))

    print('TUP LIST: {}'.format(tup_list))

    # for k, v in lines.iteritems():

    #my failed attempt at tuples, coming back to this with a TA
    # output = (['nyapals', 1], ['hey', 2], ['wow', 1])
    # counter = 1
   
    # for word in lines:
    #     if word  counter in output:
    #         print([word, counter])
    #     else:
    #         print(word + ' not found')
       
    
    # LIST OF LIST
    # lis_of_lis = []

    # for word in lines:
    #     found = False
    #     new_word = str(word)
    #     for lis in lis_of_lis:
    #         if str(lis[0]) == new_word:
    #             lis[1] += 1
    #             found = True
    #             break

    #     if not found:
    #         lis_of_lis.append([new_word, 1])
    
    # return lis_of_lis 

    #DICTIONARY SOLUTION 
   
    # dic = {}

    # for word in lines:
    #     if word in dic:
    #         dic[word] += 1
    #     else:
    #         dic[word] = 1

    # return dic

# def unique_words(histogram):
#     unique_words = []
#     for k,v in histogram.items():
#         if v == 1:
#             unique_words.append(k)
    
#     return unique_words

# def frequency(word, histogram):
#     for k,v in histogram.items():
#         if word == k:
#             return v
        
if __name__ == '__main__':
    #histogram(lines)
    h = histogram(lines)
    # q = unique_words(h)
    # f = frequency('one', h)
    print('Histogram: {}'.format(h))
    # print('Unique Words: {}'.format(q))
    # print('Frequency: {}'.format(f))
    