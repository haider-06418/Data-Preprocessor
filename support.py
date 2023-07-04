import data_preprocessor

sample1 = 'House # C38, Block 8, Gulshan-e-Iqbal, Karachi'
sample2 = 'House No. 123, Street 5, Phase 7, DHA, Karachi'
sample3 = "House No. 123, St. 5, Phase 7, DHA, Karachi"

abbreviations = data_preprocessor.load_json("abbreviations.json")

# def address_tokenize(address_str, address_type):
#     if address_type == 'both House and Apartment':
#         pass
#     elif address_type == 'house':
#         pass
#     elif address_type == 'apartment':
#         pass 
#     elif address_type == 'unknown':
#         pass

lowered_address = data_preprocessor.lowercase_conversion(sample3)
standardized_address = data_preprocessor.remove_punctuation(lowered_address, True)
standardized_address = data_preprocessor.standard_abbreviations_fix(standardized_address, abbreviations)
standardized_address = data_preprocessor.remove_extra_spaces(standardized_address, True)

address_type = data_preprocessor.check_address_type(standardized_address)
tokenized_address = data_preprocessor.standard_tokenization(standardized_address)

print(address_type)
print(tokenized_address)

print(standardized_address)

