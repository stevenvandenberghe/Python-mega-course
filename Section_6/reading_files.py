with open("fruits.txt", "r") as file:
    content = file.read()
    file.close()
    print(content)