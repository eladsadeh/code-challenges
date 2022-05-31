import re

def matchingBraces(braces):
    ans = []
    for brace in braces:
        while '()' in brace or '[]' in brace or '{}' in brace:
            brace = brace.replace('()', '').replace('[]', '').replace('{}', '')
        
        if len(brace) > 0:
            ans.append('NO')
        else:
            ans.append('YES')
    return ans
    
print(matchingBraces(['[{}]','[{]}']))