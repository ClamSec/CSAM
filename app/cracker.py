import sys, os, hashlib, string, itertools
from timeit import default_timer as timer

SYMBOLS = '!@#$%^&*(){}[]:";<>?,./\'\\' #testing, may be incomplete

'''
Given a password, a local dictionary is enumerated to see
how quickly a match can be found. A dictionary is returned giving
information about the attack.
'''
def dictionaryAttack(password):
    
    results = {}
    file = open("app/basicDictionary.txt")
    start = timer()
    count = 0
    flag = False
    for word in file:
        count += 1
        if word.rstrip() == password:
            flag = True
            break
    stop = timer()
    duration = stop - start
    results['count'] = count
    results['duration'] = round(duration, 2)
    results['rate'] = int(count / duration)
    results['found'] = flag
    return results
    

'''
Given a password, details such as length and types of characters will be used 
to craft a brute force attack against the password. A dictionary is returned giving
information about the attack.
'''
def bruteForceAttack(password):
    
    results = {}
    
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
    flag = False
    for p in gen:
        count += 1
        if p == password:
            flag = True
            break
    stop = timer()
    duration = stop - start
    results['count'] = count
    results['duration'] = round(duration, 2)
    results['rate'] = int(count / duration)
    results['found'] = flag
    return results

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
keys are requirements and their values are whether or not they have been met. 
'''
def passwordChecker(password):
    
    MINIMUM_NUMBER_OF_CHARS = 8
    
    results = {}
    
    containsLower = False
    containsUpper = False
    containsSymbols = False
    containsNumbers = False
    numberofchars = len(password)
    results['numChars'] = numberofchars
    

    for ch in password:
        if ch in SYMBOLS:
            containsSymbols = True
        elif ch in string.digits:
            containsNumbers = True
        elif ch in string.ascii_uppercase:
            containsUpper = True
        elif ch in string.ascii_lowercase:
            containsLower = True
            
    if numberofchars >= MINIMUM_NUMBER_OF_CHARS:
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
        
    if dictionaryAttack(password)['found'] == True:
        results['dict'] = True
    else:
        results['dict'] = False
        
    return results

'''
Create a dictionary that will be used to display a table
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
        table['Not contained in a dictionary'] = 'x'
    else:
        table['Not contained in a dictionary'] = u'\u2713'
        
    return table
 
    
'''
Create a dictionary that will be used to display a table
'''
def makeCrackTable(password, method):
    
    table = {}
    results = {}
    
    if method == 'brute':
        results = bruteForceAttack(password)
    
    elif method == 'dict':
        results = dictionaryAttack(password)
        
    table['Time spent looking for the password'] = '{:,.2f} s'.format(results['duration'])
    table['# of passwords tried'] = '{:,}'.format(results['count'])
    table['Rate'] = '{:,}'.format(results['rate']) + ' passwords / second'
    table['Found'] = results['found']
      
    return table

'''
Estimates the time that it will take for a password to be cracked, returns a
dictionary that represents that information
'''
def timeToCrack(password):
    
    results = passwordChecker(password)
    table = {}
    pool = 0
    rate = 100000000
    
    if results['upper']:
        pool += 26

    if results ['lower']:
        pool += 26
    
    if results ['containsNums']:
        pool += 10
    
    if results['symbols']:
        pool += len(SYMBOLS)
        
    table['Pool'] = pool
    table['Length of password'] = results['numChars']
    possible = pool ** results['numChars']
    table['All possible combinations'] = '{:,}'.format(possible)
    table['Rate'] = '{:,}'.format(rate) + ' passwords / second'
    #if the number is really small, show decimal places
    if float(possible) / rate > 1:
        table['Time needed to crack'] = '{:,.0f} s'.format(float(possible) / rate)
    else:
        table['Time needed to crack'] = '{:,.3f} s'.format(float(possible) / rate)
        
    return table