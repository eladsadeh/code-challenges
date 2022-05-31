class SimpleTrie:
    # create empty dictionary
    def __init__(self):
        self.trie = {}
    
    # if string exist in exist then return true
    # otherwise add the string to trie
    def check_prefix(self, s):
        # pointer to current node (walker)
        w = self.trie # start from the top
        for i,c in enumerate(s):
        # if current character is not in current node
        # add it as either end of word or empty dictionary
            if c not in w:
                # w[c] = {"!": None} if i == len(s) - 1 else {}
                w[c] = 'eow' if i == len(s) - 1 else {}
            else:
        # return true if it's end of word or the last character.
        # If it's end of word than an existing word is a prefix
        # of the current word. If it's the end of the current word
        # than the current word is a prefix of existing word
                if w[c] == 'eow' or i == len(s) - 1:
                # if "!" in w[c] or i == len(s) - 1:
                    return True
        # set walker to current node        
            w = w[c]
        
        return False

        
def noPrefix(words):
    st = SimpleTrie()
    for word in words:
        if st.check_prefix(word):
            print("BAD SET")
            print(word)
            return
    
    print("GOOD SET")

noPrefix(['aab','bcd','aabgab'])
# noPrefix(['acb', 'defgab', 'abcde', 'aabcde', 'bbbbbbbbbb', 'jabjjjad'])