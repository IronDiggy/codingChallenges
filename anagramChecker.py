def anagrams(word, words):
    # your code here
    isAnAnagram = []
    wordCompare = list(word)
    wordCompare.sort()

    for w in words:
        splitWord = list(w)
        splitWord.sort()
        # print(splitWord)

        if splitWord == wordCompare:
            isAnAnagram.append(w)
            # print(w + " is an anagram of " + word)
        else:
            # print(w + " is not an anagram of " + word)
            continue
    return isAnAnagram


print(anagrams("abba", ["aabb", "abcd", "bbaa", "dada"]))
