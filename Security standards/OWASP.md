# OWASP 
## (Open Web Application Security Risk )

https://raw.githubusercontent.com/OWASP/Top10/master/2017/OWASP%20Top%2010-2017%20(en).pptx

### Injection

Injection is being able to send hostile data to an interpreter.
Common injections are:

| SQL         | LDAP                  |
|-------------|-----------------------|
| XPath       | NoSQL                 |
| OS cammands | XML parsers           |
| SMTP header | Expression languages  |

* Discovery

The use of scanners and fuzzers can ben used to easily find teh injection flaws 

* Impact
 
An injection attack can result in data loss corruption or data disclosure, Denial of access.
And could even lead to complete takeover.

* Prevention

Use a safe API which will avoid the use of interpreters entirely or provides a parameterized interface
or using ORMs (object relational Mapping tools)
    * ORM is a programming technique for converting data between incompatible type systems using OOP languages, which creates a Virtual object database to be used from within the programming language. 
Use SQL control i.e LIMIT to prevent disclosure of records 


### Logging and Monitoring
Exploitability 2 Average
Prevalence 3 Widespread
Detectability 1 Difficult
Technical 2 Moderate