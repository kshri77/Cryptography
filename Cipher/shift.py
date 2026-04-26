def mod(n): 
    return n % 26 
def clean_text(text): 
    return "".join(ch for ch in text.upper() if ch.isalpha()) 
def shift_cipher(text, key, mode): 
    result = "" 
    for ch in text: 
        p = ord(ch) - 65 
        if mode == "E": 
            r = mod(p + key) 
        else: 
            r = mod(p - key) 
        result += chr(r + 65) 
    return result
