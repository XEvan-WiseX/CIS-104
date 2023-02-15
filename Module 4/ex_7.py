
def computegrade(scr):
    if scr > 1 or scr < 0:
        finalscr = "Invalid Score"
    elif scr >= .9:
        finalscr = "A"
    elif scr >= .8:
        finalscr = "B"
    elif scr >= .7:
        finalscr = "C"
    elif scr >= .6:
        finalscr = "D"
    else:
        finalscr = "F"
    return finalscr

scr = input("Enter Score")

try:
    scr = float(scr)
    finalscr = computegrade(scr)
    print(finalscr)

except:
    print("Score must be a decimal between 0 and 1")
