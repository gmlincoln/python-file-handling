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
