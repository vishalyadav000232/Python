# ✅ Python Functions – Complete Important Concepts (Beyond Basics)

# 1. Function Annotations (Type Hints)

# python allow you to hint the type of the parameter

def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))


# 2. Docstrings

# add the descirption of the fn using triple qute """ """

# def greet(name: str):
#     """This function prints a greeting message."""
#     print(f"Hello {name}")

# help(greet)


# 3. Global & Nonlocal Variables


# globle


x = 10

def change():
    global x
    x += 5
change()
print(x)

# nonLcal

def outer():
    x = 5
    def inner():
        nonlocal x
        x += 5
        print(x)
    inner()
    print(x)
outer()  # 10
