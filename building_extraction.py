# Functions for Building Name Extraction: Extracting Building Names using an automated learning corpus


# imports
import re


# refines building names by removing outliers
def refine_building_names(building_list):
    refined_list = [name for name in building_list if not re.match(r'^(building( all blocks| block)?|block)( [a-zA-Z0-9]+)?$', name, re.I)]
    refined_list.sort(key=lambda x: (len(x) <= 4, x))
    return refined_list