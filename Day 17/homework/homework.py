# 1 დავალება
def manual_remove(x):
    list1 = ["saba","gio","nika"]
    res = []
    for i in list1:
        if x != i:
            res.append(i)
    print(res)

manual_remove("gio")

# 2 დავალება

def manual_index(x):
    list2 = ["saba", "gio", "nika", "vano"]
    for i in range(len(list2)):
        if list2[i] == x:
            print(i)

manual_index("gio")


# 3 დავალება
def manual_len(list1):
    count = 0
    for i in list1:
        count+=1
    print(count)

manual_len(["saba", "gio", "nika", "vano"])

# 4 დავალება

def manual_pop(x):
    list3 = ["saba","gio","nika"]
    for i in range(len(list3)):
        print(list3[x])
        break

manual_pop(1)

# 5 დავალება

def manual_reverse(str1):  
    str2 = ""
    for i in str1:
        str2 = i + str2
    print(str2)

manual_reverse("goa")