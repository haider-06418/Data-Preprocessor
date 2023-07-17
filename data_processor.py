# Functions for Data Processing - Address Fields classification


# imports
import data_preprocessor
import random
abbreviations = data_preprocessor.load_json("abbreviations.json")


# performs pre processing functions on the address and returns information packed as a tuple
def pre_processing(address):
    standardized_address = data_preprocessor.lowercase_conversion(address)
    # standardized_address = data_preprocessor.remove_punctuation(standardized_address, True)
    standardized_address = data_preprocessor.standard_abbreviations_fix(standardized_address, abbreviations)
    # standardized_address = data_preprocessor.remove_extra_spaces(standardized_address, True)
    standardized_address = data_preprocessor.remove_extra_spaces(standardized_address, False)

    address_type = data_preprocessor.check_address_type(standardized_address)
    tokenized_address = data_preprocessor.standard_tokenization(standardized_address)

    # print(standardized_address)
    # print(address_type)
    # print(tokenized_address)

    return (standardized_address, address_type, tokenized_address)


# finds index of the desired field, returns none if field not found
def field_finder(field_name, tokenized_list):

    street_keywords = ['street', 'lane']
    road_keywords = ['road', 'highway', 'khayaban', 'avenue', 'boulevard', 'shahrah', 'alley', 'commercial']
    house_keywords = ['house', 'house no', 'house number', 'house #', 'plot']
    apartment_keywords = ['flat', 'flat no', 'flat number', 'flat #', 'apartment', 'suite']
    floor_keywords = ['floor', 'fl', 'level']
    area_keywords = ['phase', 'scheme', 'sector']
    keywords = []
    
    field_name = field_name.lower()

    if field_name == 'street':
        keywords = street_keywords
    elif field_name == 'road':
        keywords = road_keywords
    elif field_name == 'house':
        keywords = house_keywords
    elif field_name == 'apartment':
        keywords = apartment_keywords
    elif field_name == 'floor':
        keywords = floor_keywords
    elif field_name == 'area':
        keywords = area_keywords

    for index, token in enumerate(tokenized_list):
        if any(keyword in token for keyword in keywords):
            return index
    
    return None


# using a probability based algorithm to classify remaining fields
def probabilistic_identifiers(reference_tokenized_address, remaining_address):

    index_p_scores = []
    count = 0

    for item in remaining_address:
        true_index_in_original = reference_tokenized_address.index(item)+1
        index_percentage = (true_index_in_original/len(reference_tokenized_address))*100
        index_p_scores.append((count, index_percentage))
        count += 1

    potienal_area = [(index, score) for index, score in index_p_scores if score > 50]
    remaining_fields = [(index, score) for index, score in index_p_scores if score <= 50]

    if len(remaining_fields) >= 2:
        max_score_index = max(remaining_fields, key=lambda x: x[1])[0]
        potienal_building_name_tuple = remaining_fields.pop(max_score_index)
        potienal_building_name = list()
        potienal_building_name.append(potienal_building_name_tuple)

        potienal_building_number = list(remaining_fields)
    
    elif len(remaining_fields) == 1:
        potienal_building_name = list(remaining_fields)
        potienal_building_number = []

    else:
        potienal_building_name, potienal_building_number = [], []

    areas_indexes = [ip_tuple[0] for ip_tuple in potienal_area]
    building_name_indexes = [ip_tuple[0] for ip_tuple in potienal_building_name]
    building_number_indexes = [ip_tuple[0] for ip_tuple in potienal_building_number]

    return areas_indexes, building_name_indexes, building_number_indexes


# creates a random dataset of given size from the complete dataset
def create_random_sample(df, sample_size, selected_columns):
    random_indices = random.sample(range(len(df)), sample_size)
    random_sample = df.loc[random_indices, selected_columns]
    return random_sample