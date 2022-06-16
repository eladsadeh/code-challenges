# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
def letterCombinations(self, digits: str) -> List[str]:
    dic = {'2': "abc", '3':"def", '4':'ghi', '5':'jkl', '6':'mno',
            '7':'pqrs', '8':'tuv','9':'wxyz'}

    if len(digits) == 0:
        return []
    
    comb = list(dic[digits[0]])
    for d in digits[1:]:
        temp = []
        for c in comb:
            for l in list(dic[d]):
                temp.append(c+l)
        comb = list(temp)
        
    return comb