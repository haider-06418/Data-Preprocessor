# Data Preprocessor
Converting raw unstructured string data into uniform & standartized data

## Address Parsing: 
To solve the problem of discrepancies in the address attribute of your dataset and achieve uniform addresses with consistent spelling.

1. **Data Preprocessing:**
   - Convert all addresses to lowercase for case insensitivity.
   - Remove leading and trailing whitespaces from addresses.

2. **Standardization of Abbreviations:**
   - Create a mapping or lookup table of commonly used abbreviations and their corresponding full forms. For example, "St." can be mapped to "Street," "Ave" to "Avenue," etc.
   - Use this mapping to replace the abbreviations in the addresses and standardize them. 

3. **Address Parsing and Normalization:**
   - Use an address parsing library or tool to split the addresses into individual components such as building number, street name, city, state, and postal code.
   - Normalize the parsed components to a standardized format using rules or lookup tables. For example, converting "Rd" to "Road" or "NY" to "New York."
   - Remove or correct any irregular address formats, ensuring all addresses follow a consistent structure.

4. **Address Validation and Correction:**
   - Utilize a geocoding service or tool (e.g., Google Maps Geocoding API, OpenStreetMap Nominatim) to validate and correct the addresses.
   - Submit each address for geocoding, and retrieve the standardized and corrected version provided by the service.
   - Update your dataset with the validated and corrected addresses.

5. **Address Matching and Deduplication:**
   - Perform address matching to identify similar or duplicate addresses within your dataset. This can be achieved using fuzzy matching algorithms (e.g., Levenshtein distance, Jaro-Winkler distance) to compare the addresses and identify close matches.
   - Once duplicates are identified, choose a canonical representation for each unique address and update all occurrences of the duplicates accordingly.

6. **Spelling Correction:**
   - Employ spelling correction algorithms (e.g., Levenshtein distance, Soundex, or more advanced models like BERT) to identify misspelled addresses and suggest corrections.
   - Compare the identified misspelled addresses against a dictionary or a large corpus of correctly spelled addresses to find the most probable correct spellings.
   - Replace the misspelled versions with the suggested correct spellings.

7. **Manual Review and Cleanup:**
   - Conduct a manual review of the addressed data to catch any remaining discrepancies or errors that automated techniques might have missed.
   - Make necessary corrections based on domain knowledge or further external validation.
