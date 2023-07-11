def duplicate_encode(word):
    #your code here
    word = word.lower()
    freq = {}
    
    for letter in word:
        if letter not in freq:
            freq[letter] = 0
        freq[letter] += 1
    
    ans = []
    for letter in word:
        if freq[letter] == 1:
            ans.append('(')
        else:
            ans.append(')')
    return "".join(ans)
