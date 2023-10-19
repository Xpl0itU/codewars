walk_values = {
    "n": 1,
    "s": -1,
    "e": 2,
    "w": -2,
}

def is_valid_direction(direction):
    return direction in ["n", "s", "e", "w"]

def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    
    current_point = 0
    for direction in walk:
        if not is_valid_direction(direction):
            return False
        current_point += walk_values[direction]
    return current_point == 0