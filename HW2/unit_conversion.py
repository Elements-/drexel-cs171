# CS-171-A Prof Mark Boady
# Homework 2
# Cameron Kelliher
# 10/10/17

units = {
    'inches': .0254,
    'feet': .3048,
    'yards': .9144,
    'miles': 1609.34,
    'leagues': 4828.03,
    'centimeters': .01,
    'decimeters': .1,
    'meters': 1,
    'decameters': 10,
    'hectometers': 100,
    'kilometers': 1000
}

print('Welcome to the length conversion wizard')
print('This program can convert between any of the following lengths.')
print('\n'.join(units.keys()))
print('Note: You must use the units exactly as spelled above.\n')

value = float(input('Enter value:\n'))
from_units = input('Enter from units:\n')
to_units = input('Enter to units:\n')

base_value = units[from_units] * value
converted_value = (1 / units[to_units]) * base_value

print('%f %s is %f %s' % (value, from_units, converted_value, to_units))
