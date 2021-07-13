# Cryptography
![img_4.png](img_4.png)

## Essentials

* Encryption
    
  
    Encryption is a process which transforms the *original* information into an unrecognisable form of data 
![img_5.png](img_5.png)
* Decryption

  
    A process of converting encoded/encrypted data in a form that is readable and understood by a human or a computer
![img_6.png](img_6.png)

## Ciphers 

### Substitution cipher
Has a method, and a key for example below the key is 3, and the method is move along the alphabet by the number of the key
* Caesar Cipher
![img_7.png](img_7.png)

### Transposition Cipher
* No letter are replaces
* The letters are rearranged
![img_17.png](img_17.png)
## Encryption Classes

### Symmetric encryption algorithms
        Encryption algoriths that use the same key to encrypt and decrypt data
        Uses less computer resources then Asymmetric
* pre shared key that is different for every communication 
![img_8.png](img_8.png)
  1. Block Cipher
        * Takes the entire block of plain text and runs the encryption on the entire block i.e 64 bit blocks
        * Will pad the data if it isn't enough for 64 bits
    2. Stream Cipher 
        * Encrypts one bit at a time
        * Better to be used for things like streaming
![img_9.png](img_9.png)

![img_10.png](img_10.png)
## Asymmetric encryption algorithms
    Encryption algorithms that usse different keys to encrypt and decrypt data
    Either Public or Private can be used for encryption and decryption

![img_11.png](img_11.png)
![img_12.png](img_12.png)
 ### Confidentiality
* Public key(Encrypt) + Private Kay(Decrypt) = Confidentiality 
![img_13.png](img_13.png)
### Authentication
When you encrypt the message with the private key the receiver can be sure that it has come from the correct user as only they will  have the private key 
Integrity of the message is solid as no one can change it and re-encrypted it. 
![img_14.png](img_14.png)

## Diffie-Hellman
* An asymmetric mathematical algorithm
* Allows two computers to generate an identical shared secret without having communicated before
* The new shared key is never actually exchanged between the sender and receiver 
i.e Used in IPSec protocol
  
### Protocols that use Asymmetric
![img_15.png](img_15.png)

## Difference between Symmetric & Asymmetric 
![img_16.png](img_16.png)

# Online tools


https://www.dcode.fr/caesar-cipher

https://www.dcode.fr/substitution-cipher

https://www.dcode.fr/transposition-cipher

https://www.devglan.com/online-tools/aes-encryption-decryption

https://www.youtube.com/watch?v=gP4PqVGudtg

https://asecuritysite.com/encryption/diffie

# References

1. https://www.kaspersky.com/resource-center/definitions/what-is-cryptography
2. https://www.guru99.com/difference-encryption-decryption.html 
3. https://itexamanswers.net/ccna-cyber-ops-version-1-1-chapter-9-cryptography-and-the-public-key-infrastructure.html
4. https://itexamanswers.net/cyberops-associate-module-21-cryptography.html
5. https://www.thesslstore.com/blog/difference-encryption-hashing-salting/ 
6. https://itexamanswers.net/ccna-security-2-0-study-material-chapter-7-cryptographic-systems.html