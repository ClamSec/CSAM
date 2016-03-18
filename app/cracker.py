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
    count = 0
    for word in file:
        count += 1
        if word.rstrip() == password:
            stop = timer()
            duration = stop - start
            #return 'Found the password in ' + str(stop - start) + ' seconds.'
            return 'Found the password in ' + str(round(duration, 2)) + ' seconds. Tried '+ str(count)+ ' passwords, for an average of '+ str(int(count / duration))+ ' password attempts/second.'
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
    count = 0
    gen = bruteforce(charset, numberofchars) 
    start = timer()
    for p in gen:
        count += 1
        if p == password:
            stop = timer()
            duration = stop - start
            return 'Found the password in ' + str(round(duration, 2)) + ' seconds. Tried '+ str(count)+ ' passwords, for an average of '+ str(int(count / duration))+ ' password attempts/second.'
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
Determines what requirements a given password satisfy, returns a dictionary where
keys are requirements and their values are whether or not they have been met
'''
def passwordChecker(password):
    
    results = {}
    
    containsLower = False
    containsUpper = False
    containsSymbols = False
    containsNumbers = False
    numberofchars = len(password)
    
    results['numchars'] = numberofchars
    
    
    for ch in password:
        if ch in SYMBOLS:
            containsSymbols = True
        elif ch in string.digits:
            containsNumbers = True
        elif ch in string.ascii_uppercase:
            containsUpper = True
        elif ch in string.ascii_lowercase:
            containsLower = True
            
    if numberofchars >= 8:
        results['minchars'] = True
    else:
        results['minchars'] = False
        
    if containsUpper:
        results['upper'] = True
    else:
        results['upper'] = False
        
    if containsLower:
        results['lower'] = True
    else:
        results['lower'] = False
        
    if containsNumbers:
        results['containsNums'] = True
    else:
        results['containsNums'] = False
        
    if containsSymbols:
        results['symbols'] = True
    else:
        results['symbols'] = False
        
    if dictionaryAttack(password) != 'Password not cracked, not in dictionary.':
        results['dict'] = True
    else:
        results['dict'] = False
        
    return results

'''
'''
def makeComplexityTable(password):
    results = passwordChecker(password)
    table = {}
    if results['minchars']:
        table['Minimum # of characters'] = u'\u2713'
    else:
        table['Minimum # of characters'] = 'x'
    
    if results['upper']:
        table['Uppercase characters'] = u'\u2713'
    else:
        table['Uppercase characters'] = 'x'
    
    if results ['lower']:
        table['Lowercase characters'] = u'\u2713'
    else:
        table['Lowercase characters'] = 'x'
    
    if results ['containsNums']:
        table['Digits'] = u'\u2713'
    else:
        table['Digits'] = 'x'
    
    if results['symbols']:
        table['Symbols'] = u'\u2713'
    else:
        table['Symbols'] = 'x'
    
    if results['dict']:
        table['Contained in a dictionary'] = 'x'
    else:
        table['Contained in a dictionary'] = u'\u2713'
        
        
    return table
    

'''
'''
def timeToCrack(password):
    requirements = passwordChecker(password)
    
    return 5
    
    
        
        
    
    