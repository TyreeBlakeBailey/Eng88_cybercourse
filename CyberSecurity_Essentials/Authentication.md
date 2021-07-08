# Authentication

    The process of identifying a user, when they require access to a resource

## The fundamentals of Authentication

* Something you know (pin, password)

  #### *Password*
  
        - Users normally use something easy to remember
        - Most common method of authentication
        - An average a person has 25 different online accounts and only 54% use different passwords
        - 86% of more then 2 million breached passwords were identical to passwords that had already been breached 
        - Nation Cyber secuirty centre (NCSC) has a list of the top 100,000 passwords that have been part of a breached  
    #### Bad Passwords
        - Using dirionary words
        - Using personal information 
        - Using pattern 
        - Using character substituation
        - Using numbers and special characters only at the end 
        - Using common password
* Something you carry/have ( USB, proximity)
* Something you are (Fingerprint)

### Attacks & Defence
  #### Attacks
- Brute-Force attack 
- Rainbow Table Attack
  #### Defence 
- Salt techniques
- Key Stretching 

## Token Authentication 
    
    Can be either hardware/software
    Is a material device that is used to access a secure system
    Common forms include Dongle, Card, RFID chip  
    A hacker will need your credentials and your tangible device itself

### Biometrict Authentication 
  *Key Advantages*
  - Can be easily compared to authorized featured saved in a database 
  - Can control physical access when installed on entrances and doors
  - Can be added into multi-factor authentication-process

*Methods*

  - Facial Recognition
  - Fingerprint scanners 
  - Voice Identification
  - Eye scanners
      - Retinal
      - Iris 

### Certification-Based Authentication
    A digital verification is an electronic document based on the idea of a driving license
- The certification contains the digital identity of a user including a public key and the digital signature of a certification authority 

### Multi-factor authentication
    MFA is an authentication method that requires two or more independent ways to identify a user 
  - Used to increase the confidence of the user by adding layers of security
  - Good against attacks, but human error such as losing your phone can cause big problems 

## Authentication Protocols
- NTLM
  - Microsoft's protocol that provides authentication, integrity, Available
- KERBEROS 
  - Avoids storing keys locally and sending them over the network
- PAP
  - Password based authentication, Original used for point to point communication 
- CHAP 
  - Challenged handshake protocol similar to PAP but uses extra security features
- SSL/TLS
  - Secure Socket Layer/Transport Layer Security allows for the user to also question the server for authentication.
  - Has client and server side certificates 



## Lab 
Each line in the shadow file is separated into different fields by a ‘:’. Reading left-to-right,
the fields are:

    Login name
    Digest (referred to horribly as the “encrypted password”)
    Date of last password change
    Minimum password age
    Maximum password age
    Password warning period
    Password inactivity period
    Account expiration date
    Reserved
Within the field designated for the digest, it is further broken up into other fields that are
separated by a ‘$’. These fields are:
    
    $ID$salt$digest
| ID | Hash Function |
| --- | --- |
| 1 | MD5 |
| 2 | Blowfish |
| 3 | NT-hash |
| 4 | Not used |
| 5 | SHA 256 |
| 6 | SHA 512 |

# References

https://itexamanswers.net/ccna-1-v7-0-curriculum-module-2-basic-switch-and-end-device-configuration.html

https://www.ncsc.gov.uk/blog-post/passwords-passwords-everywhere

https://www.alliancetechpartners.com/network-security-authentication/

https://www.idrnd.ai/5-authentication-methods-that-can-prevent-the-next-breach/

https://haveibeenpwned.com/API/v3

https://www.solarwindsmsp.com/blog/network-authentication-methods

https://www.geeksforgeeks.org/understanding-rainbow-table-attack/