# Test your code Pieces
'''s = input()
n = 0 
for x in s[::-1]:
    if x == 'I':
        n += 1
    elif x == 'V':
        n += 5
    elif x == 'X':
        n += 10
    elif x == 'L':
        n += 50
    elif x == 'C':
        n += 100
    elif x == 'D':
        n += 500
    elif x == 'M':
        n += 1000

    if(s[x] == 'V' and s[x + 1] == 'I') or (s[x] == 'X' and s[x + 1] == 'I'):
        n -= 2
    elif (s[x] == 'X' and s[x + 1] == 'L') or (s[x] == 'X' and s[x + 1] == 'C') :
        n -= 20
    elif (s[x] == 'C' and s[x + 1] == 'D') or (s[x] == 'C' and s[x + 1] == 'D'):
        n -= 200

    
print(n)'''

val = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M':1000}
