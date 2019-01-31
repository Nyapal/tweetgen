import random 
from random import sample

# with automatically closes the file once everything inside of it has been done
with open('//usr/share/dict/words', 'r') as f:
    words_list = [line.strip() for line in f]

output = ' '.join(random.sample(words_list, 9)) + '.'

print(output.capitalize())