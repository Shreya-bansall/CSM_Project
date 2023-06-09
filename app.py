from flask import Flask, request, render_template
import os
import tempfile

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get public key file and save it
    publicKeyFile = request.files['publicKeyInput']
    publicKeyFilename = os.path.join(tempfile.gettempdir(), publicKeyFile.filename)
    publicKeyFile.save(publicKeyFilename)

    if 'privateKeyInput' in request.files:
        privateKeyFile = request.files['privateKeyInput']
        privateKeyFilename = os.path.join(tempfile.gettempdir(), privateKeyFile.filename)
        privateKeyFile.save(privateKeyFilename)

    # Get file
    file = request.files['file']
    file.save(file.filename)

    with open(file.filename, 'rb') as f:
        file_contents = f.read()

    action = request.form.get('action')

    # Perform encryption
    if action == 'encrypt':
        encrypted_file_contents = file_contents[::-1]

        encrypted_filename = 'encrypted_' + file.filename
        with open(encrypted_filename, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_file_contents)

        return f'Success! Encrypted file saved as {encrypted_filename}'

    # Perform decryption
    elif action == 'decrypt':
        decrypted_file_contents = file_contents[::-1]

        decrypted_filename = 'decrypted_' + file.filename
        with open(decrypted_filename, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_file_contents)

        return f'Success! Decrypted file saved as {decrypted_filename}'

    else:
        return 'Invalid action'

if __name__ == '__main__':
    app.run(debug=True)
