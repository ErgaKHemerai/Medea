# Medea
Read XML file and prepare it to compute stats

Two versions of the program: 
readxml.py - includes stop words in the output
readxml_nostops.py - excludes stop words


To create an input file:
1. download the full text of a tragedy from Perseus / Scaife Viewer
2. remove the TEI header
3. remove all <sp> and </sp> tags
4. remove suspension points (...) if any occur, because they would register a zero length sentences
5. remove <add>, <del>, <sic> tags
