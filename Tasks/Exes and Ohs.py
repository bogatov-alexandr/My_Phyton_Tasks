def xo(s):
    return True if (s.lower().count('x')==s.lower().count('o')) or ('x' and 'o' not in s) else False

if __name__ == '__main__':
    print(xo('xxoo'))
    print(xo('xxo'))
    print(xo('xoo'))
    print(xo('qwerty'))
    print(xo('XXXOOO'))