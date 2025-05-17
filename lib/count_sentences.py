#!/usr/bin/env python3
# Define a class named MyString
class MyString:
    # Constructor method initializing a MyString instance with a value attribute
    def __init__(self, value = ""):
        self.value = value        # Set the value attribute

    # Define property getter for value
    @property
    def value(self):
        """The value property"""
        return self._value
    # Define setter for value property
    @value.setter
    def value(self, input_value):
        """The value must be a string"""
        # Check is value is a string
        if isinstance(input_value, str):
            self._value = input_value # Set the _value attribute
        # If value is not a string, print error message
        else:
            print("The value must be a string.")   

    # Method to return true if value is a sentence ending in "." 
    def is_sentence(self):
        if self.value.endswith("."): # Checks if value ends with "."
            return True
        else:
            return False
        
    # Method to return true if value is a sentence ending in "?"    
    def is_question(self):
        if self.value.endswith("?"): # Checks if value ends with "?"
            return True
        else:
            return False
        
    # Method to return true if value is a sentence ending in "!" 
    def is_exclamation(self):
        if self.value.endswith("!"): # Checks if value ends with "!"
            return True
        else:
            return False
        
    # Method to count the number of sentences in value   
    def count_sentences(self):
        text = self.value.replace("!", ".").replace("?", ".")  # Replace all "!" and "?" with "." to standardize sentence endings
        # Splits the sentences in the value after the "."
        sentences = text.split(".")
        # Filter out empty strings and strings with only whitespace 
        filtered = [s for s in sentences if s.strip()]
        # returns the number of sentences 
        return len(filtered)
        
    pass
