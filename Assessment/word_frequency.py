def word_frequency(sentence: str) -> dict:
    sentence = sentence.lower()
    words = ''.join(letter for letter in sentence if letter.isalnum() or letter.isspace()).split()
    return {word: words.count(word) for word in set(words)}

print(word_frequency("Hello world! Hello"))






