# import data_preprocessor

# abbreviations = data_preprocessor.load_json("abbreviations.json")

data = {'Ticket #': [], 'Type': [], 'House #': [], 'Apartment #': [], 'Building #': [], 'Building Name': [], 'Street Number/Name': [], 'Area & Sub Area': [], 'Neighbourhood': [], 'City': []}


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
