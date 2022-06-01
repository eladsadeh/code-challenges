# convert string to intger
# input: '   -448 word', '+98s', '0047b'
def myAtoi(s: str) -> int:
        s = s.strip(' ')
        if len(s) == 0:
            return 0

        res = 0
        sign = 1
        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            s= s[1:]
        
        i = 0
        while len(s) > i and s[i].isdigit():
            # ans += s[i]
            res = res*10 + int(s[i])
            i += 1
        
        return max(-2147483648, min(sign*res,2147483647))