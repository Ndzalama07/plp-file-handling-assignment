# File Creation:
# Create a Python script (file_handling_assignment.py) that does the following:
# Creates a new text file named "my_file.txt" in write mode ('w').
# Write at least three lines of text to the file, including a mix of strings and numbers.
with open("my_file.txt", 'a') as file:
    lines = ["file-handling\n", "TDD\n", "handling exceptions\n", "python\n"]
    file.writelines(lines)



# file Reading and Display:
# Enhance your script to read the contents of "my_file.txt" and display them on the console.
with open("my_file.txt", 'r') as data:
    try:
        contents = data.read()
        print(contents)
    except FileNotFoundError as e:
        print(e)
    finally:
        print(
            "This line runs regardless of whether an excption was raised in the try block")

# file Appending:
# Modify the script to open "my_file.txt" in append mode ('a').
# Append three additional lines of text to the existing content.
