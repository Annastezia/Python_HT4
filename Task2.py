import math
N = int(input('Введите число: '))
simple = []
while N % 2 == 0:
      simple.append(2)
      N = N / 2
   
for i in range(3,int(math.sqrt(N))+1,2):
    while (N % i == 0):
        simple.append(i)
        N = N / i
if N > 2:
    simple.append(N)
print(simple)