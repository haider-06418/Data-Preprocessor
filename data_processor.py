import data_preprocessor

abbreviations = data_preprocessor.load_json("abbreviations.json")

def pre_processing(address):
    lowered_address = data_preprocessor.lowercase_conversion(address)
    standardized_address = data_preprocessor.remove_punctuation(lowered_address, True)
    standardized_address = data_preprocessor.standard_abbreviations_fix(standardized_address, abbreviations)
    standardized_address = data_preprocessor.remove_extra_spaces(standardized_address, True)

    address_type = data_preprocessor.check_address_type(standardized_address)
    tokenized_address = data_preprocessor.standard_tokenization(standardized_address)

    # print(standardized_address)
    # print(address_type)
    # print(tokenized_address)

    return (standardized_address, address_type, tokenized_address)


fname = 'data/khi_tickets_2022.csv'

df_complete = data_preprocessor.load_corpus(fname, pandas = True, header = True)

df = df_complete.drop(columns=['Title', 'Created', 'Close Time', 'Queue'], axis=1)



# print(df['Address'][0:5])

test = df['Address'][0:10]

# # for ady in test:
# #     print(ady)

# for i in range(len(test)):
#     info = pre_processing(test[i])
#     print(info[0])


