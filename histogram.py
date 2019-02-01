with open('sample.words', 'r') as f:
    lines = f.read().split(" ")

def histogram(lines):
    output = []

    for word in lines:
        found = False
        new_word = str(word)
        for lis in output:
            if str(lis[0]) == new_word:
                lis[1] += 1
                found = True
                break
        if not found:
            new_lis = [new_word, 1]
            output.append(new_lis)
    
    return output #print(output)
   
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
    