def allconstruct_brute(target: str, wordbank: list):
    if target == '': return [[]]

    result = []
    for word in wordbank:
        if word == target[:len(word)] and len(target) >= len(word):
            answer = allconstruct_brute(target[len(word):], wordbank)
            targetways = [[word] + way for way in answer]
            if targetways:
                result.extend(targetways)
    return result

def allconstruct_memoization(target: str, wordbank: list):
    
    memo = {}
    
    def hepler(target, wordbank):

        if target == '': return [[]]
        if target in memo: return memo[target]

        result = []
        for word in wordbank:
            if word == target[:len(word)] and len(target) >= len(word):
                answer = hepler(target[len(word):], wordbank)
                targetways = [[word] + way for way in answer]
                if targetways:
                    result.extend(targetways)
        memo[target] = result
        return result

    return hepler(target, wordbank)

def allconstruct_tabulation(target: str, wordbank: list):

    table = [[] for _ in range(len(target)+1)]
    table[0] = [[]]

    for i in range(len(table)):
        for word in wordbank:
            if target[i:].startswith(word):
                # combination = [way + [word] for way in table[i]]
                combination = map(lambda x: x + [word], table[i])
                table[i+len(word)].extend(combination)
    return table[-1]

def all_construct(target, word_bank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]
    for i in range(len(target)):
        for word in word_bank:
            if target[i : i + len(word)] == word:
                new_combinations = [combination + [word] for combination in table[i]]
                table[i + len(word)].extend(new_combinations)
    return table[-1]
 
if __name__ == "__main__":
    print(allconstruct_tabulation('purple', ['purp','p','ur','le','purpl']))
    print(allconstruct_tabulation('abcdef', ['ab','abc','cd','def','abcd','ef','c']))
    print(allconstruct_tabulation('skateboard', ['bo','rd','ate','t', 'ska', 'boar']))
    # print(all_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee', 'eeeee', 'eeeeee']))
