# find all the words in a sentence which does not appear in a subsentence.
# the subsentence must maintain the word order
def missing_words(s, t):
    sentence = s.split(' ')
    sub = t.split(' ')

    # print(sentence)
    # print(sub)

    j = 0
    missing = []
    for word in sentence:
        if j < len(sub) and word == sub[j]:
            j += 1
        else:
            missing.append(word)
    
    print(missing)

missing_words("I am using computer am to improve my computer work","computer am to improve",)