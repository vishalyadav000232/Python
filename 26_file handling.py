# What is the file handling 

# file handling allow you to read from file and write to files .
#  File can store data permanetaly , unlike the variable wich vanish whwn the programs end 


#  Pythons support many types of file 

#  Text file 
# .txt , .log , .csv

#  Binary File 
# .jpg , .png , .exc


#  File modes in Pythons 

#   "r"      -->         Read ( Defaul ) File must be exist 
#   'w'      -->         Write Create file if not exidt if exist truncates
#   'a'      -->         Append add contents at the end,create if not exis
#   'x'      -->         Exclisive crations fail if file not exist
#   'b"      -->         Binary mode combine with other 
#   't'      -->         Text mode Default combine with other 




# Opening and Closing files 

#  Open file 
f = open("demo.txt" , 'r')
# Read file 
data = f.read()
# Close file 
f.close()
print(data)

# ✅ Best Practices : use with statement to automatically close the file 

with open("Demo.txt" , 'r') as demo:
    content = demo.read()

print(content)

# 🗓️ Reading file 
#  there are multiple way to read file 

# 1️⃣ read() -->  Read whole file 

with open("Demo.txt", "r") as f:
    content = f.read()
    print(content)


# 2️⃣ readline() --> Read one line at one time 

with open("Demo.txt" , 'r') as f:
    first_line = f.readline()
    first_line = f.readline()
    first_line = f.readline()
    first_line = f.readline()
    print(first_line)

#  3️⃣ readlines() --> return all list of line 

with open("Demo.txt" , 'r') as f:
    list = f.readlines()

    for line in list:
        print(line.strip())
    
    print(list)


# ✏️  Write in file 

# 1️⃣ 'w' write mode 

#  OverWrites the existing content create a frash new file

# with open("Demo.txt" , 'w') as f:
#     f.write("this is write by the usngi mode 1'W' \n ")
#     f.write("this is write by the usngi mode 2'W'\n ")




# 2️⃣ 'a' Append mode 

#  Add new content at the end of the existinfg file without deleting old

with open("Demo.txt" , "a") as demo_file:
    demo_file.write("this is write by the append mode it  new ss 2 \n")



#  3️⃣ Writes Multiple lines 

lines = ["1. line \n","2. line \n","3. line \n","4. line \n","5. line \n"]
with open("Demo.txt" , "a") as demo_file:
    demo_file.writelines(lines)



# 👉 File Pointer and seek()

#  file pointer keep track of current postions in the file 
#  tell() --> tells postions
#  seel( ofsret , whencè) --> moves pointer 


with open("Demo.txt" , "r") as f:
    print(f.read(10))    # first 10 char
    print(f.tell())     # tell the current postions 
    f.seek(11)          # go back to that psotions ya phir starts
    print(f.tell())


# Working with binary 

# Binary file stors the non texr data (image audio video etc.)

#  Read Binary file 
import base64
with open("logo.png" , "rb") as f:
    data = f.read()
    print(type(data))

# Write binary file
with open("copy.png", "wb") as f:
    f.write(data)



# Handling file exceptions 

try:
    with open("Demo.txt" ,'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("file does not exist ")

except IOError:
    print("Error reding and writting file ")



#  Checking if file exist or not (os and pathlib)

#  us os 
import os

if os.path.exists("demo.txt"):  # manuly tels 
    print("file exist ")
else:
    print("file not exist")

# use pathlib

from pathlib import Path

file = Path("demo.txt")     

print(file.exists()) # It return a boolen

# Real world example 

#  log writer 

import datetime

with open("log.txt", "a") as f:
    f.write(f"{datetime.datetime.now()} - Event happened\n")


# CSV writer
import csv

csv_data = [
    ["Name", "Age", "City , village"],
    ["Alice", "25", "New York"],
    ["Bob", "30", "Los Angeles"],
    ["Charlie", "22", "Chicago"]
]

with open("data.csv" , "w" , newline="") as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)




# Advance file handling
 



#  Tips and Best preactices
# 1. Always use with open to auto close file 
# 2. use Exception handling to prevent the file crashs
# 3. for large file read line by line
# 4. use pathlib for cross platform file paths
# 5. Keep binary and text oprations seperate to aoide error




# ========================================================================




#  =======================================================================




# ✅ LEVEL–1: Basic Practice Questions

# (These build your foundation: reading, writing, appending, file modes)

# 1️⃣ Write a Python program to create a new file and write 5 lines inside it.

with open("new_file.txt" , 'w') as f:
    f.write("this is the first line 1 \n")
    f.write("this is the second line 2 \n")
    f.write("this is the third line 3 \n")
    f.write("this is the fourth line 4 \n")
    f.write("this is the fifit line 5 \n")



# 2️⃣ Read the file and print the content line by line.

with open("new_file.txt"  , 'r') as f:
    content = f.read()
    print(content)
    print(type(f))
    for line in f:
        print(line)



# 3️⃣ Write a program to count:
# number of lines
# number of words
# number of characters

with open("new_file.txt" , 'r') as f:
    lines = 0
    words = 0
    character = 0
    for line in f:
        lines += 1
        character += len(line)

        word_list = line.strip().split(" ")
        words += len(word_list)
    print("Number of lines : " , lines)
    print("Number of words : " , words)
    print("Number of character : " , character)
        

# 4️⃣ Write a program to append a new line: "This is appended text" at the end of the file.

with open("new_file.txt" , "a") as f:
    f.write("this is the new line add by the appending \n")


# 5️⃣ Write a program to check whether a file exists or not using os.path or pathlib.
import os 
if os.path.exists("new_file.txt"):
    print("file exist ")
else:
    print("file not exist ")

# 6️⃣ Read the first 10 characters of a file using read(n).
with open("new_file.txt" , "r") as f:
    data = f.read(10)
    print("first 10 char inside the file :",data)


# 7️⃣ Move file pointer using seek() and print content from the middle of the file.

with open("new_file.txt" , "r") as f:
    f.seek(12)
    data = f.read(10)
    print()
    print("file starta at char 12 :",data)


# 8️⃣ Program to copy contents from one file to another file.

#  copy from oone file to another file

with open ("new_file.txt" , "r") as src:
    data = src.read()
with open('Demo.txt' , 'a') as ss:
    ss.write(data)


# 9️⃣ Write a program to delete a file safely (check before deleting).

import os

file_path = "Demo.txt"

if os.path.exists(file_path):
    # os.remove(file_path)
    print("file successfully deleted ✅")
else:
    print( " file not found ✅")


# 🔟 Write a program to replace a word in a file:


# Example: Replace "Python" with "PYTHON" everywhere.

with open ("demo.txt" , 'w') as f:
    f.write("hello this is the python \n")
    f.write("hello here is the python \n")
    f.write("hello there is the python \n")
    f.write("hello where is the python \n")

with open("demo.txt" , "r") as ff:
    data = ff.read()
    print(data)
    

data = data.replace("python" , "PYTHON")

with open("demo.txt" , "w") as f:
    f.write(data)

# ✅ LEVEL–2: Intermediate Practice Questions

# (Logic-based problems – very important for interviews)

# 1️⃣ Read a file and remove all blank lines. Write cleaned data to a new file.


input_file = "input_file.txt"
output_file = "output_file.txt"
cleaned_lines = []


with open(input_file , "r") as file :
    for line in file:
        if line.strip():
            cleaned_lines.append(line)

# Step 2: Write cleaned data to new file
with open(output_file, "w") as f:
    f.write(data)
    f.writelines(cleaned_lines)

print("Blank lines removed successfully! Check cleaned.txt")


# 2️⃣ Reverse the content of a file line-by-line.

input_file = "input.txt"
output_file = "reversed.txt"

reversed_lines = []

# Step 1: Read file
with open(input_file, "r") as fa:
    for line in fa:
        # Reverse each line
        reversed_line = line.rstrip("\n")[::-1]   # reverse string
        reversed_lines.append(reversed_line + "\n")

# Step 2: Write reversed output to new file
with open(output_file, "w") as f:
    f.writelines(reversed_lines)

print("Lines reversed successfully! Check reversed.txt")

# 3️⃣ Read a file and print only unique lines (remove duplicates).

# 4️⃣ Program to merge two text files into a third file.
# 5️⃣ Write a program that logs every program run into a log file with timestamp.
# 6️⃣ Read a big file (100MB+) line by line without loading full file → show memory-safe method.
# 7️⃣ Count frequency of each word in a file (build a dictionary).
# 8️⃣ Convert a text file into uppercase and save it in a new file.
# 9️⃣ Read a file and find the longest word in it.
# 🔟 Read a file and print line numbers like:
# 1: This is line one
# 2: This is line two

# ✅ LEVEL–3: Advanced / Real-life File Handling Problems

# (These are real-world challenges)

# 1️⃣ CSV File Handling

# Without using pandas:

# Read a CSV and print all rows

# Count how many entries

# Sort data based on a column

# Filter data (e.g., age > 25)

# Write filtered data to a new CSV

# 2️⃣ JSON File Handling

# Create a JSON file with multiple users

# Read JSON and print one specific user

# Add new user into JSON file

# Update / delete a field

# 3️⃣ Log Reader

# Given a log file like:

# 2024-01-22 10:45:23 - ERROR: Disk full
# 2024-01-22 10:46:13 - INFO: Server started


# Tasks:

# Count number of ERROR, INFO, WARNING

# Extract all errors into a separate file

# Sort logs by timestamp

# 4️⃣ Binary File Handling

# Write bytes to a binary file

# Read an image file and create a duplicate

# Extract only first 100 bytes from a binary file

# 5️⃣ Text Search Engine

# Create a program that:

# Searches a word in a file

# Shows line numbers where word appears
print("th")