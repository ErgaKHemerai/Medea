# Medea Project - Alfredo Pizzirani, 2025
# count the number of lines assigned to each speaker and write results to a comma-delimited file
# before running this program, add a dummy speaker part after the last line of verse in the input xml:
# <speaker>dummy</speaker> 

import csv
# import xml.etree.ElementTree as ET 
from lxml import etree as ET
file_name = "Simple_Electra_clean"
xml_file = file_name+".xml"  # Replace with relevant file path

def find_leaf_elements(element, leaves):
    """Recursively find leaf elements with no child elements."""
    if len(element) == 0: # Check if element has no children
        leaves.append(element)
    else:
        for child in element:
            find_leaf_elements(child, leaves)

tree = ET.parse(xml_file)
root = tree.getroot()

speaker = ""
line_count = 0
csv_row = []
csv_data = []

# Find leaf elements
leaf_elements = []
find_leaf_elements(root, leaf_elements) # not clear what this returns

for idx, leaf in enumerate(leaf_elements, 1):
    if leaf.tag == "speaker" :
        csv_row.append(speaker)
        csv_row.append(line_count)
        csv_data.append (csv_row)
        csv_row = []
        speaker = leaf.text
        line_count = 0
    if leaf.tag == "l" :
        line_count = line_count + 1


target_file = file_name + "_lines" + ".txt"
with open(target_file, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
print("Output written to", target_file)
