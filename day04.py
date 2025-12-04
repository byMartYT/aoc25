import time

time_start = time.perf_counter()

with open('day04.txt', 'r') as file:
  lines = file.readlines()

  result = []

  for i in range(0, len(lines)):
    newLine = lines[i].strip()
    result.append(list(newLine)) 
  allPapers = 0

  while True:
    papers = 0
    for i in range(0, len(result)):
      for j in range(0, len(result[i])):
        nachbarn = 0

        if result[i][j] == '.': continue
        if result[i][j] == 'x': continue

        for k in range(i-1, i+2):
          for l in range(j-1, j+2):
            if k == i and l == j: continue

            if k < 0 or l < 0: continue
            if k >= len(result) or l >= len(result[i]): continue

            if result[k][l] == '@': nachbarn += 1
        if(nachbarn < 4): 
          result[i][j] = 'x'
          papers += 1        

      print(''.join(result[i]))  
    print(papers)
    print('_________________')
    if papers == 0:
      break
    else: 
      allPapers += papers

  print(allPapers)







print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')