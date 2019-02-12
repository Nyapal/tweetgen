import random
from histogram import histogram

with open('sample.words', 'r') as f:
    lines = f.read().split(" ")

def freq(hist):
    ''' take a random word from a histogram, based on freq'''
    output = random.sample(list(hist), 1)

    return ''.join(output)

    #print(random.choice(hist.keys()))

    # return random.choice(hist.keys())
    # output = []
    # for word, freq in hist.items():
    #     return random.choice(hist.keys())
    # print(hist)
    # return random.choice(hist)
    # count = 0 
    # output = []

    # for word, freq in hist.items():
    #     count += freq
    #     print("{} appears {} time(s). The count is {}".format(word, freq, count))
    #     # if freq < count:
    #     #     print(word)

def rand_test(hist):
    ''' run the random word function a x times '''
    word = freq(hist)
    x = 10000
    output = []

    i = 0
    while i <= x:
        word = freq(hist)
        output.append(word)
        i += 1

    return histogram(output)

    

# one  => 0.125
# fish => 0.5
# two  => 0.125
# red  => 0.125
# blue => 0.125

# def sample(lis):
#     total = 0
#     cum_prob = 0.0
#     for val in lis:
#         print(val[1])
#         #total += val[1]
    
#     rand_num = random.uniform(0, 1)
#     for val in lis:
#         cum_prob += val[1]/total
#         if cum_prob >= rand_num:
#             return val[0]

    
if __name__ == '__main__':
    hist = histogram(lines)
    rand = freq(hist)
    test = rand_test(hist)
    
    print(test)

    