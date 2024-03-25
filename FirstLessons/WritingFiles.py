# A program that will write files

text = "\n \n This line of text was appended to the text above. \n"

with open('text.txt', 'a') as file:
    file.write(text)