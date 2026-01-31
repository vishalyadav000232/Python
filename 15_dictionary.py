print("Dictionary Basic to Advance")


# A dictionary is collection of a keyy value pairs

# Key value always unique .

#  value -> any data type 

# element arrange in ordered manner 

#  Syntax :-  dic_name = { key1 : value , key2 : value}



# ✅ 2. How to Create a Dictionary

# Using the curly braces 

dict_name = { 'name' : 'vishl' , 'age' : 23 , 'isMale' : True}
print(dict_name)
print(len(dict_name))
print(type(dict_name))


# using dict() constructer 

dict_const = dict(add = "varansi"  , graduation = "B-tech")

print(dict_const)


# Empty Dictionary 

empty_dict = dict()
print(empty_dict)



# Accessing Dictionar Items 

# Access using Key 

dict_name = { 'name' : 'vishl' , 'age' : 23 , 'isMale' : True}
print(dict_name["name"])

# Accessing using get()

print(dict_name.get("age" , "not Found")) # not found 


# Adding and update dictionary 

# add new key value  pair 

dict_name["newKey"]= "this is new kewword "
print(dict_name)

# update the existing key value pairs 

dict_name["age"] = 22
print(dict_name)


# Update the multiple value using the update()

dict_name.update({"pytho" : 23 , "temaIndia": False})
print(dict_name)


#  Removing the Items all syntax 

# using pop(key) remove the spacific key

dict_name.pop("temaIndia")
print(dict_name)

#  Remove the lasr inserted pair  using the popitem()
dict_name.popitem()
print(dict_name)

# del keyword 

del dict_name["newKey"]

print(dict_name)

'''
 del keyword delet the key value and does not return any value 
 if the key does not exist then throw the error key error 
 
'''

# Clear the all dictionary 

# dict_name.clear()
# print(dict_name)


#  All dictionary methods

# copy() return the new dictionary with copy the all items 

new_dict_copy = dict_name.copy()
print(new_dict_copy)
print(id(new_dict_copy) , id(dict_name))

d=dict_name.items()
print(d)




# Dictionary all looping techniques 

# Loop through the key 

for key in dict_name.keys():
    print(key)

#  Loop through the value 

for value in dict_name.values():
    print( value)

#   Loop through the key value pairs 

for key , value  in dict_name.items():
    print( f"{key} : {value}")



for tuple  in dict_name.items(): # items is return in the tuple form key value 
  print(tuple[0])



# This pattern is used everywhere:

# Printing API response data

# Displaying database records

# Debugging model parameters in AI/ML

# Showing key–value results in configuration files




# Nested Dictinaory dive dives 

dataset = {
    "image1": {"height": 256, "width": 256, "label": "cat"},
    "image2": {"height": 128, "width": 128, "label": "dog"}
}

print(dataset)
print("Image 1 :" , dataset["image1"]["label"])


model = {
    "layers": {
        "layer1": {"units": 256, "activation": "relu"},
        "layer2": {"units": 128, "activation": "relu"},
    }
}


copy_nested_dict = model.copy()
import copy
deep_dict = copy.deepcopy(dataset)
print(deep_dict)
print(copy_nested_dict["layers"]["layer1"]["activation"])


metrics = {}

for epoch in range(1, 6):
    loss = 0.01 * epoch
    accuracy = 0.80 + 0.02 * epoch

    metrics[epoch] = {
        "loss": round(loss, 3),
        "accuracy": round(accuracy, 3)
    }

print(metrics)


# 🟢 PART 1 — BASIC (1–10)

# Create a dictionary for a student with name, age, and marks. Print all keys and all values.


students = {
    "name" : "vishal",
    "age" : 23,
    "marks" : 80.34
}

print(students)

for key , value in students.items():
    print(f"{key} : {value}")

# Access a value using a key. Handle missing key using .get().


id = students.get("id" , "id number is not found ")
print(id)




# Add a new key "city" and update "age" in an existing dictionary.

city = " varansi"
students["city"] = city
students["age"] = 25
print(students)

# Delete a key "marks" from a dictionary.

del students["marks"]
print(students)

# students.pop("age")
# print(students)



# Loop through dictionary keys and print them one by one.(key)

for key in students.keys():
    print(key)

# Loop through key–value pairs and print them in key : value format.

for key , value in students.items():
    print(f"{key} : {value}")

# Check if a key "price" exists in a dictionary.

if "peice" in students.keys():
    print( "Exist");
else:
    print("Not Exist.")



# Create an empty dictionary and add keys dynamically using assignment.

empty_dicts = dict()

empty_dicts["name"] = "vishal"
print(empty_dicts)

# Count number of keys in a dictionary.

print(len(empty_dicts))



# Convert two lists into a dictionary:
keys = ["name","age"]
values = ["Vishal", 21]
print(dict(zip(keys , values)))


# 🟡 PART 2 — INTERMEDIATE (11–20)

# Use dictionary comprehension to create {1:1, 2:4, 3:9 … 10:100}.

result = {i: i*i for i in range(1,11)}

print(result)



# Create a dictionary of even numbers {2:4, 4:16, 6:36} using comprehension.

evne_Number = { num : num * num for num in range (2 , 10) if num % 2 ==0}
print(evne_Number)

# Merge two dictionaries using update().
dict1 = {"name": "Vishal", "age": 21}
dict2 = {"city": "Delhi", "skills": ["Python", "ML"]}

dict1.update(dict2)

print(dict1)


# Copy a dictionary using copy() and update the copied one.

newDict = dict1.copy()
print(newDict)

# Create a dictionary with default value "Not Found" using fromkeys().

keys = [ "name " , " age ", "marks "]
result = dict.fromkeys(keys , "values are not assiign")
print( result)

# Reverse keys and values of a dictionary.

data = {"name": "Vishal", "age": 21, "city": "Delhi"}

reversed_dict = {value: key for key, value in data.items()}

print(reversed_dict)




# Create a dictionary from a sentence counting each word.
sentence = "python is easy and python is powerFull"
words = sentence.split(" ")
print( words)

word_count = {}

for w in words:
    word_count[w] = word_count.get(w , 0) + 1
print(word_count)



# Safely remove a key using pop() without crashing.

data = {"name": "Vishal", "age": 21}

# Safely remove "city" key without crashing
removed_value = data.pop("city", "Key Not Found")

print("Removed Value:", removed_value)
print("Updated Dictionary:", data)




# 🔵 PART 3 — ADVANCED (21–30)

# Create a nested dictionary representing a laptop specification.


mackbook = {
    "M1":{
        "Storage":{
            "ram":"8gb",
            "ssd":256
            },
        "color": "gray-silicon",
        "body": "metal"
    },
    "M2":{
        "Storage":{
            "ram" : "16gb",
            "ssd" : "512gb"
        },
         "color": "gray-silicon",
        "body": "metal"
    }
}

print(mackbook)



# Example: processor, RAM, storage → values also dictionaries.

# Access and modify inner dictionary values in a nested dictionary.
mackbook["M2"]["Storage"]["ram"]= "64gb"
print(mackbook)

# Deep copy a nested dictionary and prove that changes in deep copy do not affect original.

import copy
deep_mackbook = copy.deepcopy(mackbook)
print("This is the deeep copy ::",deep_mackbook)

# Flatten a nested dictionary into a single dictionary.
nested_dict = {
    "epoch1": {"loss": 0.42, "acc": 0.81},
    "epoch2": {"loss": 0.35, "acc": 0.85}
}

flat = {}

for outer_key , innerDict in nested_dict.items():
    for inner_key , value in innerDict.items():
             flat[f"{outer_key}_{inner_key}"] = value;

print(flat)


#  anthpre way using the comprehension 

flat_dict = {f"{out_key}_{inn_key}" : val
             for out_key , innDict in nested_dict.items()
             for inn_key , val in innDict.items()
             };
print("flat using the comprehension :",flat_dict)
 
# Convert a dictionary into a list of tuples.

list_tuple = list(flat_dict.items())
print(list_tuple)

# Convert a list of tuples back into a dictionary.
# Convert list of tuples to dictionary
my_dict = dict(list_tuple)

print(my_dict)


# Sort a dictionary by keys.

# Sort a dictionary by values.

# Create a dictionary where keys are numbers 1–5 and values are lists.

# Write a program to compute union of two dictionaries.
# (If same key exists → add values)




# Extract only keys of a dictionary into a list.

data = {"name": "Vishal", "age": 21, "city": "Delhi"}

keys_list = list(data.keys())

print(keys_list)



# 🔴 PART 4 — AI/ML BASED (31–40)

# (Real project-style questions)

# Create a dictionary storing hyperparameters:

# learning_rate, batch_size, epochs, optimizer.

# Update the hyperparameters dictionary to change learning_rate dynamically.

# Store training metrics for 5 epochs inside a nested dictionary.
# Example: {1: {"loss": 0.42, "acc": 0.81}, ...}

# Iterate over each epoch and print formatted output:
# "Epoch 1 → Loss: 0.42, Accuracy: 0.81"

# Create a dictionary mapping labels to indices:
# {"cat":0, "dog":1, "horse":2}

# Reverse the above mapping to:
# {0:"cat", 1:"dog", 2:"horse"}

# Count frequency of each class given a list of labels:
# ["cat","dog","cat","dog","cat"]

# Represent a simple neural layer dictionary:
# {"units":128,"activation":"relu","trainable":True}

# Create a dataset dictionary where each entry stores image size and label.

# Given a dataset dict, print only those images where label == "cat".