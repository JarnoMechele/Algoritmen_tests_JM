number = 0
total = 0
while (number < 10000):
  if number % 7 == 0 or number % 9 == 0:
    print (number)
    total += number
  number = number + 1
print ('sum is:', total)