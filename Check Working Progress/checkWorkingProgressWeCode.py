"""
Python script for checking working progress of 200-wecode
"""

import re
import os

re_unworked = r'\[!\[Unworked Badge\].+'
re_worked = r'\[!\[Worked Badge\].+'
replace_unworked_project_badge = r'[![Unworked Badge](https://img.shields.io/badge/pending-{count_unworked_projects}%20%2F%20{count_projects}-FF8080?style=for-the-badge)](./UnworkedProject.md)'
replace_worked_project_badge = r'[![Worked Badge](https://img.shields.io/badge/done-{count_worked_projects}%20%2F%20{count_projects}-82A0D8?style=for-the-badge)](./WorkedProject.md)'
README_file_dir = 'docs/README.md'
unworked_project_filename = 'docs/UnworkedProject.md'
worked_project_filename = 'docs/WorkedProject.md'
undone_sign_list = [r'//undone', r'//chuaxong', r'//chưaxong',
                    r'//haventdone', r'//haven\'tdone']
done_sign_list = [r'//done', r'//xong', r'//daxong', r'//đãxong']
unworked_project_file_content = r"""
## UNWORKED PROJECTS

List các file chưa làm:

""".lstrip('\n')
worked_project_file_content = r"""
## WORKED PROJECTS

List các file đã làm:

""".lstrip('\n')


def listOfProject():
    global cpp_files_paths
    global count_projects
    cpp_files_paths = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.cpp'):
                cpp_files_paths.append(os.path.join(root, file))
    cpp_files_paths.sort()
    count_projects = len(cpp_files_paths)


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


def createMarkDownFile(cpp_file_path, markdown_file, i):
    cpp_file_relative_path = cpp_file_path.replace(
        ' ', '%20').replace('\\', '/')[2:]
    cpp_file_basename = os.path.basename(
        cpp_file_path).replace('.cpp', '')
    with open(markdown_file, 'a', encoding='utf8') as file:
        file.write(
            f'{i}.\t[{cpp_file_basename}](../{cpp_file_relative_path})\n')


def checkWorkedProject():
    global count_worked_projects
    count_worked_projects = 0

    with open(unworked_project_filename, 'w', encoding='utf8') as file:
        file.write(f'{unworked_project_file_content}'.format())

    with open(worked_project_filename, 'w', encoding='utf8') as file:
        file.write(f'{worked_project_file_content}'.format())

    index_for_worked = 1
    index_for_unworked = 1
    for cpp_file_path in cpp_files_paths:
        if forceCheckDone(cpp_file_path) == -1 or os.path.getsize(cpp_file_path) < 100:
            createMarkDownFile(
                cpp_file_path, unworked_project_filename, index_for_unworked)
            index_for_unworked += 1
        else:
            count_worked_projects += 1
            createMarkDownFile(
                cpp_file_path, worked_project_filename, index_for_worked)


def editREADME():
    with open(README_file_dir, 'r', encoding='utf8') as file:
        content = file.readlines()

    with open(README_file_dir, 'w', encoding='utf8') as file:
        for line in content:
            if re.match(re_worked, line):
                file.write(
                    f'{replace_worked_project_badge}\n'.format(count_worked_projects=count_worked_projects, count_projects=count_projects))
            elif re.match(re_unworked, line):
                file.write(
                    f'{replace_unworked_project_badge}\n'.format(count_unworked_projects=count_projects - count_worked_projects, count_projects=count_projects))
            else:
                file.write(line)


def main():
    listOfProject()
    checkWorkedProject()
    editREADME()


if __name__ == "__main__":
    main()
