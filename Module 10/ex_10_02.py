dictionary_hours = {}
listy = []

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    quit()
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    ref_point = words[5].find(':')
    time = words[5][:ref_point]
    if time not in dictionary_hours:
        dictionary_hours[time] = 1
    else:
        dictionary_hours[time] += 1
for k, v in list(dictionary_hours.items()):
    listy.append((k, v))
listy.sort()
for k, v in listy:
    print(k, v)
