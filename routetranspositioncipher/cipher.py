transposition_matrix = [
    ['16', '12', '8', '4', '0'],
    ['1', '5', '9', '13', '17'],
    ['18', '14', '10', '6', '2'],
    ['3', '7', '11', '15', '19']
]

# for i in range(len(transposition_matrix)):
#     print(transposition_matrix[i])

# Load the ciphertext string.
cipher_text = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"

# Convert ciphertext into a cipherlist to split out individual words.
cipher_text = list(cipher_text.split())
print(cipher_text)

# Get input for the number of columns and rows.
num_cols = 5
num_rows = 4

start = 0
stop = num_rows

# Get input for the key.
key ='-1 2 -3 4' # neg number means read UP column vs. DOWN

# Convert key into a list to split out individual numbers.
key =  [int(i) for i in key.split()]
print(key)

# Create a new list for the translation matrix.
translation_matrix = []

# For every number in the key: 
for i in key:
    print(i)
    if i < 0:
        col_items = cipher_text[start:stop]
        print(col_items)
    elif i > 0:
        col_items = list((reversed(cipher_text[start:stop])))
        print(col_items)
    translation_matrix[abs(i) - 1] = col_items
    start += num_rows
    stop += num_rows
print("\nciphertext = {}".format(cipher_text))
print("\ntranslation matrix =", *translation_matrix, sep="\n")
print("\nkey length= {}".format(len(key)))



# Create a new list and append every n items (n = # of rows) from the cipherlist.    

# Use the sign of key number to decide whether to read the row forward or backward.
#     
# Using the chosen direction, add the new list to the matrix. The index of each
#     
# new list is based on the column number used in the key.
# Create a new string to hold translation results.For range of rows:    
# For the nested list in translation matrix:          
# Remove the last word in nested list          
# Add the word to the translation string.Print the translation string.
