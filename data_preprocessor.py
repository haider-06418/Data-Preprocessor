# Stage 1: Uniformaty - converting to lowercase and eradicating whitespaces

# imports
import string
from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize import word_tokenize
# from nltk import word_tokenize


def lowercase_conversion(text_str):
    return text_str.lower()

def remove_punctuation(text_str):
    punctuation = string.punctuation 
    return text_str.translate(str.maketrans('', '', punctuation))

def tokenization(text_str):
    return word_tokenize(text_str)


sample1 = 'House  # C-38,  Block  8 , Gulshan-e -Iqbal, Karachi'

# ans = lowercase_conversion(sample1)
# ans = remove_punctuation(ans)
# print(lowercase_conversion(ans))

ans = tokenization(sample1)
print(ans)