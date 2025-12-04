user_name = "  vIsHaL yaDaV  "
email = "  vishal@example.com "

# Clean + Normalize
clean_name = user_name.strip().title()        # "Vishal Yadav"
clean_email = email.strip().lower()           # "vishal@example.com"

# Generate formatted message
message = f"""
Dear {clean_name},

Your account has been created successfully.
We’ve sent a confirmation email to {clean_email}.

Thank you,
The Python Team 🐍
"""

print(message)


# Replace a with @ in banana
str = "banana"
newStr = str.replace("a", "@")
print(newStr , str )


# Count how many time "a" appears in the "anrakbsadakaa"


str = "anrakbsadakaaaaaaaa"
count = 0
for val in str:
    if( val.lower() == "a"):
        count += 1

print(count)


