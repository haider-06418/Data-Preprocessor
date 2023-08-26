# Functions for Building Name Extraction: Extracting Building Names using an automated learning corpus


# imports
import re
from fuzzywuzzy import process
import data_preprocessor
import data_processor
import os


# returns None if building name is found to match with pattern
def refine_building_names(building_name):
    if not re.match(r'^(building( all blocks| block)?|block)( [a-zA-Z0-9]+)?$', building_name, re.I):
        return building_name
    return 'None'


# extracts addresses with unidentified building names and correctly identified building names for extraction 
def preparing_extraction(address_df, normalized_df):
    
    normalized_df = normalized_df.merge(address_df, left_on='Ticket #', right_on='Ticket#', how='left').drop('Ticket#', axis=1)
    
    lst_addresses = normalized_df[normalized_df['Building Name'] == 'None']['Address'].tolist()
    
    city_name = list(set(normalized_df['City']))[0]    
    file_name = f"data/buildings/directory/{city_name}_buildings.txt"

    if os.path.exists(file_name):
        buildings_corpus_lst = data_preprocessor.load_corpus(file_name)
    else:
        buildings_corpus_lst = []


    building_names_df = normalized_df[(normalized_df['Building Name'] != 'None') & (normalized_df['Type'] == 'apartment')]
    building_names_df.loc[:, 'Building Name'] = building_names_df['Building Name'].apply(refine_building_names)
    
    cleaned_building_names = list(set(building_names_df[(building_names_df['Building Name'] != 'None') & (building_names_df['Type'] == 'apartment')]['Building Name']))
    buildings_lst = [building_name.lower() for building_name in cleaned_building_names]


    # print("Commands: 'd' - delete, 'e' - edit, any other key - continue.")
    # for index, building in enumerate(buildings_lst):
    #     if building not in buildings_corpus_lst:
    #         print(f"Building Name: {building}")
    #         action = input("Enter Command: ").lower()
    #         if action == 'd':
    #             buildings_lst.pop(index)
    #         elif action == 'e':
    #             new_name = input("Enter new Building Name: ").lower()
    #             buildings_lst[index] = new_name

    # for building in buildings_lst:
    #     if building not in buildings_corpus_lst:
    #         buildings_corpus_lst.append(building)
            
    # data_preprocessor.create_corpus(file_name, buildings_corpus_lst)
 
 
    
    # lst_addresses = building_names_df[building_names_df['Building Name'] == 'None']['Address'].tolist()
    
    removed_building_addresses  = building_names_df[building_names_df['Building Name'] == 'None']['Address'].tolist()
    lst_addresses.extend(removed_building_addresses)
    
    updated_lst_addresses = data_processor.brew_address_list(lst_addresses)
    
    return updated_lst_addresses, buildings_corpus_lst


# Additional checking mechanism for building names
def layer2checks(address, buildingname, buildingnamecorpus):
    if buildingname not in address:
        for potiental_building_name in buildingnamecorpus:
            if potiental_building_name in address:
                buildingname = potiental_building_name 
                return buildingname
        return buildingname
    else:
        return True


# Extract building names from addresses based on fuzzy matching with a default adjustable threshold
def extract_building_names(addresses, building_names, threshold=75):
    extracted_names = []

    for address in addresses:
        best_match, score = process.extractOne(address, building_names)

        if score >= threshold:
            
            verify_building_name = layer2checks(address, best_match, building_names)
            if verify_building_name == True:
                extracted_names.append(best_match)
            else:
                extracted_names.append(verify_building_name)
        else:
            extracted_names.append('None')

    return extracted_names


# def extract_building_names(addresses, building_names, threshold=80):
#     extracted_names = []

#     for address in addresses:
#         best_match, score = process.extractOne(address, building_names)

#         if score >= threshold:
#             extracted_names.append(best_match)
#         else:
#             extracted_names.append('None')

#     return extracted_names


####
from config import *
import pandas as pd

df = data_preprocessor.load_corpus(fname, pandas = True, header = True) 
df = df.drop(columns=columns_to_drop, axis=1) 

df_normalized = data_preprocessor.load_corpus(fname_normalized, pandas = True, header = True)
df_normalized = df_normalized.fillna('None') # -> if from file

print('Dataframes Loaded')

def building_name_extraction_pipeline(df, df_normalized):
    lst_addresses, lst_building_names = preparing_extraction(df, df_normalized)
    extracted_building_names = extract_building_names(lst_addresses, lst_building_names)
    return lst_addresses, extracted_building_names

lst_addresses, ebnl = building_name_extraction_pipeline(df, df_normalized)

data = {
    'Addresses':lst_addresses,
    'Extracted Building Name':ebnl
}

df = pd.DataFrame(data)

df.to_excel('data/buildings/extraction_12.xlsx', sheet_name = 'Sheet1', index=False)

print('All Done')