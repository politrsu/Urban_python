my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
nul = 0
while len(my_list):       # while True как вариант
  if my_list[nul] > 0:
    print(my_list[nul])
    nul = nul + 1
    continue
  elif my_list[nul] == 0:
    nul = nul + 1
    continue
  else:
    break