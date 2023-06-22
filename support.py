# import pandas as pd
# import numpy as np
# from ez_address_parser import AddressParser
# import usaddress

abbreviations = {
    'Apt': 'Apartment',
    'Bldg.': 'Building',
    'Cantt.': 'Cantonment',
    'Col.': 'Colony',
    'Ext.': 'Extension',
    'Hno.': 'House Number',
    'Mkt.': 'Market',
    'Ngr.': 'Nagar',
    'P.O.': 'Post Office',
    'P.O.B': 'Post Office Box',
    'Pl.': 'Place',
    'Sec.': 'Sector',
    'Twn.': 'Town',
    'Vlg.': 'Village',
    'Dist.': 'District',
    'Rd.': 'Road',
    'Jct.': 'Junction',
    'Ln.': 'Lane',
    'Masjid': 'Mosque',
    'Fl.': 'Floor',
    'Blk.': 'Block',
    'Sch.': 'School',
    'Univ.': 'University',
    'Corp.': 'Corporation',
    'Ctr.': 'Center',
    'Plz.': 'Plaza',
    'Ph.': 'Phase',
    'G.P.O.': 'General Post Office',
    'Bzr.': 'Bazaar',
    'Est.': 'Estate',
    'St.': 'Street',
    'Ave': 'Avenue',
    'Blvd': 'Boulevard',
    'Pkwy': 'Parkway',
    'Hwy': 'Highway',
    'Res.': 'Residential',
    # Add more mappings as needed
    }

sample1 = 'House # C38, Block 8, Gulshan-e-Iqbal, Karachi'
sample2 = 'House No. 123, Street 5, Phase 7, DHA'
sample3 = "House No. 123, St. 5, Phase 7, DHA"

def standard_abbreviations_fix(address, abbreviation_mapping):
    words = address.split()
    standardized_words = [abbreviation_mapping.get(word, word) for word in words]
    standardized_address = ' '.join(standardized_words)
    return standardized_address


standardized_address = standard_abbreviations_fix(sample3, abbreviations)

print(standardized_address)
