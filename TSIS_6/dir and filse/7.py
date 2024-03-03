def copy_file(source_filename, destination_filename):
    try:
        with open(source_filename, 'r') as source_file:
            
            content = source_file.read()

            with open(destination_filename, 'w') as destination_file:
                
                destination_file.write(content)

        print(f"Contents of '{source_filename}' copied to '{destination_filename}' successfully.")
    except FileNotFoundError:
        print(f"Error: The specified file '{source_filename}' could not be found.")
    except Exception as e:
        print(f"Error: {e}")


first = input("Enter the source file name: ")
second = input("Enter the destination file name: ")

copy_file(first, second)
