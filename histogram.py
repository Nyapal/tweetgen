def histogram(source):
    words = source.split()
    dict_list = {}

    for word in words:
        if word in dict_list:
            dict_list[word] += 1
        else:
            dict_list[word] = 1

return dict_list

def unique_words():
    pass

def frequency():
    pass

if __name__ == '__main__':
    histogram('one fish two fish red fish blue fish blue blue red two')
    # params = sys.argv
    # rearrange(sys)