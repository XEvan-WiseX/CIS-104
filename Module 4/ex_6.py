def computepay(hours, rate):
    if hours > 40:
        reg = hours * rate
        ot = (hours - 40) * rate *.5
        pay = reg + ot
        return(pay)
    elif hours <= 40:
        pay = hours * rate
        return(pay)
hrs = input("Enter Hours: ")
rt = input("Enter Rate: ")
fhrs = float(hrs)
frt = float(rt)

pay = computepay(fhrs, frt)
print(pay)
