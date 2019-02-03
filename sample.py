import random, sys

def rand_word(sys): 
    sys.argv.pop(0)
    print(sys.argv)
    # output = []

    # while len(sys.argv) > 0:
    #     selected = random.choice(sys.argv)
    #     output.append(selected)
    #     sys.argv.remove(selected)
    # print(output)

if __name__ == '__main__':
    params = sys.argv
    rand_word(sys)