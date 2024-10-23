'''
Message Authentication Code (MAC): 
MAC is a technique used to ensure the integrity and authenticity of messages exchanged between two parties. It involves the use of a secret key and a cryptographic hash function to generate a tag or code that can be appended to the message. The receiver can verify the integrity and authenticity of the message by recomputing the MAC using the same key and hash function and comparing it with the received MAC. 
MAC can be implement using various algorithms, we consider MD5 and SHA1 

MD5 Algorithm: 
MD5 (Message Digest Algorithm 5) is a widely used cryptographic hash function. Although it has been widely used historically, it is now considered to have vulnerabilities and is not recommended for security-critical applications. Nonetheless, it serves as an educational example for understanding MAC and cryptographic hash functions. 

MAC Generation Process: 
To generate a MAC using the MD5 algorithm, follow these steps: 
	a) Both the sender and receiver must agree on a secret key, K, which is known only to them. 
	b) Concatenate the message, M, and the secret key, K: ConcatenatedData = M || K (|| denotes concatenation). 
	c) Apply the MD5 algorithm to the ConcatenatedData to obtain the MAC: MAC = MD5(ConcatenatedData). 
	d) MAC Verification Process: 

To verify the integrity and authenticity of a received message using the MAC, follow these steps: 
	a) Receive the message, M, and the MAC, MAC. 
	b) Concatenate the received message, M, with the secret key, K: ConcatenatedData = M || K. 
	c) Apply the MD5 algorithm to the ConcatenatedData to compute the recalculated MAC: RecalculatedMAC = MD5(ConcatenatedData). 
	d) Compare the RecalculatedMAC with the received MAC. If they match, the message is considered authentic and intact. 

Security Considerations: 
MD5 is no longer considered secure for cryptographic purposes due to vulnerabilities that have been discovered. It is susceptible to collision attacks, where two different inputs produce the same hash value. Therefore, it is recommended to use stronger hash functions, such as SHA-256 or SHA-3, for MAC generation in real-world applications. 
SHA1 (Secure Hash Algorithm): 
SHA is a family of cryptographic hash functions designed by the National Security Agency (NSA) in the United States. It provides secure one-way hashing and is widely used for various security applications. Examples include SHA-256 and SHA-3, which are stronger and more secure than MD5 or SHA-1. 
MAC Generation Process: 
To generate a MAC using the SHA algorithm, such as SHA-256, follow these steps: 
	a) Both the sender and receiver must agree on a secret key, K, which is known only to them. 
	b) Concatenate the message, M, and the secret key, K: ConcatenatedData = M || K (|| denotes concatenation). 
	c) Apply the SHA algorithm (e.g., SHA-256) to the ConcatenatedData to obtain the MAC: MAC = SHA-256(ConcatenatedData). 
	d) MAC Verification Process: 

To verify the integrity and authenticity of a received message using the MAC, follow these steps: 
	a) Receive the message, M, and the MAC, MAC. 
	b) Concatenate the received message, M, with the secret key, K: ConcatenatedData = M || K. 
	c) Apply the SHA algorithm (e.g., SHA-256) to the ConcatenatedData to compute the recalculated MAC: RecalculatedMAC = SHA-256(ConcatenatedData). 
	d) Compare the RecalculatedMAC with the received MAC. If they match, the message is considered authentic and intact. 

Security Considerations: 
The security of MAC relies on the confidentiality and integrity of the secret key. If an attacker gains access to the secret key, they can generate valid MACs and forge messages. Therefore, it is crucial to employ strong key management practices to protect the secret key. 
Additionally, the security of the MAC depends on the security of the underlying hash function. Strong hash functions like SHA-256 are designed to resist collision attacks and other cryptographic vulnerabilities.

'''

import hashlib 
result = hashlib.md5(b'Ismile')
result1 = hashlib.md5(b'Esmile') # printing the equivalent byte value. 
print("The byte equivalent of hash is : ", end ="")
print(result.digest()) 
print("The byte equivalent of hash is : ", end ="")
print(result1.digest())