# install nltk and punkt_tab

import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize,sent_tokenize

# Sample text
text = "I love programming. It's so much fun!"

# Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentences:", sentences)

# Word Tokenization
words = word_tokenize(text)
print("Words:", words)

