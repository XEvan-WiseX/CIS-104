try:
    score = input("Enter Score: ")
    finalscr = float(score)
    if finalscr < .6 :
        print("F")
    elif finalscr > .6 and finalscr <= .7 :
        print("D")
    elif finalscr > .7 and finalscr <= .8 :
        print("C")
    elif finalscr > .8 and finalscr <= .9:
        print("B")
    elif finalscr > .9 and finalscr <= 1 :
        print("A")
    elif finalscr > 1 :
        print("Invalid Score")
except:
    print("invalid score")