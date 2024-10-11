""" The values and tolerances of older resistors are identified by four colored
bands: the first two indicate the first two significant figures of the resistance in ohms,
the third denotes a decimal multiplier (number of zeros) and the fourth indicates the
tolerance. The colors and their meanings for each band are listed in Table 4.3.
For example, a resistor with colored bands violet, yellow, red, green has value 
74x10^2 = 7400 Ohm and tolerance +-0.5%.
Write a program that defines a function to translate a list of four color abbreviations
into a resistance value and a tolerance. For example,
In [x]: print(get_resistor_value(['vi', 'yl', 'rd', 'gr']))
Out[x]: (7400, 0.5)
"""

def get_resistor_value(list_lines:list):
    """ Return tuple with resistance value and tolerance given a list of 4 color abbreviations
    """
    # Let's define dictionaries using Table 4.3 with the abbreviation as keys
    # I could make separate dicts for SignificantFigures, Multiplier and Tolerance
    # Or a single dict with tuples (SF,Mult,Tol)
    color_code = {'bk':(0,1,0), 'br':(1,10,1), 'rd':(2,1E2,2), 'or':(3,1E3,0),
                  'yl':(4,1E4,5), 'gr':(5,1E5,0.5), 'bl':(6,1E6,0.25), 'vi':(7,1E7,0.1),
                  'gy':(8,1E8,0.05), 'wh':(9,1E9,0), 'au':(0,0,5), 'ag':(0,0,10)}

    # Make sure that you get a list of 4 values as input
    assert type(list_lines) in (list, tuple) and len(list_lines) == 4, "You must provide a List/Tuple with 4 elements."
    try:
        for color in list_lines:
            color_code[color]
    except KeyError:
        return f"Handled error: Undefined color {color}."
    return (int(f'{color_code[list_lines[0]][0]}{color_code[list_lines[1]][0]}')*color_code[list_lines[2]][1], color_code[list_lines[3]][2])

print(get_resistor_value(['bk', 'bk', 'bk', 'bk']))  # test by just defining bk, should be (0,0)

# Test several scenarios
# print(get_resistor_value(['vi', 'yl', 'rd', 'gr', 'a']))  # Assert error: too many arguments
print(get_resistor_value(['v', 'yl', 'rd', 'gr']))  # error: undefined key
print(get_resistor_value(('vi', 'yl', 'rd', 'gr')))  # it should work with tuples
print(get_resistor_value(['vi', 'yl', 'rd', 'gr']))  # it should work with lists