"""
Python script for checking working progress of 200-wecode
"""

import re
import os

re_pattern_readme = r'\[!\[WorkedProject Badge\].+'
replace_worked_project_badge = r'[![WorkedProject Badge](https://img.shields.io/badge/progress-{count_worked_files}%20%2F%20{count_projects}-82A0D8?style=for-the-badge)](./UnworkedProject.md)'
README_file_dir = 'docs/README.md'
UnworkedProject_filename = 'docs/UnworkedProject.md'
undone_sign_list = [r'//undone', r'//chuaxong', r'//chưaxong',
                    r'//haventdone', r'//haven\'tdone']
done_sign_list = [r'//done', r'//xong', r'//daxong', r'//đãxong']
UnworkedProject_file_content = r"""
## UNWORKED PROJECTS

List các file chưa làm:

""".lstrip('\n')


def listOfProject():
    global cpp_files_aths
    global count_projects
    cpp_files_aths = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.cpp'):
                cpp_files_aths.append(os.path.join(root, file))
    cpp_files_aths.sort()
    count_projects = len(cpp_files_aths)


def forceCheckDone(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        content = f.read().replace(' ', '').lower()

    for sign in undone_sign_list:
        if sign in content:
            return -1

    for sign in done_sign_list:
        if sign in content:
            return 1

    return 0


def checkWorkedProject():
    global count_worked_files
    count_worked_files = 0

    with open(UnworkedProject_filename, 'w', encoding='utf8') as file:
        file.write(f'{UnworkedProject_file_content}'.format())

    i = 1
    for cpp_file_path in cpp_files_aths:
        if forceCheckDoneStatus := (forceCheckDone(cpp_file_path)) == 1:
            count_worked_files += 1
        elif forceCheckDoneStatus == 0 and os.path.getsize(cpp_file_path) > 100:
            count_worked_files += 1
        else:
            cpp_file_relative_path = cpp_file_path.replace(
                ' ', '%20').replace('\\', '/')[2:]
            cpp_file_basename = os.path.basename(
                cpp_file_path).replace('.cpp', '')
            with open(UnworkedProject_filename, 'a', encoding='utf8') as file:
                file.write(
                    f'{i}.\t[{cpp_file_basename}](../{cpp_file_relative_path})\n')
            i += 1


def editREADME():
    with open(README_file_dir, 'r', encoding='utf8') as file:
        content = file.readlines()

    with open(README_file_dir, 'w', encoding='utf8') as file:
        for line in content:
            if re.match(re_pattern_readme, line):
                file.write(
                    f'{replace_worked_project_badge}\n'.format(count_worked_files=count_worked_files, count_projects=count_projects))
            else:
                file.write(line)


def main():
    listOfProject()
    checkWorkedProject()
    editREADME()


if __name__ == "__main__":
    main()
