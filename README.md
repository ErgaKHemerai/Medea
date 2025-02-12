# Medea
Read XML file and compute statistics on it

To create an input file:
1. download the full text of a tragedy from Perseus
2. remove the TEI header
3. remove all <sp> and </sp> tags
4. remove suspension points (...) if any occur, because they would register a zero length sentences
