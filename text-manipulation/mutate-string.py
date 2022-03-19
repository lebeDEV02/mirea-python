s = input("Введите строку s: ")
s = list(s)

# a
for i in range(len(s)):
    if s[i] == "a" and s[i+1] == "b" and s[i+2] == "c" and i+2 < len(s):
        s[i] = "d"
        s[i + 1] = "e"
        s[i + 2] = "f"

# b
if "w" in s:
    s.pop(s.index("w"))
    s.append(" ")

# c
lenOfString = len(s)
for i in range(lenOfString):
    if i < lenOfString:
        if s[i] == "t" and s[i + 1] == "h" and i < lenOfString:
            s.pop(i)
            s.pop(i)
            lenOfString -= 2

# d
if "x" in s:
    indexOfX = s.index("x")
    s[s.index("x")] = "k"
    s.insert(indexOfX+1, "s")

# e
for i in range(len(s)):
    if s[i] == "q":
        s.insert(i+1, "b")

# f
lenOfString = len(s)
for i in range(lenOfString):
    if i < lenOfString:
        if s[i] == "p" and s[i + 1] == "h" and i < lenOfString:
            s.pop(i)
            s.pop(i)
            s.insert(i, "f")
            lenOfString -= 1
        if s[i] == "e" and s[i + 1] == "d" and i < lenOfString:
            s.pop(i)
            s.pop(i)
            s.insert(i, "i")
            s.insert(i+1, "n")
            s.insert(i+2, "g")
            lenOfString += 1

s = ''.join(s)
print(s)