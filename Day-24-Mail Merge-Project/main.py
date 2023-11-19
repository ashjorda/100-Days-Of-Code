#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt", mode="r") as letter_template:
    transpose_letter = letter_template.read()

with open("Input/Names/invited_names.txt", mode="r") as guest_list:
    name_list = guest_list.readlines()
    for names in name_list:
        guest = names.strip()
        transposed_letter = transpose_letter.replace("[name]", f"{guest}")
        with open(f"Output/ReadyToSend/letter_for_{guest}.txt", mode="w") as send_letter:
            send_letter.write(f"{transposed_letter}")
