dictionary = dict()
l = list()

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File not found: ', fname)
    exit()

for all_text in fhand:
    each_word = all_text.split()

    if len(each_word) < 2 or each_word[0] != 'From':
        continue
    else:
        if each_word[1] not in dictionary:
            dictionary[each_word[1]] = 1
        else:
            dictionary[each_word[1]] += 1
            
for k, v in list(dictionary.items()):
    l.append((v, k))
l.sort(reverse=True)
for k, v in l[:1]:
    print(k, v)