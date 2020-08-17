def most_freq(str):
    b = set(str)
    d = {}
    for char in b:
        d[char] = str.count(char)
    sorted(d.values(),reverse=True)
    print(d)
    
str = input("Please enter a string")
most_freq(str)

