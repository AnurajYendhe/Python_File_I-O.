
def main():
    print("----Demonstration of File creation using Python -----")
    File_Name = None
    File_Name = input("Enter the name of file that we want to created : ")
    fd = open(File_Name,"w")
    fd.close()
    print("file is created.")
if __name__ == "__main__":
    main()