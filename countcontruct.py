def countconstruct_brute(target: str, wordbank: list):
    if target == '': return True

    total = 0
    for word in wordbank:
        if word == target[:len(word)] and len(target) >= len(word):
            total += countconstruct_brute(target[len(word):], wordbank)

    return total


def countconstruct_memoization(target: str, wordbank: list):

    memo = {}

    def helper(target, wordbank):
        
        if target == '': return True
        if target in memo: return memo[target]
        
        total = 0
        for word in wordbank:
            if word == target[:len(word)] and len(target) >= len(word):
                total += helper(target[len(word):], wordbank)

        memo[target] = total
        return total

    return helper(target, wordbank)

def countconstuct_tabulation(target: str, wordbank: list):

    table = [0 for _ in range(len(target)+1)]
    table[0] = 1

    for i in range(len(table)):
        for word in wordbank:
            if target[i:].startswith(word):
                table[i+len(word)] += table[i]
    return table[-1]

if __name__ == "__main__":
    print(countconstuct_tabulation('purple', ['purp','p','ur','le','purpl']))
    print(countconstuct_tabulation('abcdef', ['ab','abc','cd','def','abcd']))
    print(countconstuct_tabulation('skateboard', ['bo','rd','ate','t', 'ska', 'boar']))
    print(countconstuct_tabulation('enterapotentpot', ['a','p','ent','enter', 'ot', 'o','t']))
    print(countconstuct_tabulation('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee', 'eeeee', 'eeeeee']))
