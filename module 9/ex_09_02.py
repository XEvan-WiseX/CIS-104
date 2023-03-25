dictionary = dict()

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File not found: ', fname)
    exit()

for all_text in fhand:
    each_word = all_text.split()

    if len(each_word) < 3 or each_word[0] != 'From':
        continue
    else:
        if each_word[2] not in dictionary:
            dictionary[each_word[2]] = 1
        else:
            dictionary[each_word[2]] += 1

print(dictionary)