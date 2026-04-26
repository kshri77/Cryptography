def inverse_matrix(a, b, c, d): 
    det = mod(a * d - b * c) 
    inv_det = -1 
    for i in range(1, 26): 
        if mod(det * i) == 1: 
            inv_det = i 
            break 
    if inv_det == -1: 
        return None 
    return ( 
        mod(inv_det * d), 
        mod(inv_det * -b), 
        mod(inv_det * -c), 
        mod(inv_det * a) 
    ) 
def hill_cipher(text, key_matrix, mode): 
    if len(text) % 2 != 0: 
        text += "X" 
    a, b, c, d = key_matrix 
    if mode == "D": 
        inv = inverse_matrix(a, b, c, d) 
        if inv is None: 
            return "Key matrix is not invertible." 
        a, b, c, d = inv 
    result = "" 
    for i in range(0, len(text), 2): 
        p1 = ord(text[i]) - 65 
        p2 = ord(text[i + 1]) - 65 
        r1 = mod(a * p1 + b * p2) 
        r2 = mod(c * p1 + d * p2) 
        result += chr(r1 + 65) + chr(r2 + 65) 
    return result 
