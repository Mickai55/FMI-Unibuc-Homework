fin = open('E:\Informatica\z.in.txt')

n, k = map(int, next(fin).split())

BASE_CASE = [[1, 2],
             [3, 4]]


def find(dim, x, y):
    # print(f'({x}, {y}) in {dim}')

    if dim == 1:
        return BASE_CASE[x - 1][y - 1]

    half = dim // 2
    num = dim ** 2
    if x <= half:
        if y <= half:
            # Cadranul I
            return find(half, x, y)
        else:
            # Cadranul II
            return num // 4 + find(half, x, y - half)
    else:
        if y <= half:
            # Cadranul III
            return num // 2 + find(half, x - half, y)
        else:
            # Cadranul IV
            return 3 * num // 4 + find(half, x - half, y - half)


dim = 2 ** n
with open('E:\Informatica\z.out.txt', 'w') as fout:
    for _ in range(k):
        x, y = map(int, next(fin).split())
        print(find(dim, x, y), file=fout)