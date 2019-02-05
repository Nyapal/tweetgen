import random

with open('sample.words', 'r') as f:
    lines = f.read().split(" ")

#Jackson's code from class
def sample(histogram):
    total = 0
    cum_prob = 0.0
    for val in histogram:
        total += val[1]
    
    rand_num = random.uniform(0, 1)
    for val in histogram:
        cum_prob += val[1]/total
        if cum_prob >= rand_num:
            return val[0]

def multiple_runs(histogram):
    count = {}

    for item in histogram:
        count[item[0]] = 0

    for i in range(0, 1000):
        count[sample(histogram)] += 1
    
    print(count)

#if __name__ == '__main__':
    