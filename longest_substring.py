from curses import longname


def lengthOfLongestSubstring(s: str) -> int:
        if s == '': return 0
        c_map = {} # Keep the last index of characters
        p = -1 # pointer to index we start to count from
        max_length = 0
        for i in range(len(s)):
            c = s[i]
        # if c is in the current substring
            if c in c_map and p < c_map[c]:
        # update the pointer
                p = c_map[c]
            else:
        # else, update the max length
                max_length = i - p if max_length < i-p else max_length
        # update the last index of c
            c_map[c] = i
            
        return max_length

print(lengthOfLongestSubstring('pwwkew'))