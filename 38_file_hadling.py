'''
What is the file Handling 


file hadnling ,means  working with the file sotre in your computer 


.txt (text files)

.csv (Excel-like data)

.json (API / config data)

.bin (binary files)

.pkl (pickle objects)

Type of the data file 

Text file --> .txt, .csv, .json, .py
Binary File ---> .jpg, .png, .mp3, .pdf, .exe, .pkl



Mode	Meaning	           If file not exists	          Pointer position
"r"  |	Read only	            ❌ Error	                      start
"w"	 | Write (overwrite)	   ✅ creates	                       start
"a"	 | Append (add at end).  	✅ creates	                        end
"x"	 | Create new file	       ❌ Error if exists	                    start
"r+" |	Read + Write	        ❌ Error	                                start
"w+" |	Write + Read	       ✅ creates	         start (but old data deleted)
"a+" |	Append + Read	       ✅ creates	                        end

'''

# Opening file 

with open("data.txt" , 'w') as f:
    f.write("this is the first hrllo line \n ")
    f.write("this is the second hrllo line \n ")


#  Reading text file 

# 1--> read() - read full file
 
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

# 2--> readline() - read one line 



with open("data.txt", "r") as f:
    line = f.readline()
    print(line)


# 3--> readlines() -- reald all lines 

with open("data.txt", "r") as f:
    lines = f.readlines()
    print(lines)


# 4--> best way to the loop  (memory efficient )

with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())


# Writting in the file 

# ✅ A) write() (writes string)

with open("data.txt", "w") as f:
    f.write("Hello Vishal\n")
    f.write("Welcome to File Handling\n")

# ✅ B) writelines() (writes list of strings)
# ⚠️ write lines does not automatically add \n


lines = ["Line1\n", "Line2\n", "Line3\n"] # list of the lines

with open("data.txt", "w") as f:
    f.writelines(lines)




# Binary file reading / writting 

import base64

with open("logo.png", "rb") as src:
    data = src.read()

encoded = base64.b64encode(data)

with open("image.txt", "wb") as f:
    f.write(encoded)



#  with statement (most importent )

#  it is used becouse it automatically closed the file 

'''
with ensures:

file closes automatically

safe and clean code

industry standard

'''
# bad way 

f = open("data.txt", "r")
print(f.read())
f.close()


#  best way 

with open("data.txt", "r") as f:
    print(f.read())





#  CSV File (common seperated value )

'''
Excel export/import

reports

database dumps
'''

print("CSV (COMMON SEPERATED VALUE )")
import csv


data = [
    ["name", "age"],
    ["Vishal", 21],
    ["Aman", 22]
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)


with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)



# Dict reader 


# writer


with open("students.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Vishal", "age": 21})


# reader


with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])



# json ()


'''
APIs

frontend-backend communication

config files
'''

data = {
  "name": "Vishal",
  "age": 21
}


import json



with open("data.json", "w") as f:
    json.dump(data, f, indent=4)




with open("data.json", "r") as f:
    data = json.load(f)

print(type(data))


#  dumps()  and dump()



age = int(input("enter the age :"))
day = str(input("enter the day :"))

price = 12

if age < 18:
    price = 8
if day == "wed":
    price -= 2

print("price" , price)



# json main all methos 


# 1--> json.dump(obj , file , indent = None , ensure_ascii = false , sort_key = false)

'''
obj →    Python data (dict/list)
fp →     file object (opened file)
indent → pretty formatting (spaces)
ensure_ascii → if False, allows Hindi/Unicode text properly
sort_keys → sort keys alphabetically
separators → custom formatting (advanced)'''



import json

student = {"name": "Vishal", "age": 21}

with open("student.json", "w", encoding="utf-8") as f:
    json.dump(student, f, indent=4, ensure_ascii=False)


# json.load()

with open("student.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)         # dict
print(data["name"]) # Vishal


