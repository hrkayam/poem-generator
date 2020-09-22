# Mehrab Jamee
# Markov Chain Poetry
# Generated from Stray Birds by Rabindranath Tagore

import codecs
import random
import sys

# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    # sys.stderr = codecs.getwriter('utf8')(sys.stderr)

with codecs.open('satakam.txt', encoding='utf-8', newline="\n") as f:
    poems = f.readlines()

poems = ''.join([i for i in poems if not i.isdigit()]).replace("\n\n", " ").split(' ')

# poems = open("satakam.txt", "r").read()
# poems = ''.join([i for i in poems if not i.isdigit()]).replace("\n\n", " ").split(' ')
# # This process the list of poems. Double line breaks separate poems, so they are removed.
# # Splitting along spaces creates a list of all words.

index = 1
chain = {}
count = 100 # Desired word count of output

# This loop creates a dicitonary called "chain". Each key is a word, and the value of each key
# is an array of the words that immediately followed it.
for word in poems[index:]:
	key = poems[index - 1]
	if key in chain:
		chain[key].append(word)
	else:
		chain[key] = [word]
	index += 1

word1 = random.choice(list(chain.keys())) #random first word
message = word1

print(message)

# Picks the next word over and over until word count achieved
while len(message.split(' ')) < count:
	word2 = random.choice(chain[word1])
	word1 = word2
	message += ' ' + word2

print(message)

# creates new file with output and prints it to the terminal
with codecs.open("output.txt", "w") as file:
	file.write(message)
output = open("output.txt","r")
print(output.read())
