def vigenere_cipher(text, key, mode): 
    result = "" 
    key = clean_text(key) 
  if len(key) == 0: 
        return "Key cannot be empty." 
    for i in range(len(text)): 
        p = ord(text[i]) - 65 
        k = ord(key[i % len(key)]) - 65 
        if mode == "E": 
            r = mod(p + k) 
        else: 
            r = mod(p - k) 
        result += chr(r + 65) 
    return result
