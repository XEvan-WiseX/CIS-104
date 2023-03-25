dictionary = dict()

max_so_far = 0
top_sender = " "

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
        ref_point = each_word[1].find('@')
        mail_server = each_word[1][ref_point+1:]
        
        if mail_server not in dictionary:
                dictionary[mail_server] = 1
        else:
                dictionary[mail_server] += 1
print(dictionary)
            