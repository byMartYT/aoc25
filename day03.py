import time

time_start = time.perf_counter()

with open('day03.txt', 'r') as file:
  banks = file.readlines()

  sum1 = 0
  sum2 = 0

  for bank in banks:
    w = bank.strip()

    leftp = int(w[0])
    rightp = int(w[1])

    for i in range(1, len(w)):
      num = int(w[i])
      if num > leftp and i < len(w)-1:
        leftp = num
        rightp = 0
      elif num > rightp:
        rightp = num

    print(int(f'{leftp}{rightp}'))
    sum1 += int(f'{leftp}{rightp}')



  for bank in banks:
    w = bank.strip()

    current = ["0"] * 12

    for i in range(0, len(w)):
      num = int(w[i])
      changeable = -(len(w) - 12 - i)
      index = changeable
      if index < 0: index = 0
      

      if index >= len(current):
        current.extend(["0"] * (index - len(current) + 1))

      

      if index < len(current):
        for ind in range(index, len(current)):
          if int(current[ind]) < num:
            current[ind] = str(num)  
            current[ind+1:] = ["0"] * (len(current) - ind - 1)  
            break 

    sum2 += int(''.join(current))

print(sum1,sum2)

print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
