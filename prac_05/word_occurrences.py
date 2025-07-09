"""
Word Occurrences
Estimate: 25 minutes
Actual:   55 minutes
"""


def main():
    user_sentence = get_sentence()
    words = create_list(user_sentence)
    longest_word = find_longest_word(words)
    word_to_count = create_dict(words)
    display_dictionary(word_to_count, longest_word)


def get_sentence():
    sentence = input("Type a sentence: ")
    return sentence


def create_dict(words):
    word_to_count = {}
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1
    return word_to_count


def find_longest_word(words):
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    max_length += 1
    return max_length


def create_list(sentence):
    words = sentence.split(" ")
    words.sort()
    return words


def display_dictionary(word_to_count,longest_word):
    for item in word_to_count:
        print(f"{item:<{longest_word}}: {word_to_count[item]}")


main()
