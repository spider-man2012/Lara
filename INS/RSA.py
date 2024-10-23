'''
RSA (Rivest-Shamir-Adleman) Algorithm: 
RSA is a widely used asymmetric encryption algorithm that provides secure communication over untrusted networks. It is based on the mathematical problem of factoring large prime numbers, which is computationally difficult and forms the foundation of RSA's security. 

Key Generation: 
The RSA algorithm involves the generation of a public-private key pair. The key generation process consists of the following steps: 
	a) Select two distinct prime numbers, p and q. 
	b) Compute the modulus, N, by multiplying p and q: N = p * q. 
	c) Calculate Euler's function, φ(N), where φ(N) = (p - 1) * (q - 1). 
	d) Choose an integer, e, such that 1 < e <φ(N) and e is coprime with φ(N). This means that e and φ(N) should have no common factors other than 1. 
	e) Find the modular multiplicative inverse of e modulo φ(N), denoted as d. In other words, d is an integer such that (d * e) % φ(N) = 1. 
	f) The public key consists of the modulus, N, and the public exponent, e. The private key consists of the modulus, N, and the private exponent, d. 

Encryption Process: 
To encrypt a message using RSA encryption, follow these steps: 
	a) Obtain the recipient's public key, which includes the modulus, N, and the public exponent, e. 
	b) Represent the plaintext message as an integer, M, where 0 ≤ M < N. 
	c) Compute the ciphertext, C, using the encryption formula: C = Me mod N. 

Decryption Process: 
To decrypt a message encrypted with RSA encryption, the recipient uses their private key. Follow these steps: 
	a) Obtain the recipient's private key, which includes modulus, N, and the private exponent, d. 
	b) Receive the ciphertext, C. 
	c) Compute the plaintext, M, using the decryption formula: M = Cd mod N. 


'''

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
