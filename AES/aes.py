from flask import Flask, render_template, request 
from 
import AES 
import binascii 
app = Flask(  name  ) 
@app.route('/', methods=['GET', 'POST']) 
def index(): 
output = "" 
if request.method == 'POST': 
pt = request.form['pt'].encode('utf-8') 
key_text = request.form['key'] 
# AES-128 requires exactly 16 bytes for the key 
if len(key_text) != 16: 
output = "Error: Key must be exactly 16 characters long." 
else: 
key = key_text.encode('utf-8') 
# Initialize AES cipher in EAX mode 
cipher = AES.new(key, AES.MODE_EAX) 
# Encrypt the plaintext and generate a MAC tag for integrity 
ciphertext, tag = cipher.encrypt_and_digest(pt) 
# Formatting results for display 
output += "STEP 1: INITIALIZATION\n" 
output += f"Key Used: {key_text}\n" 
output += f"Nonce (Hex): {binascii.hexlify(cipher.nonce).decode()}\n\n" 
output += "STEP 2: ENCRYPTION\n" 
output += f"Ciphertext (Hex): {binascii.hexlify(ciphertext).decode()}\n" 
output += f"Auth Tag (Hex): {binascii.hexlify(tag).decode()}\n\n" 
output += "Note: Keep the Nonce and Tag for decryption." 
return render_template('AES.html', output=output) 
if  name == ' main ': 
app.run(debug=True)
