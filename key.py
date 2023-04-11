from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

# Generate ECC key pair
private_key = ec.generate_private_key(ec.SECP256R1())  # You can choose a different curve if needed
public_key = private_key.public_key()

# Serialize public key to PEM format
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save public key to a file
with open('public_key.pem', 'wb') as f:
    f.write(public_key_pem)