def most_freq(str):
    b = set(str)
    d = {}
    for char in b:
        d[char] = str.count(char)
    for i in sorted(d,key=d.get,reverse=True):
        print(i,end="")
        print("=",end="")
        print(d[i])
    
str = input("Please enter a string")
most_freq(str)

