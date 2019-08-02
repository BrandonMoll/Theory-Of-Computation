import re # module for processing regular expressions https://docs.python.org/3/library/re.html
import sys
import csv
import codecs
if __name__ == '__main__':
  # Exit if command line args entered incorrectly
  if len(sys.argv) != 2:
    print("usage: extract_links.py [input_file]")
    sys.exit(0)

# Filename is 2nd command line arg
filename = sys.argv[1]

# TODO Read HTML file
html_file = open(filename, 'r', encoding='utf-8')
source_code = html_file.read()

# TODO Set up regex
exp = r'[h]{1}[t]{2}[p]{1}[s]?[:]{1}[\/]{2}[^"|\']+[.]{1}[^"|\']+'

# TODO Find links using regex, save in list called 'matches'
matches = re.findall(exp, source_code)

# Check matches, print results
# TODO Read in links from answers.txt (hint...this is a CSV file), 
# save in list called 'answer_data'
csv_file = open('answers.txt')
data = csv.reader(csv_file, delimiter=',')
badarray_data = []
answer_data = []
for row in data:
  badarray_data.append(row)
for i in badarray_data[0]:
  answer_data.append(i)
# Compare answers with matches found using regex, print out any mismatches
# UNCOMMENT BELOW WHEN READY TO CHECK IF YOUR REGEX IS FINDING ALL THE LINKS
result = "All links matched!"
if len( matches ) != len( answer_data ):
  result = "Your regex found %i matches. There should be %i matches" %(len( matches ), len( answer_data ) )
else:
  for i in range( len(answer_data) ):
    if( matches[i] != answer_data[i] ):
      result = "Mismatched link. Got %s but expected %s" % ( matches[i], answer_data[i] )
      break
print( result )