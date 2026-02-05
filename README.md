# 📁 Python File Handling, OS Operations, ZIP & CSV Management

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