import os

for i in range(1, 195):
    project_name = f'Bai{i:03}'
    os.chdir(project_name)

    with open (f'{project_name}.vcxproj.user', 'r') as file:
        content = file.read().replace(r'<ShowAllFiles>true</ShowAllFiles>', r'<ShowAllFiles>false</ShowAllFiles>')

    with open (f'{project_name}.vcxproj.user', 'w') as file:
        file.write(content)

    os.chdir("../")