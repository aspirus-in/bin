from random import choice
import sys

with open('words.txt', 'r') as words_file:
    words = words_file.read().split()

for i in range(int(sys.argv[1])):
    print(choice(words), end=' ')
print()
