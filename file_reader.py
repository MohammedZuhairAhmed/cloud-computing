file_path = input("Enter the name of the file: ")

# Prefix the file path with /home/ec2-user
file_path = "/home/ec2-user" + file_path

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file path.")
