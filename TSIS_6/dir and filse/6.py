def generate():
    try:
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(len(letters)):
            with open(letters[i] + ".txt" , 'w') as file:
                file.write(f'this is {letters[i]} file')
    except Exception as e:
        print("Error")
generate()