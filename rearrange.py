import random
from random import shuffle
import sys

sys.argv.pop(0)
shuffle(sys.argv)

print(sys.argv)