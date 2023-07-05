# Stage 1: Uniformaty - converting to lowercase and eradicating whitespaces
# Stage 2: Standardization of Abbreviations
# Stage 3: Address Parsing and Normalization
# Stage 4: Spelling Correction - using Levenshtein distance
# Stage 5: Manual Review & percentage accuracy

# imports
import string
import json
from nltk.tokenize import word_tokenize
import pandas as pd
from nltk.metrics.distance import edit_distance


def load_corpus(file_name, pandas=False, header = False):
    if pandas==True:
        if header == False:
            df = pd.read_csv(file_name, sep="\t", header=None, names=["Neighborhood"])
        else:
            df = pd.read_csv(file_name, encoding='latin1')
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


def create_dataframe(columns, data = None, datacheck=False):
    if datacheck == True:
        df = pd.DataFrame(data, columns=columns)
    else:
        df = pd.DataFrame(columns=columns)
    return df


def load_json(file_name):
    with open(file_name, 'r') as file:
        dictionary = json.load(file)
    return dictionary


def lowercase_conversion(text_str):
    return text_str.lower()


def remove_punctuation(text_str, commas = False):
    if commas == True:
        punctuation = string.punctuation.replace(",", "")
        # punctuation = punctuation.replace("#", "")
        # punctuation = punctuation.replace("-", "")
    else:
        punctuation = string.punctuation 
    return text_str.translate(str.maketrans('', '', punctuation))


def remove_extra_spaces(text_str, allspaces = False):
    if allspaces == True:
        cleaned_text = text_str.replace(" ", "")
        return cleaned_text
    else:
        words = text_str.split()
        cleaned_text = ' '.join(words)
        return cleaned_text


def standard_tokenization(text_str, space=False):
    if space == True:
        return word_tokenize(text_str)
    else:
        tokens = text_str.split(",")
        return tokens


def word_correction_levenshtein(word, word_corpus):
    temp = [(edit_distance(word, w),w) for w in word_corpus]
    # return sorted(temp, key = lambda val:val[0])[0][1]

    if len(temp) > 1: 
        temp = [min(temp, key=lambda t: t[0])]

    # return temp[0][1]
    return temp


def standard_abbreviations_fix(address_str, abbreviation_mapping):
    words = address_str.split()
    standardized_words = [abbreviation_mapping.get(word.translate(str.maketrans('', '', string.punctuation)), word) for word in words]
    standardized_address = ' '.join(standardized_words)
    return standardized_address


def check_address_type(address):
    house_keywords = ['house', 'house no', 'house number', 'house #', 'plot']
    apartment_keywords = ['flat', 'flat no', 'flat number', 'flat #', 'apartment', 'building', 'suite']

    house_found = any(keyword in address for keyword in house_keywords)
    apartment_found = any(keyword in address for keyword in apartment_keywords)

    if house_found and apartment_found:
        return 'apartment'
    elif house_found:
        return 'house'
    elif apartment_found:
        return 'apartment'
    else:
        return 'unknown'


sample1 = 'House # C-38, Block 8, Gulshan-e-Iqbal, Karachi'
sample2 = 'House No. 123, Street 5, Phase 7, DHA, Karachi'
sample3 = "House No. 123, St. 5, Phase 7, DHA, Karachi"

abbreviations = load_json('abbreviations.json')

fname = "karachi_neighbourhoods.txt"

correct_words = ['gulshan e hadeed', 'gulshan e iqbal', 'defence', 'clifton', 'meher plaza', 'al murtaza heights', 'al murtaza height']

incorrect_words= ['gulshen iqbal', 'defnse', 'klifton', 'mehar plaza', 'al murteza heights']


# for word in incorrect_words:
#     print(word_correction_levenshtein(word, correct_words))


# khi_areas = load_corpus(fname)

# u1 = []

# for item in khi_areas:
#     t1 = lowercase_conversion(item)
#     t2 = remove_punctuation(t1)
#     t3 = remove_extra_spaces(t2)
#     u1.append(t3)

# create_corpus(fname, u1)