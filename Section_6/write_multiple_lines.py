numbers = [1, 2, 3]
with open("output.txt", "w") as file:
    for number in numbers:
        file.write(str(number) + "\n")