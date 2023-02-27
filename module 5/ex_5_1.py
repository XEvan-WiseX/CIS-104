total = 0
count = 0
while True :
    userentry = input("Enter a number: ")

    if userentry == "done" :
        break
    
    try:
        floatvalue = float(userentry)
        count = count + 1
        total = total + floatvalue
        
    except:
        print("invalid entry")  

print("total:", total, "count:", count, "average:", total/count)

    

