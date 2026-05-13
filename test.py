# Test your code Pieces
from itertools import zip_longest
wrd1 = 'heeraaaaaaaa'
wrd2 = 'shanker'
for x,y in zip_longest(wrd1,wrd2, fillvalue ="" ):
    pairs = x,y
    result = "".join(ch for pair in pairs for ch in pair)
    



""" if len(wrd1)>len(wrd2)
        merger[len(wrd1):len(wrd2)]
        pass"""