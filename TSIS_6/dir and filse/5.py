def write(filename, data_list):
    try:
        with open(filename, 'w') as file:
            for i in data_list:
                file.write(i)
        print(f"The list has been successfully written to the file '{filename}'.")
    except Exception as e:
        print(f"Error: {e}")


data_to_write = ["Apple", "Banana", "Orange", "Grapes"]

file_name = input("Enter the file name to write the list: ")

write(file_name, data_to_write)
