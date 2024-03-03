import os

def check_path_access(path):
    try:
        
        if os.path.exists(path):
            print(f"Путь '{path}' существует.")

            
            if os.access(path, os.R_OK):
                print(f"Путь '{path}' доступен для чтения.")
            else:
                print(f"Путь '{path}' не доступен для чтения.")

            
            if os.access(path, os.W_OK):
                print(f"Путь '{path}' доступен для записи.")
            else:
                print(f"Путь '{path}' не доступен для записи.")

            
            if os.access(path, os.X_OK):
                print(f"Путь '{path}' доступен для выполнения.")
            else:
                print(f"Путь '{path}' не доступен для выполнения.")
        else:
            print(f"Путь '{path}' не существует.")
    except Exception as e:
        print(f"Ошибка: {e}")


path_input = input("Введите путь: ")
check_path_access(path_input)
