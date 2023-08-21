# csv_to_moodle_xml_converter
This file converts a CSV file containing questions to an MCQ XML Moodle question format

The repo consists of 2 files: QuestionFormat.xml and xmlToCsvConverter.py

Download both files in the same directory and ensure the CSV file is in the same directory. Run the .py file, and the program will generate the XML file which can be uploaded to moodle.

The CSV file is assumed to be of the following format:
questionname, questiontext, answer1, answer2,	answer3, answer4,	tag1, tag2,	tag3, tag4, .....

Answer is by default stored in answer1 field.
The marking scheme of the questions generated will be +1 for correct answer and -0.33 for negative answer.
The negative marks penalty can be removed by changing <penalty> tag value in line 14 of QuestionFormat.xml to 0 and change the fraction attribute value of answer tag in lines 37, 43, and 49 to a value 0.

Number of question tags can be variable with subsequent question tags added with headers tag5, tag6, and so on.
