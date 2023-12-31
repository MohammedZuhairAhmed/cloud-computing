file_name = input("Enter the name of the file: ")

# Prefix the file name with /home/ec2-user
file_path = "/home/ec2-user/" + file_name

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file name.")
