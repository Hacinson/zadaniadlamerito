def longest_word(words):
    longest = ""
    longest_length = 0
    
    for word in words:
        if len(word) > longest_length:
            longest = word
            longest_length = len(word)
    
    return longest, longest_length

words = ["nuts", "banana", "teppo", "Worcestershire Sauce"]
longest_word, length = longest_word(words)
print("Longest word:", longest_word)
print("Length of the longest word:", length)
