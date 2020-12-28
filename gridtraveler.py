def gridTraveler_brute(m,n) -> int:
    if m == 0 or n == 0: return 0
    if n == 1 and m == 1: return 1
    
    return gridTraveler_brute(m-1, n) + gridTraveler_brute(m, n-1)

def gridTraveler_memoization(m,n, memo = {}) -> int:
    key = str(m) + '-' + str(n)

    if key in memo: return memo[key]
    if m == 0 or n == 0: return 0
    if n == 1 and m == 1: return 1
    
    memo[key] = gridTraveler_memoization(m-1, n, memo) + gridTraveler_memoization(m, n-1, memo)
    return memo[key]

def gridTraveler_tabulation(m,n) -> int:
    
    table = [[0] * (n + 2) for _ in range(m + 2)]
    table[1][1] = 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            table[i+1][j] += table[i][j]
            table[i][j+1] += table[i][j]

    return table[m][n]

    #         print(f'--[{i}][{j}]') 
    #         p = '\n'.join(str(t) for t in table)
    #         print(f"{p}")
    # print(f'--1' 
    #       f'{table}')
    # # right-most column
    # for i in range(1, m):
    #     table[i + 1][-1] += table[i][-1]
    # print(f'--2' 
    #       f'{table}')
    
    # # bottom row
    # for j in range(1, n):
    #     table[-1][j + 1] += table[-1][j]

    # print(f'--3' 
    #       f'{table}')
    
if __name__ == "__main__":
    print(gridTraveler_tabulation(1,1))
    print(gridTraveler_tabulation(2,3))
    print(gridTraveler_tabulation(3,2))
    print(gridTraveler_tabulation(3,3))
    print(gridTraveler_tabulation(18,18))