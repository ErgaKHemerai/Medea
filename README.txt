# Medea
The goal of this project is to produce a basic set of statistics about the texts of Greek tragedies: average words per sentence, average characters per word, number of lines spoken by each character.

The project relies on the texts published by the Perseus project, downloaded as XML files. A file containing a tragedy is first prepared by removing unused tags, stop words, etc. Next, a text file is created, with a line for each sentence in the text; the line is prefixed an indication of the section it comes from, and which character speaks it.
Finally, Microsoft Excel is used to average words per sentence and characters per word in each of the sections of the text.

In detail, the steps are:
1. download the full text of a tragedy from Perseus / Scaife Viewer
2. remove the TEI header; after this, I save the file as Simple_<title>.xml. These input files are included in this repository
3. run remove_tags.py on the file. This program removes some tags that are not relevant to the task of the project. I save the output as Simple_<title>_clean.xml
4. insert this tag immediately after the last line of verse: <speaker>dummy</speaker> . This is needed to ensure the last speaker's lines are processed correctly.
5. run readxml_nostops.py. This program removes punctuation and stop words from the text. It creates a txt file in which each line has this layout: <division of the play>,<character>,<one sentence from the play>.
6. Open the txt file with Microsoft Excel. Import it is a comma-delimited file. Add calculations for number of words and character per sentence (see sample: Simple_Electra.xls). Add a pivot table if you want to summarize by section of the play ("division", in Perseus XML parlance) or speaker.

There is also a program that counts the lines assigned to each character: line_count.py. It takes the output of step 3 and it produces a comma-delimited text file that can be processed in Microsoft Excel as described above.

Note: readxml.py does not remove stop words; otherwise, it is identical with readxml_nostops.py



