from flask import Flask, render_template, request, jsonify
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import ec
from ecc_library import ecc_encrypt, ecc_decrypt
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)

@app.route('/upload', methods=['POST','GET'])
def upload():
    try:
        public_key = request.files['publicKeyInput'].read()
        private_key = request.files['privateKeyInput'].read()
        file = request.files['file']
        plaintext = file.read()
        encrypted_filename = 'encrypted_' + file.filename
        decrypted_filename = 'decrypted_' + file.filename

        # Perform ECC encryption
        public_key = serialization.load_pem_public_key(public_key, backend=default_backend())
        ciphertext = ecc_encrypt(public_key, plaintext)
        with open(encrypted_filename, 'wb') as encrypted_file:
            encrypted_file.write(ciphertext)

        # Perform ECC decryption
        private_key = serialization.load_pem_private_key(private_key, password=None, backend=default_backend())
        with open(encrypted_filename, 'rb') as encrypted_file:
            ciphertext = encrypted_file.read()
        plaintext = ecc_decrypt(private_key, ciphertext)
        with open(decrypted_filename, 'wb') as decrypted_file:
            decrypted_file.write(plaintext)

        return f'Success! Encrypted file saved as {encrypted_filename}. Decrypted file saved as {decrypted_filename}'
    
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=False)
