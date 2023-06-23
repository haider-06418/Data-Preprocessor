import data_preprocessor

sample1 = 'House # C38, Block 8, Gulshan-e-Iqbal, Karachi'
sample2 = 'House No. 123, Street 5, Phase 7, DHA'
sample3 = "House No. 123, St. 5, Phase 7, DHA"

abbreviations = data_preprocessor.load_json("abbreviations.json")


def check_address_type(address):
    house_keywords = ['house no', 'house number', 'house #', 'house']
    apartment_keywords = ['flat no', 'flat number', 'flat #', 'flat', 'apartment', 'building']

    house_found = any(keyword in address for keyword in house_keywords)
    apartment_found = any(keyword in address for keyword in apartment_keywords)

    if house_found and apartment_found:
        return 'Both House and Apartment'
    elif house_found:
        return 'House'
    elif apartment_found:
        return 'Apartment'
    else:
        return 'Unknown'



addy = data_preprocessor.lowercase_conversion(sample1)

standardized_address = data_preprocessor.standard_abbreviations_fix(addy, abbreviations)

addy_type = check_address_type(standardized_address)

print(addy_type)