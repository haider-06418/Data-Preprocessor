import data_preprocessor

sample1 = 'House # C38, Block 8, Gulshan-e-Iqbal, Karachi'
sample2 = 'House No. 123, Street 5, Phase 7, DHA, Karachi'
sample3 = "House No. 123, St 5, Phase 7, DHA, Karachi"

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

sample4 = 'Apartment/Suite# 404 4th Floor, Building All Blocks, Fatima Tower, Jamaludin Afghani Rd, Block 3, PECHS, Karachi'

samples = [' House # F-37 Off, Khayaban-e-Iqbal, Block 8, Clifton, Karachi ', 
           ' House # 82-B ,1st Floor, 21st Street, Khayaban e badar, Phase 6, Defence, Karachi ', 
           ' Apartment/Suite# 702 7th Floor, Building All Block, Jheel ParkView, Siraj Road, Block 2, PECHS, Karachi ', 
           ' House # R-18, Street No 37, Block-1, Gulistan-e-Johar, Karachi ', 
           ' Apartment/Suite# 409 4th fl, Building All Blocks, Sahil Promenade, Khayaban e Sadi, Block 3, Clifton, Karachi ', 
           ' House # 6C 1st Floor Ismail Center, Alamgir Road, Bahadurabad, PECHS, Karachi ', 
           ' Apartment/Suite# 204 2nd Floor, Building C, Farhan Classic, Pro Abdul Ghafoor Rd, Block 12, Gulistan-e-Johar, Karachi ', 
           ' House # 16B/1 Main, National Highway, Phase 2, Defence, Karachi ', 
           ' House # 187/2/B Off, Shahrah e Qaideen, Block 2, PECHS, Karachi ', 
           ' House # R-11/1, Khayaban e Sadi, Phase 7, Defence, Karachi ']


# tokenized_address = data_preprocessor.standard_tokenization(sample4) 
# remaining_address = [' Building All Blocks', ' Fatima Tower', ' Block 3']
# ['Apartment/Suite# 404 4th Floor', ' Building All Blocks', ' Fatima Tower', ' Jamaludin Afghani Rd', ' Block 3', ' PECHS', ' Karachi']
# word = ' Block 3'

# sample5 = ' House # 82-B ,1st Floor, 21st Street, Khayaban e badar, Phase 6, Defence, Karachi ',

sample6 = ' Apartment/Suite# 409 4th fl, Building All Blocks, Sahil Promenade, Khayaban e Sadi, Block 3, Clifton, Karachi '

remaining_address = [' Building All Blocks', ' Sahil Promenade', ' Khayaban e Sadi', ' Block 3']
# remaining_address = [' Building All Blocks', ' Sahil Promenade', ' Khayaban e Sadi']
# remaining_address = [' Khayaban e Sadi', ' Block 3']
# remaining_address = [' Building All Blocks', ' Sahil Promenade']

data = {'Ticket #': [], 'Type': [], 'House #': [], 'Apartment #': [], 'Building #': [], 'Building Name': [], 'Street Number/Name': [], 'Area & Sub Area': [], 'Neighbourhood': [], 'City': []}


def probabilistic_identifiers(sample_address):
    tokenized_address = data_preprocessor.standard_tokenization(sample_address) 
    reference_tokenized_address = list(tokenized_address)

    # to_place = len(remaining_address)

    index_p_scores = []
    count = 0

    for item in remaining_address:
        true_index_in_original = reference_tokenized_address.index(item)+1
        index_percentage = (true_index_in_original/len(reference_tokenized_address))*100
        index_p_scores.append((count, index_percentage))
        count += 1

    # for score in index_p_scores:
    #     if score < 50:
    #         if score == sorted(index_p_scores)[0]:
    #             return 1

    potienal_area = [(index, score) for index, score in index_p_scores if score > 50]

    remaining_fields = [(index, score) for index, score in index_p_scores if score <= 50]

    if len(remaining_fields) >= 2:

        max_score_index = max(remaining_fields, key=lambda x: x[1])[0]
        potienal_building_name_tuple = remaining_fields.pop(max_score_index)
        potienal_building_name = list()
        potienal_building_name.append(potienal_building_name_tuple)

        potienal_building_number = list(remaining_fields)

        # if len(remaining_fields) == 1:
        #     potienal_building_number = list(remaining_fields.pop())
        # else:
        #     potienal_building_number = list(remaining_fields)
    
    elif len(remaining_fields) == 1:
        potienal_building_name = list(remaining_fields)

    else:
        potienal_building_name, potienal_building_number = [], []


    # print(potienal_area)
    # print(potienal_building_name)
    # print(potienal_building_number)

    # if len(remaining_fields) < 2:

    # return index_p_scores

    areas_indexes = [ip_tuple[0] for ip_tuple in potienal_area]
    building_name_indexes = [ip_tuple[0] for ip_tuple in potienal_building_name]
    building_number_indexes = [ip_tuple[0] for ip_tuple in potienal_building_number]

    # return potienal_area, potienal_building_name, potienal_building_number
    return areas_indexes, building_name_indexes, building_number_indexes


# print(probabilistic_identifiers(sample6))

ai, bni, bnui = probabilistic_identifiers(sample6)

print('Area Index: ', ai)
print('Building Name Index:', bni)
print('Building Number Index: ', bnui)





# lst = [(0, 28.57142857142857), (1, 42.857142857142854), (2, 57.14285714285714)]

# lowest_score_index = min(lst, key=lambda x: x[1])[0]

# print(lowest_score_index) 

# max_score_index = max(lst, key=lambda x: x[1])[0]

# print(max_score_index) 
