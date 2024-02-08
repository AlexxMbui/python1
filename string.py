text = "hello"
text1 = "THERE"
print(text)

# Accessing an element in a string
print(text[1])
print(text[2])
print(text[0])

# Modifying a string
print(text.upper())
print(text1.lower())

# Size/length of a string
print(len(text))

# String Concatenation--Combining strings
print(text + " " + text1)

# 1.Reassigning a string
initial = "Hello 0 world"
result =""
index = 6

for i in range(len(initial)):
    if i !=index:
        result+=initial[i]

print(result)

# 2.Deleting  a string
print(initial)
print(result)


