PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("../Mail Merge Project/Input/Letters/starting_letter.txt") as letter:
    drafted_letter = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = drafted_letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

'''        
letter = open("F:/Mail Merge Project Python/Mail Merge Project/Input/Letters/starting_letter.txt","r")
#TODO: Create a letter using starting_letter.txt
letter = open("./Input/Letters/starting_letter.txt","r")
print(letter.readlines())
#for each name in invited_names.txt
for invitee in invited_names:
    print(invitee)
    #Replace the [name] placeholder with the actual name.
    replaced_name = placeholder_text.replace(placeholder_text, invitee)
    trimmed_name = replaced_name.strip()
    #Save the letters in the folder "ReadyToSend".
    with open(f"../Mail Merge Project/Output/ReadyToSend/letter_for_{trimmed_name}.txt",mode="w") as data:
        data.write(f'{trimmed_name}.txt')

'''
