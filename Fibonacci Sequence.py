number = int(input('How many times do u want Fibonacci Sequence to run: '))
a = 0 
b = 1
for i in range(number):
    a, b = b, a + b
print(a)
