with open("input11.txt") as input:
    content = input.read()

grid_str = content.split("\n")
grid_str.pop()

grid = []
greatest = 0

for line in grid_str:
    line = line.split()
    x = []
    for elem in line:
        num = int(elem)
        x.append(num)
    grid.append(x)

# horizontal:
for row in range(len(grid)):
    for column in range(len(grid[0]) - 3):
        a = column
        b = a + 1
        c = b + 1
        d = c + 1
        mult = grid[row][a] * grid[row][b] * grid[row][c] * grid[row][d]
        if mult > greatest:
            greatest = mult
# vertical:
for row in range(len(grid) - 3):
    for column in range(len(grid[0])):
        e = row
        f = e + 1
        g = f + 1
        h = g + 1
        mult = grid[e][column] * grid[f][column] * grid[g][column] * grid[h][column]
        if mult > greatest:
            greatest = mult
# diag\:
for row in range(len(grid) - 3):
    for column in range(len(grid[0]) - 3):
        a = column
        b = a + 1
        c = b + 1
        d = c + 1
        e = row
        f = e + 1
        g = f + 1
        h = g + 1
        mult = grid[e][a] * grid[f][b] * grid[g][c] * grid[h][d]
        if mult > greatest:
            greatest = mult
# diag/:
for row in range(4, len(grid)):
    for column in range(len(grid[0]) - 3):
        a = column
        b = a + 1
        c = b + 1
        d = c + 1
        i = row
        j = i - 1
        k = j - 1
        l = k - 1
        mult = grid[i][a] * grid[j][b] * grid[k][c] * grid[l][d]
        if mult > greatest:
            greatest = mult
print(greatest)
