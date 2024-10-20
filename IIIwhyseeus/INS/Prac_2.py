#pip install pycryptodome (in CMD Prompt to import Crypto mopdules)
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generate RSA key pair
keypair = RSA.generate(1024)

# Get public key
pubKey = keypair.publickey()  # Corrected from public_key() to publickey()
print(f"Public Key : (n={hex(pubKey.n)}, e={hex(pubKey.e)})")

# Export public key to PEM format
pubKeyPEM = pubKey.export_key()
print(pubKeyPEM.decode('ascii'))

# Encryption
msg = 'Umbrella Academy'
msg_bytes = msg.encode('utf-8')  # Convert the message to bytes
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg_bytes)
print("Encrypted : ", binascii.hexlify(encrypted).decode('ascii'))  # Convert to hex and decode to ASCII
