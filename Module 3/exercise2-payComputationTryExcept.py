try:
    hrs = input("enter hours:")
    h = float(hrs)
    rate = input("enter rate:")
    r = float(rate)


    pay = h * r
    ot = (h - 40) * (r * .5)

    if h > 40.0:
        print(pay + ot)
    else:
        print(pay)
except:
    print("Enter a number, Ding Dong")

