import re # module for processing regular expressions https://docs.python.org/3/library/re.html

# Initial prompt to user
line = input("Enter a phone number to validate or 'exit' when done. ")

# TODO Define your regex
exp = r'^\D?(\d{3})\D?\D?(\d{3})\D?(\d{4})$'



while line != "exit":
    # TODO Find matches
    result = re.findall(exp, line)
    
    # TODO If no match found, print that no number was found
    if len(result) == 0:
        print('That is not a phone number')
   
    
    # TODO Else, break number up into area code, prefix, and suffic
    else:
        print(f"That is a valid phone number. Area code: {result[0][0]}, Prefix: {result[0][1]}, Suffix: {result[0][2]}")
    
    # As a stretch goal, you can modify your regex to search for country codes
    # too and print that out as well!
    
    
    # Done validating, read in a new line
    line = input("Enter a phone number to validate or 'exit' when done. ")