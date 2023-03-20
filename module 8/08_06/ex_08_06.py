number_list = []
while True:

    new_list_item = input("Enter a number: ")
    if new_list_item == "done":
        break
    try:
        input_converter = float(new_list_item)
    except ValueError:
        print("Numbers Only, start over")
        quit()
    number_list.append(input_converter)
print("Maximum: ", max(number_list))
print("Minimum: ", min(number_list))
