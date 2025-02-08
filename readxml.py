# Edit file path in if section
# xml file: remove TEI header; add a dummy (empty) <speaker></speaker> after the last line

import csv
import xml.etree.ElementTree as ET 
xml_file = "example.xml"  # Replace with relevant file path
# tree = ET.parse(xml_file)
# root = tree.getroot() # this returns a root in the form <Element 'body' at 0x0000022645C95030>

def remove_punctuation(row):    # remove punctuation marks (,:"-()?!), excluding:
                                # full stops, semicolons, high point (changed to full stops)
                                # apostrophes (replace apostrophes with spaces)
    row = row.lower()           # make all words all lowercase
    row = row.translate(row.maketrans('', '', ',')) #eliminate commas
    # row = row.translate(row.maketrans('', '', ';')) #eliminate semicolons
    row = row.translate(row.maketrans('', '', ':')) #eliminate colons
    row = row.translate(row.maketrans('', '', '"')) #eliminate double quotes
    row = row.translate(row.maketrans('', '', '-')) #eliminate dash
    row = row.translate(row.maketrans('', '', '?')) #eliminate question marks
    row = row.translate(row.maketrans('', '', "!")) #eliminate exclamation marks
    row = row.translate(row.maketrans('', '', '(')) #eliminate left parenthesis
    row = row.translate(row.maketrans('', '', ')')) #eliminate right parenthesis
    row = row.translate(row.maketrans("", '', "’")) #eliminate apostrophes
    row = row.replace(';',' . ')
    row = row.replace('·', ' .')
    row = row.replace('.',' . ')
    return row

def find_leaf_elements(element, leaves):
    """Recursively find leaf elements with no child elements."""
    if len(element) == 0: # Check if element has no children
        leaves.append(element)
    else:
        for child in element:
            find_leaf_elements(child, leaves)

def count_letters(speech) : # count LETTERS per sentence in a string with multiple sentences. Sentences are separated by "."
    # count letters
    letter_counts = []
    stop = 0

    for idx, letter in enumerate(speech):
        if letter == "." :
            letter_counts.append(idx-stop)
            stop = (idx+2)
    
    return(letter_counts)
   
def count_words(speech) : # count WORDS per sentence in a string with multiple sentences. Sentences are separated by "."
 
    # count words
    words = ""
    word_counts = []

    for letter in speech:
        words = words + letter
        if letter == "." :
            word_count = len(words.split())
            word_counts.append (word_count)
            words = ""
            
    return(word_counts)

csv_row = ["","","",""] # temporary holder for data to be written to CSV: division, speaker, letter count, word count
csv_data = [] # list of lists, containing one csv_row per dialog part
division = "episode"
speech = "null"
speaker = "null"

# Parse XML file
tree = ET.parse(xml_file)
root = tree.getroot()

# Find leaf elements
leaf_elements = []
find_leaf_elements(root, leaf_elements) # not clear what this returns

# iterate, collecting each speaker's speech into a single list item. Store all speeches in csv_data, which later will be written to file
print("\nLeaf elements found:")
for idx, leaf in enumerate(leaf_elements, 1):
    
    
    if leaf.tag == "div":
        division = leaf.attrib
        #print("division",division)
    if leaf.tag == "speaker" :
        # first, write out information about the previous speech and reset the variables
        csv_row.append (speaker)
        print ("line91",type(csv_row))
        csv_row.append = speaker
        csv_row.append = speech
        csv_data.append (csv_row)
        csv_row =""
        speech = ""
        # then get the new speaker's name
        speaker = leaf.text #
    if leaf.tag == "l" :
        text = leaf.text.strip() if leaf.text else "" # remove spaces before and after the line (spaces in the line are left, even if duplicate)
        text = remove_punctuation(text)
        speech = speech + text

print(csv_data)
        
        
    #print ("csv_row", csv_row)
    #print(f"{idx}. Tag: {leaf.tag}")
    #print(f" Text: {text}")
    #if leaf.attrib:
    #    print(f" Attributes: {leaf.attrib}")
csv_data.append (csv_row)
csv_row = []
      
            


print("csv_data", csv_data)

