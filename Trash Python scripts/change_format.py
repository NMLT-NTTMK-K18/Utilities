import os

list_index = [1] + list(range(84, 168))


for i in list_index:
    i_width_3 = f'{i:03}'
    cpp_file_name = f'Bai_{i_width_3}.cpp'
    folder_name = f'Bài {i_width_3}'
    new_folder_name = f'Bai{i_width_3}'
    os.chdir(folder_name)
    os.rename(cpp_file_name, 'Source.cpp')
    os.rename(folder_name + '.vcxproj', new_folder_name + '.vcxproj')
    os.rename(folder_name + '.vcxproj.filters', new_folder_name + '.vcxproj.filters')
    os.rename(folder_name + '.vcxproj.user', new_folder_name + '.vcxproj.user')
    
    with open(new_folder_name + '.vcxproj', 'r', encoding='utf8') as file:
        content_vcxproj = file.read()
    content_vcxproj = content_vcxproj.replace(cpp_file_name, 'Source.cpp')
    with open(new_folder_name + '.vcxproj', 'w', encoding='utf8') as file:
        file.write(content_vcxproj)

    with open(new_folder_name + '.vcxproj.filters', 'r', encoding='utf8') as file:
        content_vcxproj_filters = file.read()
    content_vcxproj_filters = content_vcxproj_filters.replace(cpp_file_name, 'Source.cpp')
    with open(new_folder_name + '.vcxproj.filters', 'w', encoding='utf8') as file:
        file.write(content_vcxproj_filters)

    os.chdir('../')
    os.rename(folder_name, new_folder_name)


with open('UIT_23520161.sln', 'r', encoding='utf-8') as file:
    content = file.read()

    for i in list_index:
        i_width_3 = f'{i:03}'
        folder_name = f'Bài {i_width_3}'
        new_folder_name = f'Bai{i_width_3}'
        content = content.replace(folder_name, new_folder_name)

with open('UIT_23520161.sln', 'w', encoding='utf-8') as file:
    file.write(content)