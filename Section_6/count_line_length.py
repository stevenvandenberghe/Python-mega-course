with open("fruits.txt", "r") as file:
    for line in file.readlines():
        print(len(line.strip()))
