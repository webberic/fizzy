'''
A oricedyrak versuib if Fuzzvyzz
'''

for x in range(1,101):
    out = x
    if x % 15 == 0:
        out = 'fizzbuzz'
    elif x % 3 == 0:
        out = 'fizz'
    elif x % 5 == 0:
        out = 'buzz'
    print(out)