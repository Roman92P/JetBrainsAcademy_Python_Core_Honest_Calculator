name = ''
names = []
while True:
    name = input()
    if name.__eq__("."):
        break
    names.append(name)
print(names)
print(names.__len__())