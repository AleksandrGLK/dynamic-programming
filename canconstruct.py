def canConstruct_brute(target: str, wordbank: list):
    if target == '': return True
       
    for word in wordbank:
        if word == target[:len(word)]:
            if canConstruct_brute(target[len(word):], wordbank):
                return True
    
    return False

def canConstruct_memoization(target: str, wordbank: list):

    memo = {}

    def helper(target, wordbank):

        if target in memo: return memo[target]
        if target == '': return True
        
        for word in wordbank:
            if word == target[:len(word)] and len(target) >= len(word):
                if helper(target[len(word):], wordbank):
                    memo[target] = True
                    return True
        
        memo[target] = False
        return False
    
    return helper(target, wordbank)

def canConstruct_tabulation(target: str, wordbank: list):

    table = [False for _ in range(len(target) + 1)]
    table[0] = True

    for i in range(len(table)):
        if table[i] is True:
            for word in wordbank:
                if target[i:].startswith(word):
                    table[i+len(word)] = True
    return table[-1]

if __name__ == "__main__":
    print(canConstruct_tabulation('abcdef', ['ab','abc','cd','def','abcd']))
    print(canConstruct_tabulation('skateboard', ['bo','rd','ate','t', 'ska', 'boar']))
    print(canConstruct_tabulation('enterapotentpot', ['a','p','ent','enter', 'ot', 'o','t']))
    print(canConstruct_tabulation('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee', 'eeeee', 'eeeeee']))