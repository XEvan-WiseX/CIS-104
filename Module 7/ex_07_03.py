fname = input ("Enter the file name:\n")
try:
    if fname=="na na boo boo":
        print("NA NA BOO BOO\nYOU HAVE BEEN PUNKED")
        exit()
    else:
        fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

total,count = 0,0    
for line in fhand:
    if not line.startswith('X-DSPAM-Confidence') : continue
    ref_point = line.find(":")
    spam_val = float(line[ref_point+1:])
    count = count + 1
    total = total + spam_val
print("Average Spam Confidence: ", total/count)



    