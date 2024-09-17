# Copy all content from existing file into Demo.txt

import os
import sys 
def checkFile(file_Name):
    if(os.path.exists(file_Name)):
        return True 
    else:
        return False
def main():
    file_Name = sys.argv[1]
    bRet = False
    bRet = checkFile(file_Name)
    if(bRet == True):
        print("File is present in the current directory")
        fobj1 = open(file_Name,"r")
        if(fobj1):
            print("File is succesfully opened ")
            data = fobj1.read()
            fobj1.close()
            fobj2 = open("Demo.txt","w")
            fobj2.write(data)
            fobj2.close()
            print("succesfully copy all contents from",file_Name,"into Demo.txt")
        
        else:
            print("Error : Unable to open file")
    else:
        print("Error : There is no such file or directory")
if __name__ == "__main__":
    main()