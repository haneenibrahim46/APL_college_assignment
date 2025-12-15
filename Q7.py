sentences = [
    "I love Python",
    "Map and Lambda are useful",
    "Data Science is fun"
]

word_lengths = list(map(
    lambda s: list(map(lambda w: len(w), s.split())), 
    sentences
))

print(word_lengths)