temperatures = [10, -20, -289, 100]

def c_to_f(celsius):
    if celsius < -273.15:
        return "Input can't be lower than -273.15°C"
    else:
        return celsius * 9.0 / 5.0 + 32

for temp in temperatures:
    print(c_to_f(temp))
