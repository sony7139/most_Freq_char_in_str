str = input("Please enter a string")
b = set(str)
d = {}
for char in b:
    d[char] = str.count(char)
sorted(d.values(),reverse=True)
print(d)
    
