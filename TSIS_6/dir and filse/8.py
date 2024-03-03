import os

def delete_file(look):
    try:
        
        if os.path.exists(look):
            
            
            if os.access(look, os.W_OK):
                
                os.remove(look)
                print(f"File '{look}' has been successfully deleted.")
            else:
                print(f"Error: No write access to the file '{look}'. Cannot delete.")
        else:
            print(f"Error: The specified file '{look}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")


x = input("Enter the path of the file to delete: ")

delete_file(x)
