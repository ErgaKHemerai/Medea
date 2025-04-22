import xml.etree.ElementTree as ET
import sys

# input_file = "Simple_Electra.xml"
# output_file = ".csv"
tag_kill_list = ['q', 'del', 'sic', 'add', 'sp']

def strip_del_tags(xml_input_path, xml_output_path):
    tree = ET.parse(xml_input_path)
    root = tree.getroot()

    def remove_del_tags(elem, tag):
        for child in list(elem):
            if child.tag == tag:
                # Insert the contents of <del> before it
                index = list(elem).index(child)
                for subchild in list(child):    
                    elem.insert(index, subchild)
                    index += 1
                # Also include text inside <del> tag, if any
                if child.text:
                    if index > 0 and elem[index - 1].tail:
                        elem[index - 1].tail += child.text
                    else:
                        elem.text = (elem.text or '') + " " + child.text
                if child.tail:
                    elem.text = (elem.text or '') + " " + child.tail
                dirty_text = elem.text
                elem.text = dirty_text.replace ('\n', '')
                elem.remove(child)
            else:
                remove_del_tags(child, tag)
    for tag in tag_kill_list:
        remove_del_tags(root, tag)
    tree.write(xml_output_path, encoding='utf-8', xml_declaration=True)

# Example usage
strip_del_tags('Simple_Electra.xml', 'Simple_Electra_clean.xml')