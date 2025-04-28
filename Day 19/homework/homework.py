# 1 დავალება

def merged_list_sort(list, list1):
    merged_list = list + list1
    merged_list.sort()
    return merged_list

new_list1 = [1, 5, 3, 2]
new_list2 = [4, 6, 9, 10]
print(merged_list_sort(new_list1, new_list2))


# 2 დავალება

def bigger_sum_list(list1, list2):
    sum1 = 0
    for num in list1:
        sum1 += num
    
    sum2 = 0
    for num in list2:
        sum2 += num
    
    if sum1 > sum2:
        return list1
    else:
        return list2

new_list3 = [1, 4, 5, 6,]
new_list4 = [8, 2, 3, 10]
res1 = bigger_sum_list(new_list3, new_list4)
print(res1)

# 3 დავალება

def negative_positive(list1, list2):
    positive = 0
    negative = 0

    for i in list1 + list2:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += i

    return positive, negative

list1 = [-1, -5, 2, 6, 3]
list2 = [-3, 9, -4, -2]
res2 = negative_positive(list1, list2)
print(res2)

# 4 დავალება

def remove_3(lst):
    list = []
    for i in lst:
        if i % 3 != 0:
            list.append(i)
    return list        


new_list = [1, 3, 4, 2, 6, 9, 5]
res = remove_3(new_list)
print(res)

# 5 დავალება

def multiply_list(lst):
    list = []
    for i in lst:
        list.append(i * 2)
    return list

my_list = [1, 5, 2, 6, 3]
result = multiply_list(my_list)

print(result)