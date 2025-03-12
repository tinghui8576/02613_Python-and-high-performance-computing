def listsum(l):
    sum = 0
    for v in l:
        sum += v
    return sum

l = [1, 2, 3, 3, 2, 2, 4]
def deduplicate(l):
    return list(set(l))

tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
def sorttuples(tuples):
    return sorted(tuples, key=lambda x: x[1])

#%%
lists = [1, 2, 3, 4] 
def squarecubes(lists):
    l1 = [l**2 for l in lists]
    l2 = [l**3 for l in lists]

