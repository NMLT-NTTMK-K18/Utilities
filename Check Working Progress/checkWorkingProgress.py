import re
import os

re_pattern = r'.*Bai[0-9]{3}'
re_pattern_readme = r'\[!\[WorkedProject Badge\].+'
replace_worked_project_badge = r'[![WorkedProject Badge](https://img.shields.io/badge/progress-{count_worked_files}%20%2F%20{count_projects}-82A0D8?style=for-the-badge)](./UnworkedProject.md)'
source_code_filename = 'Source.cpp'
README_file_dir = 'docs/README.md'
UnworkedProject_filename = 'docs/UnworkedProject.md'
undone_sign_list = [r'//undone', r'//chuaxong',
                    r'//haventdone', r'//haven\'tdone']
done_sign_list = [r'//done', r'//xong', r'//daxong', r'//đãxong']
UnworkedProject_file_content = r"""
## UNWORKED PROJECTS

List các file `{source_code_filename}` chưa làm:

""".format(source_code_filename=source_code_filename)


def listOfProject():
    global directories
    global count_projects
    directories = []
    directories += [project_dir for project_dir in os.listdir(
        './') if re.match(re_pattern, project_dir) and os.path.isdir(project_dir)]
    directories.sort()
    count_projects = len(directories)


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
    for project_dir in directories:
        file_path = os.path.join(project_dir, source_code_filename)
        if forceCheckDoneStatus := (forceCheckDone(file_path)) == 1:
            count_worked_files += 1
        elif forceCheckDoneStatus == 0 and os.path.getsize(file_path) > 100:
            count_worked_files += 1
        else:
            project_dir_relative_path = project_dir.replace(' ', '%20')
            with open(UnworkedProject_filename, 'a', encoding='utf8') as file:
                file.write(
                    f'{i}.\t[{project_dir}](../{project_dir_relative_path}/{source_code_filename})\n')
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
