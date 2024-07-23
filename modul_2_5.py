def get_matrix(n, m, value):
  matrix = []
  for str in range(n):
      row = []
  for stol in range(m):
      row = [value] * m
      matrix.append(row)
  return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)