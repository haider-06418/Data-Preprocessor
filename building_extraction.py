# Functions for Building Name Extraction: Extracting Building Names using an automated learning corpus


# imports
import re
from fuzzywuzzy import process


# extracts addresses with unidentified building names and correctly identified building names for extraction 
def preparing_extraction(address_df, normalized_df):
    # appends address to respective normalized from ticket # as reference
    normalized_df = normalized_df.merge(address_df, left_on='Ticket #', right_on='Ticket#', how='left').drop('Ticket#', axis=1)
    
    # takes addresses to which Building Name is None
    # takes building names which is not None and type is apartment
    lst_addresses = normalized_df[normalized_df['Building Name'] == 'None']['Address'].tolist()
    lst_building_names = list(set(normalized_df[(normalized_df['Building Name'] != 'None') & (normalized_df['Type'] == 'apartment')]['Building Name']))

    # refinement in building names: remove building all blocks, building block, building a,b,c,d..., block 1,2,3, block a,b,c,..., 
    cleaned_building_names = refine_building_names(lst_building_names)
    
    return lst_addresses, cleaned_building_names


# refines building names by removing outliers
def refine_building_names(building_list):
    refined_list = [name for name in building_list if not re.match(r'^(building( all blocks| block)?|block)( [a-zA-Z0-9]+)?$', name, re.I)]
    refined_list.sort(key=lambda x: (len(x) <= 4, x))
    return refined_list 


# # Extract building names from addresses based on fuzzy matching with a default adjustable threshold
# def extract_building_names(addresses, building_names, threshold=75):
#     extracted_names = []

#     for address in addresses:
#         best_match, score = process.extractOne(address, building_names)

#         if score >= threshold:
#             extracted_names.append(best_match)
#         else:
#             extracted_names.append('None')

#     return extracted_names


# Extract building names from addresses based on fuzzy matching with a default adjustable threshold
def extract_building_names(addresses, building_names, threshold=75):
    # address_buildingname_tuple = []
    extracted_names = []

    for address in addresses:
        best_match, score = process.extractOne(address, building_names)

        if score >= threshold:
            # address_buildingname_tuple.append((address, best_match))
            extracted_names.append(best_match)
        else:
            # address_buildingname_tuple.append((address, 'None'))
            extracted_names.append('None')

    # return address_buildingname_tuple
    return extracted_names
