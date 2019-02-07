import random
from histogram import histogram

with open('sample.words', 'r') as f:
    lines = f.read().split(" ")

def rand_word(hist):
    count = 0 
    for word, freq in hist.items():
        print(word)
        print(freq)
    # lis = []
    # for word in hist:
    #     lis.append(word)
    
    # return random.choice(lis)

def rand_test(hist):
    ''' run the random word function a bunch of times '''
    word = rand_word(hist)
    output = []

    i = 0
    while i <= 10000:
        word = rand_word(hist)
        output.append(word)
        i += 1

    print(histogram(output))
    #print(output)

    

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

# def multiple_runs(lines):
#     count = {}

#     for item in lines:
#         count[item[0]] = 0

#     for i in range(0, 1000):
#         count[sample(lines)] += 1
    
if __name__ == '__main__':
    my_histogram = histogram(lines)
    random_word = rand_word(my_histogram)
    print('Random Word: {}'.format(random_word))
    random_test = rand_test(my_histogram)
    print('Testing Randomness: {}'.format(random_test))
    # multiple_runs(lines)
    