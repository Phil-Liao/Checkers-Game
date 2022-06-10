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

def closest_to_point(x, y, GAME_WIDTH, GAME_HEIGHT):
    for x_axis in range(0, GAME_WIDTH, GAME_WIDTH/8):
        if 0 < x - x_axis < GAME_WIDTH / 8:
            return_x = x_axis
            break
    for y_axis in range(0, GAME_HEIGHT, GAME_HEIGHT/8):
        if 0 < y - y_axis < GAME_HEIGHT / 8:
            return_y = y_axis
            break
    return return_x, return_y