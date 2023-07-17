''' Address Normalizationn & Classification for Pakistani Based Addresses

The primary objective of this project is to develop a comprehensive address normalization system tailored specifically for 
Pakistani addresses. The system will transform addresses from diverse formats into a standardized structure that adheres to 
predefined guidelines and rules. By achieving consistency and uniformity in address data, the project aims to enhance data quality,
facilitate efficient address matching, enable precise geocoding, and simplify address-based searches and analysis. 

Process Overview:

Stage 1: Uniformaty - converting to lowercase and eradicating whitespaces
Stage 2: Standardization of Abbreviations
Stage 3: Address Parsing and Normalization
Stage 4: Spelling Correction - using Levenshtein distance
Stage 5: Manual Review & percentage accuracy

For more information please refer to README.md or the project report file. '''


# imports 
import data_preprocessor
import data_processor
import pandas as pd
abbreviations = data_preprocessor.load_json("abbreviations.json")


# USER DEFINED 
fname = 'data/khi_tickets_2022.csv' 
columns = ['Ticket #', 'Type', 'House #', 'Apartment #', 'Building #', 'Building Name', 'Street', 'Road', 'Area & Sub Area', 'Neighbourhood', 'City'] 
df_complete = data_preprocessor.load_corpus(fname, pandas = True, header = True)
df = df_complete.drop(columns=['Title', 'Created', 'Close Time', 'Queue'], axis=1) 


# data to normalize
test2 = df[['Ticket#', 'Address']][0:20] 
test3 = data_processor.create_random_sample(df, 50, ['Ticket#', 'Address'])


# dataframe for storing normalized addresses 
address_df = data_preprocessor.create_dataframe(columns)


print('****** PREREQUISITIES COMPLETE ******\n')


# parsing and normalization

def parse(dataframe):

    global address_df

    list_of_addresses = dataframe['Address'].tolist()
    tickets = dataframe['Ticket#'].tolist()
    
    for index in range(len(dataframe)):
        ticketno = tickets[index]
        address = list_of_addresses[index]

        data = {'Ticket #': [], 'Type': [], 'House #': [], 'Apartment #': [], 'Building #': [], 'Building Name': [], 'Street': [], 'Road': [], 'Area & Sub Area': [], 'Neighbourhood': [], 'City': []}
        
        address_info = data_processor.pre_processing(address)
        address_type = address_info[1]
        tokenized_address = address_info[2]
        reference_tokenized_address = list(tokenized_address)

        ''' Ticket # '''
        data['Ticket #'].append(ticketno)

        ''' Type '''
        data['Type'].append(address_type)

        ''' City '''
        data['City'].append(tokenized_address.pop(-1).strip())

        ''' Neighbourhood '''
        data['Neighbourhood'].append(tokenized_address.pop(-1).strip())


        ''' Road '''
        road_index = data_processor.field_finder('road', tokenized_address)
        if road_index is not None:
            data['Road'].append(tokenized_address.pop(road_index).strip())
        else:
            data['Road'].append('None')


        ''' Street '''
        street_index = data_processor.field_finder('street', tokenized_address)
        if street_index is not None:
            data['Street'].append(tokenized_address.pop(street_index).strip())
        else:
            data['Street'].append('None')

        
        '''Appartment # '''
        appartment_index = data_processor.field_finder('apartment', tokenized_address)
        if appartment_index is not None:
            data['Apartment #'].append(tokenized_address.pop(appartment_index).strip())
        else:
             data['Apartment #'].append('None')

        floor_index = data_processor.field_finder('floor', tokenized_address)
        if floor_index is not None:
            if data['Apartment #'] == ['None']:
                data['Apartment #'] = [tokenized_address.pop(floor_index).strip()]
            else:
                data['Apartment #'].append(tokenized_address.pop(floor_index))
                value_lst = data['Apartment #']
                joined_string = ' '.join(value_lst)
                data['Apartment #'] = [joined_string.strip()]


        ''' House # '''
        house_index = data_processor.field_finder('house', tokenized_address)
        if house_index is not None:
            data['House #'].append(tokenized_address.pop(house_index).strip())
        else:
            data['House #'].append('None')

        
        ''' Area/Sub Area '''
        area_index = data_processor.field_finder('area', tokenized_address)
        if area_index is not None:
            data['Area & Sub Area'].append(tokenized_address.pop(area_index).strip())
        else:
            data['Area & Sub Area'].append('None')

        p_area_index, p_buildingname_index, p_buildingnumber_index = data_processor.probabilistic_identifiers(reference_tokenized_address, tokenized_address)
            
        if len(p_area_index) > 0:
                if data['Area & Sub Area'] != ['None']:
                    for index in p_area_index:
                        data['Area & Sub Area'].append(tokenized_address[index].strip())
                    value_lst = data['Area & Sub Area']
                    joined_string = ', '.join(value_lst)
                    data['Area & Sub Area'] = [joined_string.strip()]
                else:
                    data['Area & Sub Area'] = []
                    for index in p_area_index:
                        data['Area & Sub Area'].append(tokenized_address[index].strip())
                    value_lst = data['Area & Sub Area']
                    joined_string = ', '.join(value_lst)
                    data['Area & Sub Area'] = [joined_string.strip()]

        for index in sorted(p_area_index, reverse=True):
            tokenized_address.pop(index)

        
        if address_type == 'house':
            if len(p_buildingname_index) + len(p_buildingnumber_index) > 0:
                area_indexes_more = p_buildingnumber_index + p_buildingname_index 

                if data['Area & Sub Area'] != ['None']:
                        temp = data['Area & Sub Area']
                        data['Area & Sub Area'] = []
                        for index in area_indexes_more:
                            data['Area & Sub Area'].append(tokenized_address[index].strip())
                        value_lst = list(data['Area & Sub Area'])
                        for x in temp:
                            value_lst.append(x)
                        joined_string = ', '.join(value_lst)
                        data['Area & Sub Area'] = [joined_string.strip()]
                else:
                    data['Area & Sub Area'] = []
                    for index in area_indexes_more:
                        data['Area & Sub Area'].append(tokenized_address[index].strip())
                    value_lst = data['Area & Sub Area']
                    joined_string = ', '.join(value_lst)
                    data['Area & Sub Area'] = [joined_string.strip()]

                for index in sorted(area_indexes_more, reverse=True):
                    tokenized_address.pop(index)    
        else:
            ''' Building Name '''
            if len(p_buildingname_index)>0:
                for index in p_buildingname_index:
                    data['Building Name'].append(tokenized_address[index].strip())
                value_lst = data['Building Name']
                joined_string = ', '.join(value_lst)
                data['Building Name'] = [joined_string.strip()]

            ''' Building Number '''
            if len(p_buildingnumber_index)>0:
                for index in p_buildingnumber_index:
                    data['Building #'].append(tokenized_address[index].strip())
                value_lst = data['Building #']
                joined_string = ', '.join(value_lst)
                data['Building #'] = [joined_string.strip()]


            for index in sorted(p_buildingname_index, reverse=True):
                        tokenized_address.pop(index) 

            for index in sorted(p_buildingnumber_index, reverse=True):
                        tokenized_address.pop(index)


        ''' Shifting Entries '''
        if address_type == 'house' and data['House #'] == ['None'] and data['Apartment #'] != ['None']:
            data['House #'] = data['Apartment #']
            data['Apartment #'] = []


        ''' Null Entires'''
        for field in data:
            if len(data[field]) == 0:
                data[field].append('None')
      

        df_temp = data_preprocessor.create_dataframe(columns, data, datacheck=True)
        address_df = pd.concat([address_df, df_temp], axis=0)

    return address_df


# parse(test2)
parse(test3)


print('****** DATA PREPROCESSING DONE ******\n')
print('****** DATA NORMALIZATION DONE ******\n')


# storing processed data

# fname_processed = 'data/data_a3.csv'
# address_df.to_csv(fname_processed, index=False)

fname_processed = 'data/datarand_a4.csv'
address_df.to_csv(fname_processed, index=False)

print('********* DATA STORAGE DONE *********\n')
print(f'Processed Data Stored successfully in {fname_processed}.')