def rgb(r, g, b):
    r = min(max(0, r), 255)
    g = min(max(0, g), 255)
    b = min(max(0, b), 255)
    
    return f"{r:02X}{g:02X}{b:02X}"