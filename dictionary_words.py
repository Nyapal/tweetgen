import random 
from random import sample

# with automatically closes the file once everything inside of it has been done
with open('sample.words', 'r') as f:
    lines = f.read().split(" ")
    #words_list = [line.strip('') for line in f]


def sentence(): 
    output = ' '.join(random.sample(lines, 9)) + '.'
    return output.capitalize()

if __name__ == '__main__':
    print(sentence())