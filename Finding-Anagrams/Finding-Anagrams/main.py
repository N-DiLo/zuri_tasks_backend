# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

word = "conservation"
anagram = "conversation"

word = word.replace(" ", "").upper()
anagram = anagram.replace(" ", "").upper()

#print words if they are anagrams
print(sorted(word) == sorted(anagram))


def find_anagram(word, anagram):
    # [assignment] Add your code here

    words = dict()

    if len(word) != len(anagram):
        return False

#checks the number of letter in the given word
    for w in word:
        if w in words:
            words[w] += 1
        else:
            words[w] = 1
#checks if the same number & letter of words are used above
    for w in anagram:
        if w in words:
            words[w] -= 1
        else:
            words[w] = 1

#returns False if both words ain't corresponding
    for w in words:
        if words[w] != 0:
            return False

    return True

print((word, anagram))
#prints the word & anagram
