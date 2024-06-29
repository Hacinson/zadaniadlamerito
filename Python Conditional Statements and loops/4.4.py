def reverse_word():
    word = input("Enter a word: ")
    
    reversed_word = ""
    
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    
    print(f"Reversed word: {reversed_word}")

reverse_word()
