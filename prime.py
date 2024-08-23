number = int(input('Number: '))
if number < 2:
  print('INVALID')
for i in range(2, int(math.sqrt(number)) + 1):
    if number % i == 0:
        print(f'{number} is not prime')
        break
    else:
        print(f'{number} is prime')
