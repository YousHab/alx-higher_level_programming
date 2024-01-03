#!/usr/bin/python3

def text_indentation(text):
    """ function that prints a text with 2 new lines after each
    of these characters: ., ? and :

    Args:
        text: the text to be splitted
    
    """
    new_text = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        for char in text:
            new_text += char
            if char in ":.?":
                new_text += '\n'
        print("{}".format(new_text))

input_text = "This is a sample text. It has some questions? How about formatting: nicely?"
text_indentation(input_text)