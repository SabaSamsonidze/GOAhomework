# 1 დავალება

def manual_sum(num):
    total = 0 
    for i in num:
        total += i
    return total
my_list = [1, 2, 3, 4]
result = manual_sum(my_list)
print(result)

# 2 დავალება

def manual_append(list, item):
    new_list = []
    for i in list:
        new_list += [i]
    new_list += [item]
    return new_list

list = [1, 2, 3]
result = manual_append(list, 6)
print(result)