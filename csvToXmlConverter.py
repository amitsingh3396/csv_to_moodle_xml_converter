import shelve, csv
from lxml import etree

#set the xml filename here which will get generated
filename = "csvToXml.xml"

#Specify the encoding and root tag
with open(filename, "w") as f:
    f.write('''<?xml version="1.0" encoding="UTF-8"?>
<quiz>
</quiz>''')

tree = etree.parse(filename)
root = tree.getroot()

#Open and read the csv file of questions
with open('Test repository - Sheet13.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

# Loop over the rows of the CSV file and create XML elements for each question
for i, row in enumerate(rows):
    subTree = etree.parse("questionFormat.xml")
    subRoot = subTree.getroot()

    if i == 0:  #Skip header row
        continue

    #Comment tag containing the question number
    commentTag = subRoot[0]
    commentTag.text = f"question {i}"

    #Question tag
    questionTag = subRoot[1]

    #Add question name to the relevant tag
    question = row[1].split("\n")
    for j in range(len(question)):
        p_tag = etree.Element('p', {"dir": "ltr", "style": "text-align: left;"})
        p_tag.text = question[j]
        
        #Replace the question elements with html encoded elements
        question[j] = etree.tostring(p_tag).decode('ascii').replace('&lt;', '<').replace('&gt;', '>')

    questiontextTag = questionTag[1]
    questiontextTag[0].text = etree.CDATA("".join(question))

    #Add answers options to the relevant tags
    #First answer by default is the correct answer
    for j in range(15, 19):
        answerTag = questionTag[j]
        p_tag = etree.Element('p', {"dir":"ltr", "style":"text-align: left;"})
        p_tag.text = row[j - 13]
        option = etree.tostring(p_tag)
        answerTag[0].text = etree.CDATA(option)

    #Add questions tags to the relevant tags
    tagsTag = questionTag[19]
    for t in row[6:]:
        tag = etree.SubElement(tagsTag, 'tag')
        tagText = etree.SubElement(tag, 'text')
        tagText.text = t

    #Append the question to the main xml tree
    root.append(commentTag)
    root.append(questionTag)

#Write the xml tree to the xml file
tree.write(filename)





