import os

def checkExists(File_Name):
    if(os.path.exists(File_Name)):
        return True
    else:
        return False

def main():
    print("----Demonstration of File creation using Python -----")

    File_Name = None 
    bRet = False
    File_Name = input("Enter the name of file that we want to created : ")
    bRet = checkExists(File_Name)
    
    if(bRet == False):
        fd = open(File_Name,"w")
        fd.close()
        print("file is created.")

    else:
        print("File is already exists in the current directory.")
if __name__ == "__main__":
    main()