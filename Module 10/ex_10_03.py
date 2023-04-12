import string

counts = 0                          # Initialize variables
dictionary_letter_counter = dict()
lst = list()

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()

    words = line.split()
    for word in words:
        for letter in word:

            counts += 1
            if letter not in dictionary_letter_counter:
                dictionary_letter_counter[letter] = 1
            else:
                dictionary_letter_counter[letter] += 1

for key, val in list(dictionary_letter_counter.items()):
    lst.append(((val / counts * 100, key)))
    

lst.sort(reverse=True)

print("Values are a percentage of all letters:")

for key, val in lst:
    print( key, val)
    