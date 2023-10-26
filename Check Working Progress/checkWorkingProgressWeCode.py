"""
Python script for checking working progress of 200-wecode
"""

import re
import os

# GLOBAL VARS

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
work_readme_problem_header = r"""
## {problem}

"""


def listOfProject():
    # global cpp_files_paths
    global count_projects
    global dict_of_problem_contains_projects
    dict_of_problem_contains_projects = {}
    count_projects = 0
    problem_folders = [
        folder for folder in os.listdir() if folder.startswith('Problem')]
    problem_folders.sort()
    for problem_folder in problem_folders:
        cpp_file_list = []
        for cpp_file in os.listdir(problem_folder):
            if cpp_file.endswith('.cpp'):
                cpp_file_list += [cpp_file]
                count_projects += 1
        cpp_file_list.sort()
        dict_of_problem_contains_projects.update(
            {problem_folder: cpp_file_list})


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


def editWorkMarkDownFile(cpp_file_path, markdown_file, i):
    cpp_file_relative_path = cpp_file_path.replace(
        ' ', '%20').replace('\\', '/')
    cpp_file_basename = os.path.basename(
        cpp_file_path).replace('.cpp', '')
    with open(markdown_file, 'a', encoding='utf8') as file:
        file.write(
            f'{i}.\t[{cpp_file_basename}](../{cpp_file_relative_path})\n')


def checkWorkedProject():
    global count_worked_projects
    count_worked_projects = 0

    with open(unworked_project_filename, 'w', encoding='utf8') as file:
        file.write(f'{unworked_project_file_content}')

    with open(worked_project_filename, 'w', encoding='utf8') as file:
        file.write(f'{worked_project_file_content}')

    for problem_folder, cpp_file_list in dict_of_problem_contains_projects.items():
        index_done = 1
        index_undone = 1
        with open(unworked_project_filename, 'a', encoding='utf8') as file:
            file.write(work_readme_problem_header.format(
                problem=problem_folder.upper()))
        with open(worked_project_filename, 'a', encoding='utf8') as file:
            file.write(work_readme_problem_header.format(
                problem=problem_folder.upper()))
        for cpp_file in cpp_file_list:
            cpp_file_path = os.path.join(problem_folder, cpp_file)
            if forceCheckDone(cpp_file_path) == -1 or os.path.getsize(cpp_file_path) < 100:
                editWorkMarkDownFile(cpp_file_path, unworked_project_filename,
                                     index_undone)
                index_undone += 1
            else:
                count_worked_projects += 1
                editWorkMarkDownFile(cpp_file_path, worked_project_filename,
                                     index_done)
                index_done += 1


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
