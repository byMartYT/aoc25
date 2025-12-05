import time

time_start = time.perf_counter()



with open('day05.txt') as file:
  fresh = 0
  valids = []
  filling_valids = True
  valids_amount = 0

  for line in file.readlines():
    if line == '\n':
      filling_valids = False
      continue

    if filling_valids:
      x, y = line.strip().split('-')
      valids.append((int(x),int(y)))
    else: 
      num = int(line.strip())
      for x,y in valids:
        if num >= x and num <= y:
          fresh += 1
          break

  valids.sort(key=lambda tup: tup[1])

  while True:
    new_valids = []
    change = False
    i = 0
    while i < len(valids):
      if i < len(valids) - 1 and valids[i][1] >= valids[i+1][0]:
        new_valids.append((min(valids[i][0], valids[i+1][0]), max(valids[i][1], valids[i+1][1]))) 
        change = True
        i += 2
      else:
        new_valids.append(valids[i])
        i += 1
    if not change: break
    valids = new_valids

  print(valids)

  for x,y in valids:
    valids_amount += y+1-x

print(fresh, valids_amount)





print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')