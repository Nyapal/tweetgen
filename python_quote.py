import random

quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")

sentence = 'This is a sentence that i will reverse.'


def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

def reverse_sentence():
    words_list = sentence.split(' ')
    print(words_list)

if __name__ == '__main__':
    rand_quote = random_python_quote()
    rev_sent = reverse_sentence()
    #print (rand_quote)
    print(rev_sent)