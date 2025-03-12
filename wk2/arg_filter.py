import sys

def odd(i):
    if int(i) % 2 == 0: 
        return i
    
odds = [int(o) for o in filter(odd, sys.argv[1:])]

print(odds)