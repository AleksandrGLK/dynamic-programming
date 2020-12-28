def fibonachi_brute(num : int) -> int:
    if num <= 2: return 1
    return fibonachi_brute(num - 1) + fibonachi_brute(num - 2)

def fibonachi_memoization(num : int, memo = {}) -> int:
    if num <= 2: return 1
    if num in memo: return memo[num]
    memo[num] = fibonachi_memoization(num - 1, memo) + fibonachi_memoization(num - 2, memo)
    return memo[num]

def fibonachi_tabulation(num:int) -> int:
    
    table = [0 for _ in range(num+2)]
    table[1] = 1

    for i in range(num):
        table[i+1] += table[i]
        table[i+2] += table[i]
    
    return table[num]
    
if __name__ == "__main__":
    print(fibonachi_tabulation(6))
    print(fibonachi_tabulation(7))
    print(fibonachi_tabulation(8))
    print(fibonachi_tabulation(50))