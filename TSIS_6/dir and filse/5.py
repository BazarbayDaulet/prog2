def write(filename, data_list):
    try:
        with open(filename, 'w') as file:
            for i in data_list:
                file.write(i, " ")
        print(f"The list has been  written to the file '{filename}'.")
    except Exception as e:
        print(f"Error: {e}")

inp = input("print a list")
listt = inp.split()
data_to_write = []
for i in range(len(listt)):
    data_to_write.append(listt[i])


file_name = input("Enter the file name to write the list: ")

write(file_name, data_to_write)
