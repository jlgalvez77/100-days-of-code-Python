from random import choice

# Step 1

word_list = ['ardvark', 'baboon', 'camel']

# Randomly choose a word from the word_list and assing it to a varible called chosen_word.

chosen_word = choice(word_list)

# Ask the user to guess a letter and assing their answer to a variable called guess. Make guess
# lowercase.
# Create an empty list called display. For each letter in the coosen_word, add a "_" to 'display'

display = []
for letter in chosen_word:
    display.append('_')

guess = input('Guess a letter: ').lower()

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# Loop through each position in the chosen_word; If the letter at that position matches 'guess'
# then reveal that letter in the display at that position.

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
    

# Print 'display' and you should see the guessed letter in the correct position and every other
# letter replace with "_"

print(display)