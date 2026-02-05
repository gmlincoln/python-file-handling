#Create file

""" 
with open("python02.txt", "w") as myFile:
    myFile.write("This is a text file...")

#Read file
with open("python02.txt", "r") as myFile:
    content = myFile.read()
    print(content)
        
"""

import os 

# os.rename("python02.txt", "python.txt")

# os.remove("python.txt")



# os.makedirs("2026", exist_ok = True)
# os.makedirs("2026/01", exist_ok = True)
# os.makedirs("2026/02", exist_ok = True)
# os.makedirs("2026/02/05", exist_ok = True)
# os.makedirs("2026/02/04", exist_ok = True)

# with open("2026/02/05/shoishob.png", "w") as pngFile:
    
#     pngFile.write("")

import shutil

# shutil.make_archive("2026_archive", "zip", "2026")

import zipfile

"""

with zipfile.ZipFile("2026_archive.zip", "r" ) as zip_ref:
    zip_ref.extractall("extracted_folder")
    
"""

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
    [9, "Lincoln", 3.85]
]

# with open('students.csv', "w", newline="") as myCSV:
#     writer = csv.writer(myCSV)
    
#     writer.writerows(rows)

with open("students.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    
    for r in reader:
        print(r)
        
        