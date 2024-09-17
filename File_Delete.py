import os

def checkExists(File_Name):
    if(os.path.exists(File_Name)):
        return True
    else:
        return False

def main():
    print("----Demonstration of File Delete using Python -----")

    File_Name = None 
    bRet = False
    File_Name = input("Enter the name of file that we want to Deleted : ")
    bRet = checkExists(File_Name)
    
    if(bRet == True):
        os.remove(File_Name)
        print("file was deleted.")

    else:
        print("There is no such a file.")
if __name__ == "__main__":
    main()