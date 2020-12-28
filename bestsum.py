def bestsum_brute(target: int, numbers: list):
    if target == 0: return []
    if target < 0: return None
     
    shortestcombination = None

    for num in numbers:
        remainder = target - num
        remaindercombination = bestsum_brute(remainder, numbers)
        if remaindercombination is not None:
            combination = [*remaindercombination, num]
            if shortestcombination is None or len(combination) < len(shortestcombination):
                shortestcombination = combination
    
    return shortestcombination

def bestsum_memoization(target: int, numbers: list):
    memo = {}

    def helper(target, numbers):

        if target in memo: return memo[target]
        if target == 0: return []
        if target < 0: return None
        
        shortestcombination = None

        for num in numbers:
            remainder = target - num
            remaindercombination = helper(remainder, numbers)
            if remaindercombination is not None:
                combination = [*remaindercombination, num]
                if shortestcombination is None or len(combination) < len(shortestcombination):
                    shortestcombination = combination
        
        memo[target] = shortestcombination
        return shortestcombination

    return helper(target, numbers)

def bestsum_tabulation(target: int, numbers: list):

    table = [None for _ in range(target + 1)]
    table[0] = []

    for i in range(len(table)):
        if table[i] is not None:
            for num in numbers:
                combination = [*table[i], num]
                if i+num < len(table):
                    if not table[i+num] or len(table[i+num]) > len(combination):
                        table[i+num] = [*table[i], num]
    return table[-1]

if __name__ == "__main__":
    print(bestsum_tabulation(7, [5,3,4,7]))
    print(bestsum_tabulation(8, [2,3,5]))
    print(bestsum_tabulation(8, [1,4,5]))
    print(bestsum_tabulation(100, [1,2,5,25]))
