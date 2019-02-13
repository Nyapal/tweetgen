import random
from histogram import histogram

with open('sample.words', 'r') as f:
    lines = f.read().split(" ")

def single_rand_word(hist):
    ''' returns a random word from a histogram '''
    return ''.join(random.sample(list(hist), 1))

def freq(hist):
    ''' returns a random word from a histogram, based on freq'''
    count = 0 
    dic = histogram(hist)
    for key in dic:
        count += dic[key]

    rand = random.randrange(count)
    num_total = 0 
    for key in dic:
        num_total += dic[key]
        if rand < num_total:
            return key
    

def rand_test(hist):
    ''' run the freq function a x times '''
    word = freq(hist)
    x = 10000
    output = []

    i = 0
    while i <= x:
        word = freq(hist)
        output.append(word)
        i += 1

    return histogram(output)

if __name__ == '__main__':
    # FUNCTIONS 
    rand_word = single_rand_word(lines)
    hist = histogram(lines)
    rand = freq(lines)
    test = rand_test(lines)
    
    # FUNCTION CALLS 
    print('Randomness Test: {}'.format(test))

    