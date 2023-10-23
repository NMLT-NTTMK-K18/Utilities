import os


def cppNameCreate(CPP_Number):
    if CPP_Number < 10:
        CPP_Name = "00" + str(CPP_Number)+".cpp"
    elif CPP_Number < 100 and CPP_Number >= 10:
        CPP_Name = "0" + str(CPP_Number)+".cpp"
    else:
        CPP_Name = str(CPP_Number)+".cpp"
    return CPP_Name


def folderCreate(Folder_Number):
    if Folder_Number < 10:
        Folder_Name = "00" + str(Folder_Number)
    elif Folder_Number < 100 and Folder_Number >= 10:
        Folder_Name = "0" + str(Folder_Number)
    else:
        Folder_Name = str(Folder_Number)
    os.mkdir(Folder_Name)
    return Folder_Name


def partCreate(Part_Number):
    if Part_Number < 10:
        Part_Name = "Part"+"00" + str(Part_Number)
    elif Part_Number < 100 and Part_Number >= 10:
        Part_Name = "Part"+"0" + str(Part_Number)
    else:
        Part_Name = "Part"+str(Part_Number)
    return Part_Name


def cppCreate(Part_Number, Part_Name, CPP_Number):
    CPP_Name = cppNameCreate(CPP_Number)
    Origin_path_folder = os.getcwd()
    folder_path = os.getcwd() + f'\\{Part_Name}'
    os.chdir(folder_path)
    os.chdir(Origin_path_folder)
    Folder_Name = folderCreate(CPP_Number)
    os.mkdir(Folder_Name)
    with open('cpp.txt', "r", encoding="utf-8") as f:
        content = f.readlines()
        Origin_path_cpp = os.getcwd()
        folder_path = os.getcwd() + f'\\{Part_Name}' + f'\\{Folder_Name}'
        os.chdir(folder_path)
        with open(CPP_Name, "w", encoding="utf-8") as file:
            for line in content:
                file.write(line)
    os.chdir(Origin_path_cpp)


def inputPart():
    Part_Numbers = int(input('Please input the number of parts: '))
    Part_Number = 1
    while os.path.isdir(partCreate(Part_Number)):
        Part_Number += 1
    for i in range(1, Part_Numbers+1):
        Part_Name = partCreate(Part_Number)
        foldercppCreate(Part_Name)
        Part_Number += 1


def foldercppCreate(Part_Name):
    print('The Number of Fcpp files must generate in one time because the author so lazy')
    Fcpp_Numbers = int(input('Please input the number of Fcpp files: '))
    for i in range(1, Fcpp_Numbers+1):
        cppCreate(i, Part_Name, i)


def main():
    inputPart()


if __name__ == "__main__":
    main()
