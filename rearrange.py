import random, sys

# def rearrange(sys):
#     ''' takes words from command line & rearranges them''' 
#     sys.argv.pop(0)
#     output = []

#     while len(sys.argv) > 0:
#         selected = random.choice(sys.argv)
#         output.append(selected)
#         sys.argv.remove(selected)
#     return output

def reverse(sys):
    '''takes sentence from command line & reverses it'''
    sys.argv.pop(0)
    input = sys.argv
    output = []

    for word in input:
        output.insert(0, word)
    return ' '.join(output)

if __name__ == '__main__':
    params = sys.argv
    #print(rearrange(sys))
    print(reverse(sys))