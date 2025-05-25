# 1 დავალება
def func(x):
    if type(x) == str:
        return "Literature"
    elif type(x) == int or type(x) == float:
        return "Math"
    elif type(x) == bool:
        return "Science"

print(func(True))

# 2 დავალება

def type1(lst1):
    count1 =0
    count2 = 0
    count3= 0
    count4 =0
    for i in lst1:
        if type(i) == str:
            count1 += 1
        elif type(i) == int:
            count2 += 1
        elif type(i) == float:
            count3 += 1
        else:
            count4 +=1
    x = max([count1,count2,count3,count4])
    
    if x == count1:
        print("string")
    elif x == count2:
        print("integer")
    elif x == count3:
        print("float")
    else:
        print("boolean")

# 3 დავალება

def find1(lst2):
    lst3 = []
    for i in lst2:
        if type(i) == int:
            lst3.append(i)
    print(lst3)
    
find1([1,2,3,4,5,6,7,8,"giorga"])

# 4 დავალება

def type2(a,b,operator):
    if operator == "/":
        print("float")
    elif type(a) == float or type(b) == float:
        print("float")
    else:
        print("integer")

type2(1.5,2,"*")

