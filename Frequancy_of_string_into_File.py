# count the frequancy of input string in the file
import os 
import sys

def CheckFile(File_Name):
    if(os.path.exists(File_Name)):
        return True
    else:
        return False

def main():
    File_Name = input("Enter the Name of file : ")
    string = input("Enter the string that we want to frequancy : ")

    bRet = False
    bRet = CheckFile(File_Name)
    if(bRet == True):
        fobj = open(File_Name,"r")
        if(fobj):
            print("file is opened succesfully")
            data = fobj.read()
            list1 = data.split(" ")
            counter = 0
            for i in list1:
                if(string == i):
                    counter = counter + 1
            print("Frequnacy of",string,"in",File_Name,"file is :",counter)
        else:
            print("Error : Unable to open files.")
    else:
        print("Error : there is no such files in the directory.")
if __name__ == "__main__":
    main()