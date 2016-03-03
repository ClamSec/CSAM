import sys, os, hashlib

def dictionaryAttack(hash):
    returnString = "Password not cracked, not in dictionary."
    file = open("app/basicDictionary.txt")
    for word in file:
        candidate = hashlib.md5(word.rstrip().encode('utf-8')).hexdigest()
        if candidate == hash:
            returnString = "Password cracked."
    return returnString
