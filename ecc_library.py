from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes

# ECC encryption function
def ecc_encrypt(public_key, plaintext):
    serialized_public_key = serialization.load_pem_public_key(public_key)
    ciphertext = serialized_public_key.encrypt(
        plaintext,
        ec.ECIES(hashes.SHA256())
    )
    return ciphertext

# ECC decryption function
def ecc_decrypt(private_key, ciphertext):
    serialized_private_key = serialization.load_pem_private_key(
        private_key,
        password=None
    )
    plaintext = serialized_private_key.decrypt(
        ciphertext,
        ec.ECIES(hashes.SHA256())
    )
    return plaintext
