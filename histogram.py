def histogram(source):
    words = source.split()
    dic = {}

    for word in words:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

    return dic

def unique_words(dic):
    print(dic)
    unique_words = []
    for k,v in dic.items():
        print(k)
        if v == 1:
            unique_words.append(k)
    
    print(unique_words)
    

def frequency():
    pass

if __name__ == '__main__':
    hist = histogram('one fish two fish red fish blue fish blue blue red two yellow grey whyte')
    unique_words(hist)
    # params = sys.argv
    