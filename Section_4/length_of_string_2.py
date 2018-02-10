def length_of_string(string):
    try:
        return len(string)
    except TypeError:
        return "Sorry integers don't have length."

print(length_of_string('Steven'))
print(length_of_string(10))