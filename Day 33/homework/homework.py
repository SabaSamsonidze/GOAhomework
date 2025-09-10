# 1 დავალება

def manual_split(s, separator=" "):
    result = []
    current = ""
    for i in s:
        if i == separator:
            if current != "":
                result.append(current)
                current = ""
        else:
            current += i
    if current:
        result.append(current)
    return result

