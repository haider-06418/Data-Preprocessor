# import data_preprocessor

# abbreviations = data_preprocessor.load_json("abbreviations.json")

data = {'Ticket #': [], 'Type': [], 'House #': [], 'Apartment #': [], 'Building #': [], 'Building Name': [], 'Street': [], 'Road': [], 'Area & Sub Area': [], 'Neighbourhood': [], 'City': []}


# incorrect tokenization: incorrect comma placement

sample_addresses = [' House # 75/1 5th lane, Khayaban e badar, Phase 6, Defence, Karachi ',
                    ' House # 64/2 23rd Street, Khayaban e Badban, Phase 5, Defence, Karachi ',
                    ' House # 6C 1st Floor Ismail Center, Alamgir Road, Bahadurabad, PECHS, Karachi ', 
                    ' House # 70/1 11th Street, Khayaban e badar, Phase 6, Defence, Karachi ',
                    ' House # 3/37 Molimabad, Khalid Bin Walid Rd, Block 3, PECHS, Karachi ',
                    ' House # 159 N  SWEET HOMES FLAT B 2, Kashmir Road, Block 3, PECHS, Karachi ',
                    ' House # Flat # 204 Al-Faisal Appartment, M Rafi Shamsi Road, Block 6, PECHS, Karachi ',
                    ' House # 1 C 1st Floor 29th Street, Tauheed Commercial, Phase 5, Defence, Karachi ',
                    ' Apartment/Suite# B-508, Building Block B, Billys Paradise Phase 2, Professor Abdul Ghafoor Road, Block 18, Gulistan-e-Johar, Karachi ',
                    ' House # D-3, Sawera Grand, Gulshan e Faisal, Bath Island, Clifton, Karachi ', # 102632106168
                    ' House # 1B 2nd South Street, South Circular Av, Phase 2, Defence, Karachi ',
                    ' House # B-330, near Taimuria Police, Allama Rasheed Turab, Block L, North Nazimabad, Karachi ',
                    ' House # 5 Flat 901 9th Floor Saima Burj Al Baraka, Khaliq-uz-Zaman Road, Block 8, Clifton, Karachi ',
                    ' House # Saima Burj Al Baraka Apartment Flat No 603 6th Flo, Khaliq-uz-Zaman Road, Block 8, Clifton, Karachi ',
                    ' House # 2-C APPT No 301 Floor 3rd 6th Lane, Nishat Commercial, Phase 6, Defence, Karachi ',
                    ' House # 4E/2/10 Flat 2 Islamia Center Main, Sir Shah Suleman RD, Nazimabad No 4, Nazimabad, Karachi',
                    ' House # Flat no. 5 2nd Floor Rabia Apartment Block 7/8, Ghazi Salahuddin Rd, CP Berar CHS, PECHS, Karachi ',
                    ' House # 165 Flat 203 Pardesi Heights Numaish, Britto Road, West - Catholic Colony, Garden, Karachi ',
                    ' House # WS-3 Flat no 401 4th Floor (Amafhha Arcade) Off, Burhani Avenue Road, KCHS, PECHS, Karachi', 
                    ' House # Safety Homes Flat No 510 5th Floor, Daud Pota Road, Civil Lines, Clifton, Karachi ']


'''We are doing address normalization, and an esssential part of it is tokenization. We are tokenizing with respect to the commas placed.
It is working fine for many but for a significant chunck of addresss it is not working as the commmas are in correctly placed in them, making 
the tokenization process incorrect, such that when it splits from an incorrectly placed comma 2 or more fields are placed in the same field. 
Below the list sample_addresses contains sample of such addresses in which the commas are incorrectly placed. Device and code in python the 
means by which we can correctly place commas so it can we tokenized appropriatly. 
The address fields which we are using are the keys of the data dictionary given below and the values will be the correct address field.
data = {'Ticket #': [], 'Type': [], 'House #': [], 'Apartment #': [], 'Building #': [], 'Building Name': [], 'Street Number/Name': [], 'Area & Sub Area': [], 'Neighbourhood': [], 'City': []}
Your task is to just place the commas right so we can tokenize it correctly. '''

data = {'Ticket #': [], 'Type': [], 'House #': [], 'Apartment #': [], 'Building #': [], 'Building Name': [], 'Street': [], 'Road': [], 'Area & Sub Area': [], 'Neighbourhood': [], 'City': []}


data = {'Ticket #': ['12334'], 'Type': ['house'], 'House #': ['House # 75/1 5th lane'], 'Apartment #': [], 'Building #': [], 'Building Name': [], 'Street': [], 'Road': ['Khayaban e badar'], 'Area & Sub Area': ['Phase 6'], 'Neighbourhood': ['Defence'], 'City': ['Karachi']}

data = {'Ticket #': ['12345678'], 'Type': ['appartment'], 'House #': [], 'Apartment #': [' House # Flat no. 5 2nd Floor Rabia Apartment Block 7/8'], 'Building #': [], 'Building Name': [], 'Street': [], 'Road': [], 'Area & Sub Area': ['CP Berar CHS'], 'Neighbourhood': ['PECHS'], 'City': ['Karachi']}


# Test Data for House / Street seperation using pattern recognition

# print(separate_house_street_defense(''))

# print(separate_house_street_defense("house # 71 13th street off"))
# print(separate_house_street_defense("house # 73 13th street"))
# print(separate_house_street_defense("house # 75 / 2 13th street"))
# print(separate_house_street_defense("house # 41 / 1 20 lane off"))
# print(separate_house_street_defense("house # 53 / 2 24th lane"))
# print(separate_house_street_defense("house # 55 / 1 17th lane"))
# print(separate_house_street_defense("house # 58 21st lane"))
# print(separate_house_street_defense("house # 61 / 2 24th lane"))
# print(separate_house_street_defense("house # 124 / 1 16th street"))
# print(separate_house_street_defense("house # 142 / 2 11th street"))
# print(separate_house_street_defense("house # 89 / 4 22nd street off"))
# print(separate_house_street_defense("house # 20 b2 street of"))
# print(separate_house_street_defense("house # s - 21 street 7th"))
# print(separate_house_street_defense("house # a - 129 3rd street"))
# print(separate_house_street_defense("House # 1234 Street 56"))
# print(separate_house_street_defense("house # 161 / 2 30th street main"))
# print(separate_house_street_defense("house # 40 b opposite 23rd street"))
# print(separate_house_street_defense("house # 11 - c lane # 11"))
# print(separate_house_street_defense('house # 26c 1st floor lane 3'))
# print(separate_house_street_defense('house # 43 c near mr bergur 2nd lane'))
# print(separate_house_street_defense('house # street - 15 aero club off'))
# print(separate_house_street_defense('house # 47f 48th street'))
# print(separate_house_street_defense('house # 18 - c / 2 1st floor 11th lane'))
# print(separate_house_street_defense('house # 11 - c lane # 11'))
# print(separate_house_street_defense("house # 11 - c lane # 11"))
# print(separate_house_street_defense('house # f - 64 5th street off'))
# print(separate_house_street_defense('house # 6 - c 10thstreet'))

# sample spelling correction using Levenshtein distance 

from nltk.metrics.distance import edit_distance

correct_words = ['gulshan e hadeed', 'gulshan e iqbal', 'defence', 'clifton', 'meher plaza', 'al murtaza heights', 'al murtaza height']

incorrect_words= ['gulshen iqbal', 'defnse', 'klifton', 'mehar plaza', 'al murteza heights']

for word in incorrect_words:
		temp = [(edit_distance(word, w),w) for w in correct_words]
		# print(sorted(temp, key = lambda val:val[0])[0][1])

		if len(temp) > 1: 
			temp = [min(temp, key=lambda t: t[0])]

		print(temp)
		# print(temp[0][1])

# print(edit_distance(incorrect_words[2], correct_words[3]), correct_words[3])


# Appartment and Lane pattern recognition:

'house # 16c flat no 401 3rd lane '

'house # 6 - c flat 1 14th lane '

'house # 40 - c flat no . 2 2nd floor lane 1 '

'house # 47c flat 3 floor 3rd street 21st '

'house # 14 - c flat 301 3rd floor 3rd street '

'house # 20 c flat 101 lane 7th '

'house # 24 - c flat no 3 lane no 3 '

'house # 34 - c flat 302 3rd floor 2nd lane '

'house # 19 - c flat 2 1st floor 27th street '

'house # 12 - c flat no 02 1st floor 32nd street '

'house # 12 - c flat no 301 12th street off '

'house # 55 - c flat 204 2nd floor 29th street off '

'house # 13 - c flat 6 3rd floor 8th lane '

'house # 10 - c flat no 3 2nd floor 4th lane '

'house # 32 - c flat no 3 3rd floor 2nd lane off '


# Apartments which do not have any building name as they are portions

' Apartment/Suite# House /Suite # 802, Building Block 8th floor, Badar Street, Block-16-A, Gulistan-e-Johar, Karachi '

' House # LS-9 App 2, Street 10, Block-2, Gulistan-e-Johar, Karachi '

' House # 14 C Flat 5 3rd Floor 8th, Ittehad Lane, Phase 6, Defence, Karachi '

'  House #  4C 4th Fl 10th Str, Jami Commercial, Phase 7, Defence, Karachi '

' House # 6-C/2 Flat 1 11th , Jami Commercial, Phase 7, Defence, Karachi '

' House # 94-C Flat No 5 3rd Floor  11th, Jami Commercial, Phase 7, Defence, Karachi '

' House # C 5 C Flat no.1 Main, Sehar Commercial, Phase 7, Defence, Karachi '

' House # 34-C Flat No 2 1st Floor 6th, Ittehad Lane, Phase 6, Defence, Karachi '

' House # 31/E Flat B2 2nd Floor 7A, Badar Commercial, Phase 5, Defence, Karachi '

' House # 41/Y-2, Flat# 04, 1st Floor, Dr Mahmud Hussain Rd, Block 6, PECHS, Karachi '

' House # 43/10 -L Building 3 2nd Floor, Shah Abdul Latif Rd, Block 6, PECHS, Karachi '

' House # 43-10-L/13 Flat 1, Dr Mahmud Hussain Rd, Block 6, PECHS, Karachi '

' House # 171-E  FLAT # 302, Sir Syed Road, Block 3, PECHS, Karachi '

' House # 32-C Flat No 3 3rd Floor 2nd Lane Off, Rahat Commercial, Phase 6, Defence, Karachi '

' House # 3-C 5th Floor 3rd , Rahat Lane, Phase 6, Defence, Karachi '
