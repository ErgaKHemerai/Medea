# Medea Project. Alfredo Pizzirani, 2025
# read an xml file and convert it to a csv

import csv
# import xml.etree.ElementTree as ET 
from lxml import etree as ET
file_name = "Simple_Agamemnon"
xml_file = file_name+".xml"  # Replace with relevant file path

def find_leaf_elements(element, leaves):
    """Recursively find leaf elements with no child elements."""
    if len(element) == 0: # Check if element has no children
        leaves.append(element)
    else:
        for child in element:
            find_leaf_elements(child, leaves)
            
def find_parent(lelement):
    if lelement is not None:
        parent_element = lelement.getparent() #was: .text
        division = parent_element.get('subtype')
        return division # .rstrip()        
        
def remove_punctuation(row):    # remove punctuation marks (,:"-()?!), excluding:
                                # full stops, semicolons, high point (changed to full stops)
                                # apostrophes (replace apostrophes with spaces)
    row = row.lower()           # make all words all lowercase
    row = row.translate(row.maketrans('', '', ',')) #eliminate commas
    # row = row.translate(row.maketrans('', '', ';')) #eliminate semicolons
    row = row.translate(row.maketrans('', '', ':')) #eliminate colons
    row = row.translate(row.maketrans('', '', '"')) #eliminate double quotes
    row = row.translate(row.maketrans('', '', '-')) #eliminate dash 
    row = row.translate(row.maketrans('', '', '—')) #eliminate long dash
    row = row.translate(row.maketrans('', '', '?')) #eliminate question marks
    row = row.translate(row.maketrans('', '', "!")) #eliminate exclamation marks
    row = row.translate(row.maketrans('', '', '(')) #eliminate left parenthesis
    row = row.translate(row.maketrans('', '', ')')) #eliminate right parenthesis
    row = row.translate(row.maketrans("", '', "’")) #eliminate apostrophes
    row = row.replace(';','.')
    row = row.replace('·', '.')
    row = row.replace('.','.')
    return row
            

csv_row = [] # temporary holder for data to be written to CSV: division, speaker, letter count, word count
csv_data = [] # list of lists, containing one csv_row per dialog part
division = ""
speaker = ""
speech = ""
sentence = ""

# Parse XML file
tree = ET.parse(xml_file)
root = tree.getroot()

# Find leaf elements
leaf_elements = []
find_leaf_elements(root, leaf_elements) # not clear what this returns

for idx, leaf in enumerate(leaf_elements, 1):
    if leaf.tag == "speaker" :
        for letter in speech :
            if letter == "." :
                csv_row.append(division)
                csv_row.append(speaker)
                csv_row.append(sentence)
                csv_data.append(csv_row)
                sentence = ""
                csv_row = []
            else :
                sentence = sentence + letter
        speaker = leaf.text
        speech = ""
    if leaf.tag == "l" :
       line_text = leaf.text.strip() if leaf.text else "" # remove spaces before and after the line (spaces in the line are left, even if duplicate)
       line_text = leaf.text + " " 
       line_text = remove_punctuation(line_text)
       speech = speech + line_text
       division = find_parent(leaf)
       
     
for letter in speech :
    if letter == "." :
        csv_row.append(division)
        csv_row.append(speaker)
        text = leaf.text.strip() if leaf.text else "" # remove spaces before and after the line (spaces in the line are left, even if duplicate)
        csv_row.append(sentence)
        sentence = ""
    else :
        sentence = sentence + letter
csv_row.append(division)
csv_row.append(speaker)
text = leaf.text.strip() if leaf.text else "" # remove spaces before and after the line (spaces in the line are left, even if duplicate)
csv_row.append(sentence)
csv_data.append(csv_row)
csv_row = ""

target_file = file_name + ".txt"
with open(target_file, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
print("Output written to", target_file)
