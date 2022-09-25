from random import *
sequence = [int(randint(0,10)) for _ in range(int(input('Введите количество элементов: ')))]
print(sequence)

unique = [i for i in sequence if sequence.count(i)==1]
print(unique)