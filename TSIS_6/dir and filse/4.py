def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"The number of lines in the file '{filename}' is: {line_count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")


file_name = input("Enter the path to the text file: ")
count_lines(file_name)
