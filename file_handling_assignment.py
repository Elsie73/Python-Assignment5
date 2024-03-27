# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("Line 1: Hello,world!I am Elsie.\n")
        file.write("Line 2: I am 22\n")
        file.write("Line 3: I love coding.\n")
except (FileNotFoundError, PermissionError) as e:
    print("Error:", e)
finally:
    print("File creation completed.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("File Content:")
        print(content)
except (FileNotFoundError, PermissionError) as e:
    print("Error:", e)

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Line 4: I live in Nairobi,Kenya.\n")
        file.write("Line 5: This is my number 0721951188\n")
        file.write("Line 6: Python is my favourite module.\n")
except (FileNotFoundError, PermissionError) as e:
    print("Error:", e)
finally:
    print("File appending completed.")
