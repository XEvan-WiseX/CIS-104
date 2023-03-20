word_list = []
fhand = open('romeo.txt')
for line in fhand:
    words = line.split()
    for new_word in words:
        if new_word in word_list:
            continue
        word_list.append(new_word)
print(sorted(word_list))

