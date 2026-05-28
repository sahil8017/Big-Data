# matrix_mapreduce.py

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

# Map Step
mapped = []

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            mapped.append(((i, j), A[i][k] * B[k][j]))

print("Mapped Values:")
for item in mapped:
    print(item)

# Reduce Step
result = {}

for key, value in mapped:
    if key not in result:
        result[key] = 0
    result[key] += value

print("\nResult Matrix:")

rows = len(A)
cols = len(B[0])

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(result[(i, j)])
    print(row)