# File Rename

import os
import sys 
def checkFile(file_Name):
    if(os.path.exists(file_Name)):
        return True 
    else:
        return False
def main():
    file_Name1 = sys.argv[1]
    file_Name2 = sys.argv[2]
    bRet = checkFile(file_Name1)
    if(bRet == True):
        flag = checkFile(file_Name2)
        if(flag == False):
            fobj1 = open(file_Name1,"r")
            if(fobj1):
                print("File is succesfully opened ")
                data = fobj1.read()
                fobj1.close()
                fobj2 = open(file_Name2,"w")
                fobj2.write(data)
                fobj2.close()
                os.remove(file_Name1)
                print("succesfully Rename of file from",file_Name1,"into",file_Name2)
            
            else:
                print("Error : Unable to open file")
        else:
            print("Error :",sys.argv[2],"is already exists in directory.")
    else:
        print("Error : There is no such file or directory")

if __name__ == "__main__":
    main()