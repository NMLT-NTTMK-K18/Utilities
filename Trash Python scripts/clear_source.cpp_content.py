import os

for i in range(1, 195):
    project_name = f'Bai{i:03}'
    os.chdir(project_name)

    with open ('Source.cpp', 'w') as file:
        file.write('')

    os.chdir("../")