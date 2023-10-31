
with open("./Input/Letters/starting_letter.txt") as letter:
    example_letter = letter.read()
    with open("./Input/Names/invited_names.txt") as list_names:
        myLine = list_names.readline()
        while myLine:
            result_letter = example_letter.replace("[Name]", myLine.strip())
            with open(f"./Output/ReadyToSend/letter_to_{myLine}.txt", "w") as output_file:
                output_file.write(result_letter)
            print(myLine)
            myLine = list_names.readline()
