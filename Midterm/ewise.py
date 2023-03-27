fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File not found: ', fname)
    exit()

cheese_tray = fhand.read().replace("\n", " ").splitlines()
for line in cheese_tray:
    cheese_platter = line.split()
cheese_platter.sort()
     
print(cheese_platter)
