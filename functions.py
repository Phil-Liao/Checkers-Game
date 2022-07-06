def is_odd(num):
    num = float(num)
    if num / 2 != num / 2 // 1 :
        #print(f"{int(num)} --> Odd")
        return True
    else:
        #print(f"{int(num)} --> Even")
        return False

def key_in_dict(dict, value):
    for i in range(0, len(dict), 1):
        if dict[i+1] == value:
            #print(f"The key is {i+1}")
            return i + 1