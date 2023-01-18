
def param(a=10):
    def real_decar(funk):
        def wrapper(s):
            for i in range(len(s)):
                s[i]*=a
            return funk(s)
        return wrapper
    return real_decar

def main_f(a):
    return a

if __name__ == '__main__':
    main_f=param(10)(main_f)
    print(main_f([1,2,3]))