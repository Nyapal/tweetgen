def histogram(source_text):
    words = source_text.split()
    dic = {}

    for word in words:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

    return dic

def unique_words(histogram):
    unique_words = []
    for k,v in histogram.items():
        if v == 1:
            unique_words.append(k)
    
    return unique_words

def frequency(word, histogram):
    for k,v in histogram.items():
        if word == k:
            print(v)
        
if __name__ == '__main__':
    h = histogram('one fish two fish red fish blue fish blue blue red two yellow grey whyte')
    q = unique_words(h)
    f = frequency('blue', h)
    #print(f)
    # params = sys.argv
    