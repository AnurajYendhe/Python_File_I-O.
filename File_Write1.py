import os

def checkExists(File_Name):
    if(os.path.exists(File_Name)):
        return True
    else:
        return False

def main():
    print("----Demonstration of File Write using Python -----")

    File_Name = None 
    bRet = False
    File_Name = input("Enter the name of file that we want to Write : ")
    bRet = checkExists(File_Name)
    
    if(bRet == True):
        fobj = open(File_Name,"a")
        if(fobj):
            print("File opened successfuly")
            data = input("Enter the data that we want to write into file : ")
            fobj.write(data)
            fobj.close()
            print("data is successfuly writen into the file")
        else:
            print("Error : Unable to open.")

    else:
        print("There is no such a file.")
if __name__ == "__main__":
    main()