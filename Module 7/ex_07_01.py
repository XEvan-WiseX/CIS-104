fname = input ("Enter the file name:\n")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()
for line in fhand:
    print(line.upper())
    