#!/usr/bin/env python

"""Print out some unicode chars to a text file
"""

def print_range(base, count, length=60):
    out = ''
    for ii in range(base, base + count):
        out += chr(ii) + ' '
        if len(out) > length:
            print(out.strip())
            out = ''
    if out:
        print(out.strip())
    print('')

def print_smileys():
    """Print unicode smileys as defined here https://www.unicode.org/emoji/charts/full-emoji-list.html"""
    base = 0x1f600
    print('smileys')
    print_range(base, 80)

def print_math():
    """Math symbols from here
    https://en.wikipedia.org/wiki/Mathematical_operators_and_symbols_in_Unicode"""
    base = 8704
    print('math')
    print_range(base, 256)

def print_chess():
    base = 0x2600
    print('chess')
    print_range(base, 300)

def print_misc():
    base = 0x1f300
    print('misc')
    print_range(base, 0x300)

def print_misc2():
    base = 9800
    print('misc')
    print_range(base, 100)


def print_greek():
    base = 0x370
    print('greek')
    print_range(base, 117)




if __name__ == '__main__':
    print_smileys()
    print_math()
    print_chess()
    print_misc()
    print_greek()
