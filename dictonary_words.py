import random 
from random import sample

with open('//usr/share/dict/words', 'r') as f:
    words_list = [line.strip() for line in f]

output = ' '.join(random.sample(words_list, 9)) + '.'

print(output.capitalize())