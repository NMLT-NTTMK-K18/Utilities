import os


def fileNameCreate(File_Number):
    if File_Number < 10:
        File_Name = "00" + str(File_Number)+".cpp"
    elif File_Number < 100 and File_Number >= 10:
        File_Name = "0" + str(File_Number)+".cpp"
    else:
        File_Name = str(File_Number)+".cpp"
    return File_Name


def folderCreate(Folder_Number):
    if Folder_Number < 10:
        Folder_Name = "00" + str(Folder_Number)
    elif Folder_Number < 100 and Folder_Number >= 10:
        Folder_Name = "0" + str(Folder_Number)
    else:
        Folder_Name = str(Folder_Number)
    os.mkdir(Folder_Name)
    return Folder_Name


def fileCreate(File_Number):
    File_Name = fileNameCreate(File_Number)
    Folder_Name = folderCreate(File_Number)
    with open('cpp.txt', "r", encoding="utf-8") as f:
        content = f.readlines()
        Origin_path = os.getcwd()
        folder_path = os.getcwd() + f'\\{Folder_Name}'
        os.chdir(folder_path)
        with open(File_Name, "w", encoding="utf-8") as file:
            for line in content:
                file.write(line)
    os.chdir(Origin_path)


def fileSCreate():
    n = input()
    for i in range(1, int(n)+1):
        fileCreate(i)


def main():
    fileSCreate()


if __name__ == "__main__":
    main()
