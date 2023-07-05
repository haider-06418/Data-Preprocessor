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


