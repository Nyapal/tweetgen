import random 
from random import sample

with open('sample.words', 'r') as f:
    words_list = [line.strip() for line in f]

print(' '.join(random.sample(words_list, 5)))