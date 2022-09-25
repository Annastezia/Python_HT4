from random import randint
import itertools

k = randint(2, 10)

def get_ratios(k):
    ratios = [randint(0, 10) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10) 
    return ratios

def get_polynomial(k, ratios):
    num = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, num, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')


ratios = get_ratios(k)
print(ratios)
polynom1 = get_polynomial(k, ratios)
print(polynom1)

with open('File.txt', 'w') as data:
    data.write(polynom1)