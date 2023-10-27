# UTILITIES

[![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/NMLT-NTTMK-K18/Utilities?style=for-the-badge&color=CAEDFF)](../../../commits/main)
![GitHub repo size](https://img.shields.io/github/repo-size/NMLT-NTTMK-K18/Utilities?style=for-the-badge&color=D8B4F8)
[![GitHub contributors](https://img.shields.io/github/contributors/NMLT-NTTMK-K18/Utilities?style=for-the-badge&color=FBF0B2)](../../../graphs/contributors)
[![CodeFactor](https://img.shields.io/codefactor/grade/github/nmlt-nttmk-k18/Utilities?style=for-the-badge)](https://www.codefactor.io/repository/github/nmlt-nttmk-k18/Utilities)

## TABLE OF CONTENTS

-   [UTILITIES](#utilities)
    -   [TABLE OF CONTENTS](#table-of-contents)
    -   [SAMPLE INPUT FILES](#sample-input-files)
    -   [GENERATE VISUAL STUDIO SOLUTION \& PROJECTS](#generate-visual-studio-solution--projects)
    -   [GENERATE WECODE REPO](#generate-wecode-repo)
    -   [INSTALL MINGW FOR C++ COMPILER](#install-mingw-for-c-compiler)
    -   [.GITGIRNORE TEMPLATE](#gitgirnore-template)
    -   [.GITATTRIBUTES TEMPLATE](#gitattributes-template)
    -   [COLOR](#color)
        -   [Pastel](#pastel)
        -   [Order](#order)

---

## SAMPLE INPUT FILES

Đây là các file template input từ thầy Khang để dùng cho việc import từ file

[![Int Data input files](https://img.shields.io/badge/int_data_inp-download-FF8080?style=for-the-badge)](../../releases/download/INP/INT_DATA_INP.zip)
[![Float Data input files](https://img.shields.io/badge/float_data_inp-download-FFCF96?style=for-the-badge)](../../releases/download/INP/FLOAT_DATA_INP.zip)

[![Float Matrix input files](https://img.shields.io/badge/float_matrix_inp-download-F6FDC3?style=for-the-badge)](../../releases/download/INP/FLOAT_MATRIX_DATA_INP.zip)
[![Float Matrix input files](https://img.shields.io/badge/float_matrix_inp-download-CDFAD5?style=for-the-badge)](../../releases/download/INP/FLOAT_MATRIX_DATA_INP.zip)

---

## GENERATE VISUAL STUDIO SOLUTION & PROJECTS

-   Tạo cấu trúc folder giống như tạo project trên VS

[![genVS.py](https://img.shields.io/badge/gen_VS-click_&_save-D2E0FB?style=for-the-badge&logo=visual-studio)](../../raw/main/Generate%20VS%20Solution%20%26%20Projects/genVS.py)
[![genVS V2.py](https://img.shields.io/badge/gen_VS_v2-click_&_save-D7E5CA?style=for-the-badge&logo=visual-studio)](../../raw/main/Generate%20VS%20Solution%20%26%20Projects/genVS_v2.py)

> **Note**
>
> -   `genVS.py`: Phiên bản cũ, chỉ tạo được nhiều project với theo 1 số lượng
>
> -   `genVS V2.py` _(Recommend)_: Phiên bản mới, tạo được nhiều project với nhiều số lượng khác nhau
>
>     > Ví dụ: Mở bài [5-258-struct](../5-258-struct) ra là biết chứ không biết diễn tả sao 😕

> **Important**
>
> Vì là sử dụng random `uuid4()` nên sẽ có tỉ lệ vô cùng nhỏ trùng uuid :v hên xui khi gen

---

## GENERATE WECODE REPO

[![GenWeCode.py](https://img.shields.io/badge/gen_wecode-click_&_save-D2E0FB?style=for-the-badge&logo)](../../raw/main/200-wecode%20Generate/GenWeCode.py)

-   Dùng để tạo giống repo [7-200-wecode](../7-200-wecode/)

---

## INSTALL MINGW FOR C++ COMPILER

-   Tải nhanh luôn _(Windows nha)_
-   Tải rồi set env path cho nó

[![MinGW x32](https://img.shields.io/badge/MinGW_x32-download-D2E0FB?style=for-the-badge)](../../releases/download/MinGW/MinGW.x32.zip)
[![MinGW x64](https://img.shields.io/badge/MinGW_x64-download-D7E5CA?style=for-the-badge)](../../releases/download/MinGW/MinGW.x64.zip)

> **Note**
>
> ### Source installer
>
> Cho ai thích cài từ source
>
> -   x64: https://github.com/Vuniverse0/mingwInstaller/releases/ (Choose POSIX instead Win32)
>
> -   x32: https://sourceforge.net/projects/mingw/files/Installer/mingw-get-setup.exe/download

---

## .GITGIRNORE TEMPLATE

```.gitignore
# No tracking stuff
.vs
.vscode
**/*test*
**/*temp*

# VS
**/x64
**/x86
**/*.exe # CodeRuner C++ compiled file ignore

# CodeBlocks
**/*bin
**/*obj
**/TestCodeBlock*

# Python
**/*.py
```

## .GITATTRIBUTES TEMPLATE

```.gitattributes
**/*.cpp linguist-language=C++ eol=lf
```

## COLOR

### Pastel

-   For each name of repo: https://colorhunt.co/palette/ecee818ddfcb82a0d8edb7ed
-   Information in .github repo:
    -   https://colorkit.co/palette/ffadad-ffd6a5-fdffb6-caffbf-9bf6ff-a0c4ff-bdb2ff-ffc6ff
    -   https://colorhunt.co/palette/fbf0b2ffc7ead8b4f8caedff

### Order

-   red
-   orange
-   yellow
-   green
-   blue
-   brown
-   white
-   grey
