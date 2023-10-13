import os

for i in range(1,168):
    folder_name = f'Bai{i:03}'
    os.chdir(folder_name)
    os.rename('source.cpp', 'Source.cpp')

    with open(f'{folder_name}.vcxproj', 'r', encoding='utf-8') as f:
        vcxproj_content = f.read().replace('source.cpp', 'Source.cpp')
    with open(f'{folder_name}.vcxproj', 'w', encoding='utf-8') as f:
        f.write(vcxproj_content)

    with open(f'{folder_name}.vcxproj.filters', 'r', encoding='utf-8') as f:
        vcxproj_filters_content = f.read().replace('source.cpp', 'Source.cpp')
    with open(f'{folder_name}.vcxproj.filters', 'w', encoding='utf-8') as f:
        f.write(vcxproj_filters_content)

    os.chdir('../')