def create_phone_number(n):
    if len(n) != 10:
        return ""
    
    final_string = "("
    for i in range(0, 3):
        final_string += str(n[i])
    final_string += ") "
    for i in range(3, 6):
        final_string += str(n[i])
    final_string += "-"
    for i in range(6, len(n)):
        final_string += str(n[i])
    return final_string