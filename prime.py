number = int(input('Number: '))
if number < 2:
  print('INVALID')
for value in range(2, int(math.sqrt(number)) + 1):
    if number % value == 0:
      print(f'{number} is prime')
else:
  print(f'{number} is not prime')
