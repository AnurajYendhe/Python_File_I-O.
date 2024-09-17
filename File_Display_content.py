# Display data of the file on screen 

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
        fobj = open(file_Name,"r")
        if(fobj):
            print("File is succesfully opened ")
            data = fobj.read()
            fobj.close()
            print("content of that file : ")
            print(data)
        
        else:
            print("Error : Unable to open file")
    else:
        print("Error : There is no such file or directory")
if __name__ == "__main__":
    main()