def capitalize_first_letter(sentence):
    words = sentence.split()
    capitalized_words = [word[0].upper() + word[1:].lower() for word in words]
    return ' '.join(capitalized_words)

sentence = "hELLO wORLD hOW aRE yOU"
capitalized_sentence = capitalize_first_letter(sentence)
print(capitalized_sentence)
