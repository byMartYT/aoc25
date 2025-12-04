import re, time

time_start = time.perf_counter()

# read file
with open("day02test.txt", 'r') as file:
  lines = file.readlines()[0].split(',')

  sum = 0

  for line in lines:
    start = int(line.split('-')[0])
    end = int(line.split('-')[1])

    for i in range(start, end + 1):
      number = str(i)
      e = re.findall(r'^(\d+)\1+$', number)

      if e: 
        sum += i

      
  
  print(sum)

print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
