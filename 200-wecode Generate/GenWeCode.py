"""
Python script: GenWeCode.py
Generate folders and C++ files for the problem for WeCode UIT
Created by: NTGNguyen & KevinNitro
"""

import os

# Global variables

cpp_content = r"""
#include <iostream>
using namespace std;

int main()
{
    return 0;
}
""".strip('\n')


def createProblemName(n: int) -> str:
    """Create the name of problem
    arg:
        n: The number of problem"""
    return f'Problem_{n:03}'


def createProblemFolder(folder_name: str) -> None:
    """Create the problem folder
    arg:
        n: The number of problem"""
    os.makedirs(folder_name)


def createCPPName(n: int, i: int) -> str:
    """Create the name of C++ file
    arg:
        n: The number of C++ file"""
    return f'{n}.{i:03}.cpp'


def createOneCPPFile(n: int, i: int) -> None:
    """Create the C++ files in the problem folder
    arg:
        n: The number of C++ file"""
    cpp_name = createCPPName(n, i)
    with open(cpp_name, 'w', encoding='utf-8') as file:
        file.write(cpp_content)


def createCPPFiles(n: int) -> None:
    """Create the C++ files in the problem folder
    arg:
        n: The problem number"""
    number_of_cpp_files = int(input('Please input the number of C++ files: '))
    for i in range(1, number_of_cpp_files+1):
        createOneCPPFile(n, i)


def main():
    while True:
        problem_order = input('Please input the order of problem: ')
        if os.path.isdir(problem_order):
            print(f'The problem {problem_order} already exists!')
        elif problem_order == '0':
            break
        else:
            problem_order = int(problem_order)
            problem_name = createProblemName(problem_order)
            createProblemFolder(problem_name)
            os.chdir(problem_name)
            createCPPFiles(problem_order)
            os.chdir('../')


if __name__ == "__main__":
    main()
