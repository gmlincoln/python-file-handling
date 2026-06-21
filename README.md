# 📁 Python File Handling, OS Operations, ZIP & CSV Management, Error Handling

This project is a practical demonstration of **Python file handling** and working with important built-in modules such as `os`, `shutil`, `zipfile`, and `csv`.

It covers:

- Creating, reading, renaming, and deleting files
- Creating folders and subfolders
- Creating and extracting ZIP archives
- Writing and reading CSV files

This project is ideal for beginners to understand real-world file and directory operations in Python.

---

## 🧰 Modules Used

| Module   | Purpose                                      |
|-----------|----------------------------------------------|
| `os`      | File and directory operations                |
| `shutil`  | Creating ZIP archive                        |
| `zipfile` | Extracting ZIP files                        |
| `csv`     | Writing and reading CSV files               |
| `math`    |   Mathematical calculations               |
| `random`  |   Random number generation               |
| `datetime`|   Date and time operations               |

---

## 📝 1. Create and Read a Text File

```python
with open("python02.txt", "w") as myFile:
    myFile.write("This is a text file...")

with open("python02.txt", "r") as myFile:
    content = myFile.read()
    print(content)
```

## 🗂️ 2. Rename and Delete a File

```python
import os

os.rename("python02.txt", "python.txt")
os.remove("python.txt")
```

## 📁 3. Create Nested Directories

```python
os.makedirs("2026/02/05", exist_ok=True)
os.makedirs("2026/02/04", exist_ok=True)

```



## 🖼️ 4. Create an Empty File Inside Folder
```python
with open("2026/02/05/shoishob.png", "w") as pngFile:
    pngFile.write("")

```

## 🗜️ 5. Create a ZIP Archive of a Folder

```python
import shutil

shutil.make_archive("2026_archive", "zip", "2026")

```

## 📦 6. Extract ZIP File

```python
import zipfile

with zipfile.ZipFile("2026_archive.zip", "r") as zip_ref:
    zip_ref.extractall("extracted_folder")

```

## 📊 7. Write Data to CSV File

```python
import csv

rows = [
    ["ID", "Name", "CGPA"],
    [1, "Shoishob", 3.00],
    [2, "Tanvir", 2.85],
    [3, "Omin", 3.50],
    [4, "Fahim", 3.75],
    [5, "Ipshita", 3.52],
    [6, "Neha", 3.47],
    [7, "Bithi", 2.73],
    [8, "Mahmuda", 3.46],
    [9, "Lincoln", 00.00]
]

with open('students.csv', "w", newline="") as myCSV:
    writer = csv.writer(myCSV)
    writer.writerows(rows)

```
## 📖 8. Read Data from CSV File

```python

with open("students.csv", "r") as csv_file:
    reader = csv.reader(csv_file)

    for r in reader:
        print(r)

```
# Error Handling in Python (File Reading)

## 📌 Overview
This project demonstrates how to handle errors while reading a file in Python using `try`, `except`, and `finally` blocks.  
It safely attempts to read a file and prevents the program from crashing if something goes wrong.

---

## 🧠 Purpose of Error Handling
Error handling is used to:
- Prevent runtime crashes
- Handle missing or inaccessible files
- Ensure important messages or cleanup code always runs

---

## 9 Math Module
### What is the Math Module?
-  The math module provides mathematical functions and constants such as:

``` 
Square root
Power
Pi value
Trigonometric functions
Rounding operations

```
#### Example

```python 
import math

print(math.sqrt(25))
print(math.pi)
print(math.ceil(4.2))
print(math.floor(4.9))
```
```
```cmd
Output
5.0
3.141592653589793
5
4
```
####  Explanation
Function	Description
math.sqrt(x)	Returns the square root of x
math.pi	Returns the value of π
math.ceil(x)	Rounds up to the nearest integer
math.floor(x)	Rounds down to the nearest integer


## 🧾 Code Explanation

### 🔹 try block
```python
try:
    with open("file_name.txt", "r") as file:
        content = file.read()
    
        print(content)

except Exception as e:
    # print(f"Error type: {e}")
    pass
    
finally:
    print("Something went Wrong! Try again later.")

```







```