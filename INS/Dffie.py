"""
Key Exchange: 
Key exchange is a fundamental concept in cryptography that allows two parties to securely establish a shared secret key over an insecure communication channel. The shared key can then be used for symmetric encryption to ensure confidentiality, integrity, and authenticity of the communication. One widely used key exchange algorithm is the Diffie-Hellman algorithm. 
Key Exchange Techniques: 
Key exchange techniques enable secure key establishment between two parties. There are two main types of key exchange techniques: 
1) Symmetric Key Exchange 
2) Asymmetric Key Exchange 

Symmetric Key Exchange: 
In symmetric key exchange, both parties share a pre-established secret key. This key is typically distributed using a secure out-of-band method. Once the secret key is shared, it can be used for secure communication. However, this approach requires prior key sharing and becomes impractical for scenarios where a large number of participants need to securely communicate 
Asymmetric Key Exchange: 
Asymmetric key exchange, also known as public key exchange, overcomes the limitations of symmetric key exchange by using asymmetric encryption algorithms. It allows two parties who have never communicated before to establish a shared secret key without any prior key sharing. Asymmetric key exchange is based on the concept of public and private key pairs, where the public key is widely known and the private key is kept secret. 
Diffie-Hellman Algorithm: 
The Diffie-Hellman algorithm is a widely used asymmetric key exchange algorithm. It enables two parties to securely establish a shared secret key over an insecure communication channel. 
High-level working explanation of the Diffie-Hellman algorithm: 
	a) Select a large prime number, p, and a primitive root modulo p, g. These values are publicly known. 
	b) Each party, Alice and Bob, generates a private key, a and b, respectively. 
	c) Both Alice and Bob calculate their public keys: 
	d) Alice: A = gamod p 
	e) Bob: B = gb mod p 
	f) Alice and Bob exchange their public keys over the insecure channel. 

Key Generation: 
	a) Alice calculates the shared secret key using Bob's public key: 
	b) Secret Key: K = Ba mod p 
	c) Bob calculates the shared secret key using Alice's public key: 
	d) Secret Key: K = Ab mod p 

Key Agreement: 
Both Alice and Bob have calculated the same shared secret key, K, independently. 
They can now use K as the shared secret key for symmetric encryption algorithms to ensure secure communication. 
Security Considerations: 
The security of the Diffie-Hellman algorithm relies on the following considerations: 
1) Large Prime Numbers: The security of the algorithm is based on the difficulty of the discrete logarithm problem. Using large prime numbers ensures the security of the shared secret key. 
2) Public Key Distribution: The public keys exchanged during the key exchange process should be authenticated to prevent man-in-the-middle attacks. Techniques like digital signatures or certificate authorities can be used for authentication. 
3) Key Length: Longer key lengths provide stronger security against brute-force attacks. It is important to use an appropriate key length for the prime number to ensure the desired security level. 

Conclusion: 
Key exchange techniques play a crucial role in establishing secure communication channels between parties. The Diffie-Hellman algorithm, as an example of asymmetric key exchange, allows two parties to securely establish a shared secret key over an insecure channel.

"""

from random import randint

if __name__ == '__main__':
    P = 23
    G = 9
    print('The Value of P is :%d'%(P))
    print('The Value of G is :%d'%(G))
    a = 4
    print('Secret Number for Alice is :%d'%(a))
    x = int(pow(G,a,P))
    b = 6
    print('Secret Number for Bob is :%d'%(b))
    y = int(pow(G,b,P))
    ka = int(pow(y,a,P))
    kb = int(pow(x,b,P))
    print('Secret key for the Alice is : %d'%(ka))
    print('Secret Key for the Bob is : %d'%(kb))