import os

def checkExists(File_Name):
    if(os.path.exists(File_Name)):
        return True
    else:
        return False

def main():
    print("----Demonstration of File Open using Python -----")

    File_Name = None 
    bRet = False
    File_Name = input("Enter the name of file that we want to opened : ")
    bRet = checkExists(File_Name)
    
    if(bRet == True):
        fobj = open(File_Name,"r")
        if(fobj):
            print("File opened successfuly")
            fobj.close()
        else:
            print("Error : Unable to open.")

    else:
        print("There is no such a file.")
if __name__ == "__main__":
    main()