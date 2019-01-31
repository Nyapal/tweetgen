import random, sys

def rearrange(sys): 
    sys.argv.pop(0)
    output = []

    while len(sys.argv) > 0:
        selected = random.choice(sys.argv)
        output.append(selected)
        sys.argv.remove(selected)
    print(output)

if __name__ == '__main__':
    params = sys.argv
    rearrange(sys)