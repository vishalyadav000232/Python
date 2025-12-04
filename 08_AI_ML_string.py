

# ADVANCED STIRNG CONCEPT FOR AI ML

# Strimg Encodding and Decoding (text -> Number -> text)

# AI models only understand numbers, not text.
# So, converting strings into numerical form is the first step in NLP or text-based ML.

text = "AI is powerful 💡"
encoded = text.encode('utf-8')   # Convert to bytes
decoded = encoded.decode('utf-8') # Convert back to string

print(encoded)
print(decoded)



text = "ABC"
nums = [ord(c) for c in text]  # Encode each char to Unicode number
print("Encoded numbers:", nums)

decoded = ''.join([chr(n) for n in nums])  # Decode numbers back to text
print("Decoded text:", decoded)


#  Why String matter in ai ml 

# NlP --> Tokenization , Cleaning , Processing Text 

# DataSet Cleanig --> Removing Symvole ans lowercase_conversion 

# Sentiment analysis --> Detecting emotion from your Text .

# Spech to Text Processing --> Output is string  

# Log Analyis in server --> Error store in the string 



# Removing the special Character (Data Cleaning ...)

import re
text = "Ai is the Feature !!!  # 2035"
cleaned = re.sub(r'[^a-zA-Z0-9]' , " " , text)
print(cleaned)


# zFill(Width) pad start with zero at the start 

text = "35"
zfill  =  text.zfill(5) #--> 5 means lenth of the total string 
print(zfill)


name = "vishal"
encode = name.encode("utf-8")
decoded = encode.decode()
print(name , encode)
print(decoded)


# remove the suffix and prefix 

print("unhappy".removeprefix("un"))
print("image.png".removesuffix(".png"))


# partitions()-- split text into three part bfore  , matched , after

print( "Ai is powerFull ".partition("is"))