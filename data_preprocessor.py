# Stage 1: Uniformaty - converting to lowercase and eradicating whitespaces
# Stage 2: Standardization of Abbreviations
# Stage 3: Address Parsing and Normalization
# Stage 4: Spelling Correction - using Levenshtein distance
# Stage 5: Manual Review & percentage accuracy

# imports
import string
from nltk.tokenize import word_tokenize
import pandas as pd
from nltk.metrics.distance import edit_distance


def load_corpus(file_name, pandas=False):
    if pandas==True:
        df = pd.read_csv(file_name, sep="\t", header=None, names=["Neighborhood"])
        return df
    else:
        with open(file_name, "r") as file:
            neighborhood_names = file.readlines()    
        refined_name_list = [name.strip() for name in neighborhood_names]
        return refined_name_list
    

def create_corpus(file_name, data):
    # Process the data
    with open(file_name, "w") as file:
        for item in data:
            file.write(item + "\n")
    print(f"File '{file_name}' has been created.")


def lowercase_conversion(text_str):
    return text_str.lower()


def remove_punctuation(text_str):
    punctuation = string.punctuation 
    return text_str.translate(str.maketrans('', '', punctuation))


def remove_extra_spaces(text_str):
    words = text_str.split()
    cleaned_text = ' '.join(words)
    return cleaned_text


def standard_tokenization(text_str):
    return word_tokenize(text_str)


def word_correction_levenshtein(word, word_corpus):
    temp = [(edit_distance(word, w),w) for w in word_corpus]
    # return sorted(temp, key = lambda val:val[0])[0][1]

    if len(temp) > 1: 
        temp = [min(temp, key=lambda t: t[0])]

    # return temp[0][1]
    return temp


def standard_abbreviations_fix(address_str, abbreviation_mapping):
    words = address_str.split()
    standardized_words = [abbreviation_mapping.get(word, word) for word in words]
    standardized_address = ' '.join(standardized_words)
    return standardized_address


sample1 = 'House # C-38, Block 8, Gulshan-e-Iqbal, Karachi'

# ans = lowercase_conversion(sample1)
# ans = remove_punctuation(ans)

# print(lowercase_conversion(ans))

# ans = standard_tokenization(sample1)
# print(ans)

fname = "karachi_neighbourhoods.txt"

correct_words = ['gulshan e hadeed', 'gulshan e iqbal', 'defence', 'clifton', 'meher plaza', 'al murtaza heights', 'al murtaza height']

incorrect_words= ['gulshen iqbal', 'defnse', 'klifton', 'mehar plaza', 'al murteza heights']


for word in incorrect_words:
    print(word_correction_levenshtein(word, correct_words))

