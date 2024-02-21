# TODO, for Coaches; visit https://www.geeksforgeeks.org/how-to-open-a-file-using-the-with-statement/
# explain with, open, as keywords.

# This creates another python file where you can script python code into the console. 
with open("./FileManipulation/mySecondModule.py", "a+") as file: 
    while True: 
        line_count = len(file.readlines())
        user_input = input("> ")
        if user_input == "/exec": # type /exec to execute the newly scripted code.
            break
        if user_input.lower() == "q": # type q to quit.
            break
        file.write(user_input + "\n")        

# This allows Python to execute recently made module. 
with open("./FileManipulation/mySecondModule.py", "r") as file: 
    executable_string = ""
    for line in file.readlines(): # assembles the python script
        executable_string += line
    exec(executable_string) # tells python to execute the string as python code.


# Optional TODO for students: 
    """
        Create a simple app using python. 
            - Create a file or open if it exists, 
            - Ask users for input
            - Use that user input to write into the file. 
    """