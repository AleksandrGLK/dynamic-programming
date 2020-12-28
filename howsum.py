def howsum_brute(target: int, numbers: list):
    if target == 0: return []
    if target < 0: return None

    for num in numbers:
        remainder = target - num
        result = howsum_brute(remainder, numbers)
        if result is not None:
            return [*result, num]
    return None

def howsum_memoization(target: int, numbers: list):
    memo = {}

    def helper(target, numbers):
        if target in memo: return memo[target]
        if target == 0: return []
        if target < 0: return None

        for num in numbers:
            remainder = target - num
            result = helper(remainder, numbers)
            if result is not None:
                memo[target] = [*result, num]
                return memo[target]
        
        memo[target] = None
        return None
    
    return helper(target, numbers)

def howsum_tabulation(target: int, numbers: list):
    
    table = [None for _ in range(target+1)]
    table[0] = []

    for i in range(len(table)):
        if table[i] is not None:
            for num in numbers:
                if i + num < len(table):
                    table[i+num] = [*table[i],num]

    return table[-1]


if __name__ == "__main__":
    print(howsum_tabulation(7, [2,3]))
    print(howsum_tabulation(7, [5,4,7,3]))
    print(howsum_tabulation(7, [2,4]))
    print(howsum_tabulation(8, [2,3,5]))
    print(howsum_tabulation(300, [7,14]))