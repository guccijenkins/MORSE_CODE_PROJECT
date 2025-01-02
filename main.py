# MORSE CODE GENERATOR
# TO DOs:
# 1: Make list of letters /
# 2: Make an input for text to be modified with morse code /
# 3: Get index of letters based on their position in the alphabet /
# 4: Make an input for how morse code will operate (Ex: move the letters 4 spaces forward. (For example, 'a' will be 'e'.)/
# 5: Return the text in morse code/
# 6: Handle cases where the morse code adjustment can return text if out of range, or if there is a space in the text/
# 7: Make a input to decode morse code

# list of all letters in the english alphabet
lower_case_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                      'o','p','q','r','s','t','u','v','w','x','y','z']

# special_characters = [' ','!','@',"#",'$',"%","^","&","*","(",")","-","_","=","+","[",
#                       "{","]","}","|",";",":",",","<",".",">","/","?"]

# while loop verifies that the text input is only letters in the lower_case_letters list and is only spaces
while True:
    text_input = input(
        "Enter the text to be modified with Morse code. Please enter only letters and spaces: \n").lower()

    # Check if all characters are either letters or spaces
    if all(char in lower_case_letters or char == ' ' for char in text_input):
        break  # Valid input; exit loop
    else:
        print("Error: Please only enter letters and spaces.")

# while loop to verify if the morse code adjustment is a whole number and is between -25 and 25
while True:
    try:
        # Prompt for input
        morse_code_adjustment = int(input("Enter a whole positive or negative number between 1 and 25 for adjustment of text: \n"))
        # Validate range
        if -25 <= morse_code_adjustment <= 25:
            break  # Exit loop if input is valid
        else:
            print("Error: Please enter a number between -25 and 25.\n")
    except ValueError:
        # Handle non-integer input
        print("Error: Please enter a valid whole number.\n")

# list to capture the indices of the input text
morse_code_output_indices = []

# for loop that will convert the letters in the input to a number
for i in text_input:
    if i == " ":
        morse_code_output_indices.append(i)
    else:
        letter_index = lower_case_letters.index(i) + morse_code_adjustment
        morse_code_output_indices.append(letter_index)

# empty string to capture the new morse code text
morse_code_output_text = ''

# for loop to covert the indices into a letter
for m in morse_code_output_indices:
    if m == " ":
        space_text = " "
        morse_code_output_text += space_text
    elif m > 25:
        out_of_range = m - 26
        adjusted_indices = lower_case_letters[out_of_range]
        morse_code_output_text += adjusted_indices
    else:
        adusted_text = lower_case_letters[m]
        morse_code_output_text += adusted_text
print(morse_code_output_text)


