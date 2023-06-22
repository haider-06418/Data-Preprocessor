# Stage 1: Uniformaty - converting to lowercase and eradicating whitespaces

# imports
import string
from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize import word_tokenize
import pandas as pd


def load_corpus(file_name, pandas=False):
    if pandas==True:
        df = pd.read_csv(file_name, sep="\t", header=None, names=["Neighborhood"])
        return df
    else:
        with open(file_name, "r") as file:
            neighborhood_names = file.readlines()    
        refined_name_list = [name.strip() for name in neighborhood_names]
        return refined_name_list


def lowercase_conversion(text_str):
    return text_str.lower()


def remove_punctuation(text_str):
    punctuation = string.punctuation 
    return text_str.translate(str.maketrans('', '', punctuation))


def standard_tokenization(text_str):
    return word_tokenize(text_str)


sample1 = 'House  # C-38,  Block  8 , Gulshan-e-Iqbal, Karachi'

# ans = lowercase_conversion(sample1)
# ans = remove_punctuation(ans)

# print(lowercase_conversion(ans))

# ans = standard_tokenization(sample1)
# print(ans)

fname = "karachi_neighbourhoods.txt"

# levintiaion distance functions, indiviauals and for lists