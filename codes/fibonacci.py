total = 0
number_one = 0
number_two = 1

sumoffodd = number_one + number_two
while (sumoffodd < 4000000):
  if sumoffodd % 2:
    total += sumoffodd
  number_one = number_two
  number_two = sumoffodd
  sumoffodd = number_one + number_two

print(sumoffodd)