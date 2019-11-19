# WhoSaidIt, part 1 & 2
# A program that will predict a piece of text's author, either Austen or Shakespeare.
# By Khanh Nguyen
# -----
# Dictionary: https://www.w3schools.com/python/python_dictionaries.asp
# Punctuation removal code: https://stackoverflow.com/questions/34293875/how-to-remove-punctuation-marks-from-a-string-in-python-3-x-using-translate/34294022
import string

translator=str.maketrans('','',string.punctuation)

# normalize
# -----
# This function takes a word and returns the same word
# with:
#   - All non-letters removed
#   - All letters converted to lowercase

def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()

# get_counts
# -----
# This function takes a filename and generates a dictionary
# whose keys are the unique words in the file and whose
# values are the counts for those words.

def get_counts(filename):
    words = []
    resultDict = {"_total":0}
    word = ''
    f = open(filename,"r")
    for x in f:
        x = x.translate(translator)
        words = x.split()
        for y in words:
            if y.isalpha():
                word = normalize(y)
                if word in resultDict:
                    resultDict[word] = resultDict[word] + 1
                else:
                    resultDict[word] = 1
                resultDict["_total"] = resultDict["_total"] + 1
    f.close()
    return resultDict

# Get the counts for the two shortened versions
# of the texts
shakespeare_counts = get_counts("hamlet.txt")
austen_counts = get_counts("pride_and_prejudice.txt")

# Check the contents of the dictionaries
for word,count in shakespeare_counts.items():
    print(word + ': ' + str(count))

print("-----")

for word,count in austen_counts.items():
    print(word + ': ' + str(count))
