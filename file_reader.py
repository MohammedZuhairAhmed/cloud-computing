file_path = input("Enter the path of the file: ")

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file path.")
