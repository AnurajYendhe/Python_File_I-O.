# compare content of two files

import os 
import sys

def CheckFile(File_Name1,File_Name2):
    if((os.path.exists(File_Name1)) and (os.path.exists(File_Name2))):
        return True
    else:
        return False

def main():
    File_Name1 = sys.argv[1]
    File_Name2 = sys.argv[2]

    bRet = False
    bRet = CheckFile(File_Name1,File_Name2)
    if(bRet == True):
        fobj1 = open(File_Name1,"r")
        fobj2 = open(File_Name2,"r")
        if(fobj1,fobj2):
            print("Both files are opened succesfully")
            data1 = fobj1.read()
            data2 = fobj2.read()
            if(data1 == data2):
                print("Success.")
            else:
                print("Failure.")
        else:
            print("Error : Unable to open files.")
    else:
        print("Error : there is no such files in the directory.")
if __name__ == "__main__":
    main()