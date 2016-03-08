import sys, os, hashlib, string, itertools
from timeit import default_timer as timer

SYMBOLS = '!@#$%^&*(){}[]:";<>?,./\'\\' #testing, may be incomplete

'''
Given a password, a local dictionary is enumerated to see
how quickly a match can be found
'''
def dictionaryAttack(password):
    file = open("app/basicDictionary.txt")
    start = timer()
    for word in file:
        if word.rstrip() == password:
            stop = timer()
            return 'Found the password in ' + str(stop - start) + ' seconds.'
    return "Password not cracked, not in dictionary."

'''
Given a password, details such as length and types of characters will be used 
to craft a brute force attack against the password

Amount of time is recorded and returned as a result
'''
def bruteForceAttack(password):
    numberofchars = len(password)
    
    containsUpper = False
    containsSymbols = False
    containsNumbers = False
    
    for ch in password:
        if ch in SYMBOLS:
            containsSymbols = True
        elif ch in string.digits:
            containsNumbers = True
        elif ch in string.ascii_uppercase:
            containsUpper = True
    
    charset = string.ascii_lowercase
    
    if containsSymbols:
        charset += SYMBOLS
    if containsUpper:
        charset += string.ascii_uppercase
    if containsNumbers:
        charset += string.digits
        
    print charset
        
    gen = bruteforce(charset, numberofchars) 
    start = timer()
    for p in gen: 
        if p == password:
            stop = timer()
            return 'Found the password in ' + str(stop - start) + ' seconds.'
    return 'not found'

'''
Given a character set as a string and a length, creates a generator that yields a
new combination of a brute force sequence
'''
def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(1, maxlength + 1)))      

'''
'''
def passwordChecker(password):
    containsLower = False
    containsUpper = False
    containsSymbols = False
    containsNumbers = False
    numberofchars = len(password)
    
    
    for ch in password:
        if ch in SYMBOLS:
            containsSymbols = True
        elif ch in string.digits:
            containsNumbers = True
        elif ch in string.ascii_uppercase:
            containsUpper = True
        elif ch in string.ascii_lowercase:
            containsLower = True
            
    results = ''
    if numberofchars >= 8:
        results += 'Minumum number of characters requirement met. '
    else:
        results += 'Minumum number of characters requirement unmet. '
        
    if containsUpper and containsLower:
        results += 'Contains upper and lowercase characters. '
    else:
        results += 'Does not contain upper and lowercase characters. '
        
    if containsNumbers:
        results += 'Contains numbers. '
    else:
        results += 'Does not contain numbers. '
        
    if containsSymbols:
        results += 'Contains symbols. '
    else:
        results += 'Does not contain symbols. '
        
    if dictionaryAttack(password) != 'Password not cracked, not in dictionary.':
        results += 'Is in a dictionary. '
    else:
        results += 'Is not in a dictionary. '
        
    return results
        
        
        
    
    