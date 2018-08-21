# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 18:59:51 2018

@author: Delol
"""
def translate(text):
    # Defination used to translate the user input text
    newtext=""
      # A variable called that is initailly empty
    for letter in text:
        # For loop to traverse each element
        if letter not in 'aeiou ':
            # If loop used to neglect vovels
            newtext=newtext+letter+'o'+letter
              # Robbers Method to duplicate the consonant and place 'o' in-between them
        else:
            # Case when a vovel is entered
            newtext=newtext+letter
              # The string is left undisturbed
    return newtext
        # return statement to return the values of updated string
        
        
# calling finction
text=raw_input("Enter the text:>")
    # To take user inputs for translation
print(translate(text))
    # Calls the defination defined above and accepts updated value
print "Done"
    # Marks the end of code
            

print "".join(i+"o"+i if i not in 'aeiou ' else i for i in text)