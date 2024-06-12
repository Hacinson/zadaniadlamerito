def count_words(sentence):
    word_count = {}
    words = sentence.split()
    for word in words:
        cleaned_word = word.strip('.,!?"\'').lower()
        if cleaned_word in word_count:
            word_count[cleaned_word] += 1
        else:
            word_count[cleaned_word] = 1
    
    return word_count

sentence = "Testowe zdanie jest testowe, wooo testowe zdanie!"
word_count = count_words(sentence)

for word, count in word_count.items():
    print(f"{word}: {count}")
