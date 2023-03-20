def chop(lst):
    del lst[0]
    del lst[-1]

def middle(lst):
    list_changer = lst[1:]
    del list_changer[-1]
    return list_changer

first_list = [1, 2, 3, 4]
second_list = [1, 2, 3, 4]

chopped_list = chop(first_list)
print(first_list)
print(chopped_list)

mid_list = middle(second_list)
print(second_list)
print(mid_list)

