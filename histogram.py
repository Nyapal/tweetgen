with open('sample.words', 'r') as f:
    lines = f.read().split(" ")

def histogram(lines):
    #DICTIONARY SOLUTION 
    dic = {}

    for word in lines:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

    return dic

def tup_list(lines): 
    #LIST OF TUPLES
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

    return tup_list

def lis(lines):
    #LIST OF LIST
    lis_of_lis = []

    for word in lines:
        found = False
        new_word = str(word)
        for lis in lis_of_lis:
            if str(lis[0]) == new_word:
                lis[1] += 1
                found = True
                break

        if not found:
            lis_of_lis.append([new_word, 1])
    
    return lis_of_lis 

def counts(lines):
    #LIST OF COUNTS
    print(lines)
    lis = []
    for k, v in lines.items():
        found = False 
        for item in lis:
            if v in item[0]:
                found = True
                array = item[1]
                array.append(key)
                lis.remove(item)
                lis.append((v, array))
                break
        if not found:
            lis.append((v, [k]))
    return lis


def unique_words(histogram):
    unique_words = []
    for k,v in histogram.items():
        if v == 1:
            unique_words.append(k)
    
    return unique_words

def frequency(word, histogram):
    for k,v in histogram.items():
        if word == k:
            return v
        
if __name__ == '__main__':
    #CALLING ALL FUNCTIONS
    hist = histogram(lines)
    tup = tup_list(lines)
    lis = lis(lines)
    count = counts(lines)

    uniq = unique_words(hist)
    freq = frequency('one', hist)

    #PRINTING ALL FUNCTION 
    # print('Dictionary Histogram: {}'.format(hist))
    # print('Histogram Tup List: {}'.format(tup))
    # print('Histogram List of List'.format(lis))
    print('Histogram List of Counts : {}'.format(count))

    # print('Unique Words: {}'.format(uniq))
    # print('Frequency: {}'.format(freq))