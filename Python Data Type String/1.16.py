def find_smallest_largest_words(string):
    words = string.split()
    smallest_word = min(words, key=len)
    largest_word = max(words, key=len)
    
    return smallest_word, largest_word

string = "Drink leche or else"
smallest, largest = find_smallest_largest_words(string)

print(string)
print("Smallest word:", smallest)
print("Largest word:", largest)
