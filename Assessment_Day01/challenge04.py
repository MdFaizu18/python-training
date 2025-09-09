# Challenge 4: Temperature Converter

def celcius_to_farhenhit(c):
    return c * 9/5 + 32

def farhenhit_to_celcius(f):
    return (f - 32) * 5/9

print("25°C =", celcius_to_farhenhit(25), "°F")
print("100°F =", round(farhenhit_to_celcius(100), 2), "°C")