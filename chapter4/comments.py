# Single line, inline and multiline comments

#--------singleline Comments---------
#This is a comment.
print("Hello, World!")

#print("Hello, World!")
print("hiiiiiiiiiiiii!")

#--------Multiline Comments---------
#This is a comment
#written in
#more than just one line
print("Hello, World!")

#Write documentation using docstrings
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

#stored as an attribute of the function they document, meaning that you can access them programmatically.

def func():   
    """This is a function that does nothing at all"""  
    return
print(func.__doc__)
