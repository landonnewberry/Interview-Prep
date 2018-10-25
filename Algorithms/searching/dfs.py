from pprint import pprint

test = [['O','O','X','O'],
        ['X','X','O','X'],
        ['O','O','O','X'],
        ['X','X','O','O']]

def max_connection(A):
    row_dim = len(A)
    col_dim = len(A[0])
    visited = dict()
    for i in range(row_dim):
        for j in range(col_dim):
            visited[(i,j)] = False
    def check(r, c, s):
        if (r < 0) or (c < 0) or (r >= row_dim) or (c >= col_dim) or (visited[(r,c)]) or (A[r][c] != s):
            return []
        visited[(r,c)] = True
        return [(r,c)] + check(r + 1, c, s) + check(r - 1, c, s) + check(r, c + 1, s) + check(r, c - 1, s)
    maximum = 0
    group = None
    for i in range(row_dim):
        for j in range(col_dim):
            if not visited[(i,j)]:
                c = check(i, j, A[i][j])
                if len(c) > maximum:
                    maximum = len(c)
                    group = c
    return group

if __name__ == '__main__':
    pprint(test)
    pprint(max_connection(test))

