def canSum_brute(target: int, numbers: list) -> bool:

    if target == 0: return True
    if target < 0: return False
    

    for num in numbers:
        remainder = target - num
        if canSum_brute(remainder, numbers):
            return True

    return False

def canSum_memoization(target: int, numbers: list) -> bool:
    memo = {}
    if target in numbers: return True
    
    def helper(target, numbers):

        if target in memo: return memo[target]
        if target == 0: return True
        if target < 0: return False
    

        for num in numbers:
            remainder = target - num
            if helper(remainder, numbers):
                memo[target] = True
                return True

        memo[target] = False
        return False

    return helper(target, numbers)

def canSum_tabulation(target: int, numbers: list):

    table = [False for _ in range(0, target+1)]
    table[0] = True

    for t in range(len(table)):
        if table[t]:
            for num in numbers:
                if t+num < len(table):
                    table[t+num] = True
    return table[-1]


if __name__ == "__main__":
    print(canSum_tabulation(7, [2,3]))
    print(canSum_tabulation(7, [5,4,7,2,3]))
    print(canSum_tabulation(7, [2,4]))
    print(canSum_tabulation(8, [2,3,5]))
    print(canSum_tabulation(300, [7,14]))