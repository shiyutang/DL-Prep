n, m = list(map(int, input().split()))
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

if n == 0 and m == 0:
    print()
else:
    for i in range(n):
        for j in range(m):
            cnt = 1
            tmp = mat[i][j]

            for (ii, jj) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if not 0 <= ii < n or not 0 <= jj < m:
                    continue
                else:
                    cnt += 1
                    tmp += mat[ii][jj]

            mat[i][j] = round(tmp / cnt)

            if j != m - 1:
                print(mat[i][j], end=' ')

        print(mat[i][-1])

# 2 2
# 10 22
# 30 40