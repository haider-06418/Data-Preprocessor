import data_preprocessor

# abbreviations = data_preprocessor.load_json("abbreviations.json")

sample1 = 'House # C38, Block 8, Gulshan-e-Iqbal, Karachi'
sample2 = 'House No. 123, Street 5, Phase 7, DHA, Karachi'
sample3 = "House No. 123, St 5, Phase 7, DHA, Karachi"
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

sample5 = ' House # 82-B ,1st Floor, 21st Street, Khayaban e badar, Phase 6, Defence, Karachi '
sample6 = ' Apartment/Suite# 409 4th fl, Building All Blocks, Sahil Promenade, Khayaban e Sadi, Block 3, Clifton, Karachi '

# remaining_address = [' Building All Blocks', ' Sahil Promenade', ' Khayaban e Sadi', ' Block 3']
# remaining_address2 = [' Building All Blocks', ' Sahil Promenade', ' Khayaban e Sadi']
# remaining_address3 = [' Khayaban e Sadi', ' Block 3']
# remaining_address4 = [' Building All Blocks', ' Sahil Promenade']

# sample7 = 'Apartment/Suite# Flat 204, Building All Blocks, Pardesi Green Land Apartments, 8th Street, near baitul mukarrram majid, behind hakim saeed park, Bath Island, Clifton, Karachi'
# remaining_address = [' Building All Blocks', ' Pardesi Green Land Apartments', ' near baitul mukarrram majid', ' behind hakim saeed park', ' Bath Island']

# sample8 = ' House # 82-B ,1st Floor, near baitul mukarrram majid, behind hakim saeed park, 21st Street, Khayaban e badar, Phase 6, Defence, Karachi '
# remaining_address = [ ' near baitul mukarrram majid', ' behind hakim saeed park', ' Khayaban e badar', ' Phase 6']
# remaining_address = [ ' near baitul mukarrram majid', ' behind hakim saeed park', ' Khayaban e badar']

data = {'Ticket #': [], 'Type': [], 'House #': [], 'Apartment #': [], 'Building #': [], 'Building Name': [], 'Street Number/Name': [], 'Area & Sub Area': [], 'Neighbourhood': [], 'City': []}

