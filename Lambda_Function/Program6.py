with open("sample.txt", "r") as file:
    print(file.tell())
    print(file.read(5))
    print(file.tell())
    file.seek(0)
    print(file.read())
