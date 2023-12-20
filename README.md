# UTILITIES

[![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/NMLT-NTTMK-K18/Utilities?style=for-the-badge&color=CAEDFF)](../../../commits/main)
![GitHub repo size](https://img.shields.io/github/repo-size/NMLT-NTTMK-K18/Utilities?style=for-the-badge&color=D8B4F8)
[![GitHub contributors](https://img.shields.io/github/contributors/NMLT-NTTMK-K18/Utilities?style=for-the-badge&color=FBF0B2)](../../../graphs/contributors)
[![CodeFactor](https://img.shields.io/codefactor/grade/github/nmlt-nttmk-k18/Utilities?style=for-the-badge)](https://www.codefactor.io/repository/github/nmlt-nttmk-k18/Utilities)

## TABLE OF CONTENTS

-   [UTILITIES](#utilities)
    -   [TABLE OF CONTENTS](#table-of-contents)
    -   [🔢 SAMPLE INPUT FILES](#-sample-input-files)
    -   [💥 GENERATE VISUAL STUDIO SOLUTION \& PROJECTS](#-generate-visual-studio-solution--projects)
    -   [😌 COPY ANSWER FROM DOC _(Windows Powershell Script)_](#-copy-answer-from-doc-windows-powershell-script)
    -   [🤨 GENERATE WECODE REPO](#-generate-wecode-repo)
    -   [⚙️ INSTALL MINGW FOR C++ COMPILER](#️-install-mingw-for-c-compiler)
    -   [.GITGIRNORE TEMPLATE](#gitgirnore-template)
    -   [.GITATTRIBUTES TEMPLATE](#gitattributes-template)
    -   [COLOR](#color)
        -   [Pastel](#pastel)
        -   [Order](#order)

---

## 🔢 SAMPLE INPUT FILES

Đây là các file template input từ thầy Khang để dùng cho việc import từ file

[![Int Data input files](https://img.shields.io/badge/int_data_inp-download-FF8080?style=for-the-badge)](../../releases/download/INP/INT_DATA_INP.zip)
[![Float Data input files](https://img.shields.io/badge/float_data_inp-download-FFCF96?style=for-the-badge)](../../releases/download/INP/FLOAT_DATA_INP.zip)

[![Float Matrix input files](https://img.shields.io/badge/float_matrix_inp-download-F6FDC3?style=for-the-badge)](../../releases/download/INP/FLOAT_MATRIX_DATA_INP.zip)
[![Float Matrix input files](https://img.shields.io/badge/float_matrix_inp-download-CDFAD5?style=for-the-badge)](../../releases/download/INP/FLOAT_MATRIX_DATA_INP.zip)

---

## 💥 GENERATE VISUAL STUDIO SOLUTION & PROJECTS

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
>
> -   File `.cpp` chỉ cố định là `Source.cpp`, lười implement thêm `Bai???.cpp`

> **Important**
>
> Vì là sử dụng random `uuid4()` nên sẽ có tỉ lệ vô cùng nhỏ trùng uuid :v hên xui khi gen

---

## 😌 COPY ANSWER FROM DOC _(Windows Powershell Script)_

[![copyAnswerFromDoc.ps1](https://img.shields.io/badge/copy_answer_from_doc-click_&_save-D2E0FB?style=for-the-badge)](../../raw/main/Copy%20Answer%20From%20Doc/copyAnswerFromDoc.ps1)

-   Copy, edit, đưa lại clipboard đáp án từ tài liệu của thầy Khang
-   Có thể để script ngoài desktop, taskbar, start menu _(C:\ProgramData\Microsoft\Windows\Start Menu\Programs)_ để dễ mở

**Ví dụ:**

1. Copy từ tài liệu vào clipboard

    ```pdf
    1.     int main()
    2.     {
    3.     int n;
    4.     cout << "Nhap n: ";
    5.     cin >> n;
    00892.
    Đệ quy tuyến tính
    40
    6.     int kq = DemChuSo(n);
    7.     cout << "Ket qua: " << kq;
    8.     return 1;
    9.     }
    ```

2. Ấn chạy script
3. Paste dô file `.cpp` và dùng formatter để format lại 😌 _(Không format nó không indent scope đâu 🤨)_

    ```.cpp
    int main()
    {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    int kq = DemChuSo(n);
    cout << "Ket qua: " << kq;
    return 1;
    }
    ```

---

## 🤨 GENERATE WECODE REPO

[![GenWeCode.py](https://img.shields.io/badge/gen_wecode-click_&_save-D2E0FB?style=for-the-badge&logo)](../../raw/main/200-wecode%20Generate/GenWeCode.py)

-   Dùng để tạo giống repo [7-200-wecode](../7-200-wecode/)

---

## ⚙️ INSTALL MINGW FOR C++ COMPILER

-   Tải nhanh luôn _(Windows)_
-   Tải rồi set env path

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

```.gitignore
**/*.cpp text linguist-language=C++ eol=crlf
```

<!-- Để .gitignore cho nó lên màu render markdown cho đẹp :v-->

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
