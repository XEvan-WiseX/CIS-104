count = 0

min_value = 0
max_value = 0

while count < 3 :

    try :
        count = count + 1

        current_value = input("Enter a number: ")
        bucket_brigade = float(current_value)

        

        if min_value == 0 :
            min_value = bucket_brigade
        elif bucket_brigade < min_value :
            min_value = bucket_brigade
        
        if max_value == 0 :
            max_value = bucket_brigade
        elif bucket_brigade > max_value :
            max_value = bucket_brigade

    except :
        print("Enter numbers only")


print("Minimum:", min_value, "Maximum:", max_value)
