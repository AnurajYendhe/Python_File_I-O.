# to check file is exsits in current directory or not 

import os
def checkFile(file_Name):
    if(os.path.exists(file_Name)):
        return True 
    else:
        return False
def main():
    file_Name = input("Enter the Name of file : ")
    bRet = False
    bRet = checkFile(file_Name)
    if(bRet == True):
        print("File is present in the current directory")
    else:
        print("File is not present in the current directory")
if __name__ == "__main__":
    main()