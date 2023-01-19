t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

# здесь продолжайте программу
def param(chars=" !?"):
    def real_decorator(funk):
        def wrapper(s):
            new_s=funk(s)
            for i in new_s:
                if i in chars:
                    new_s=new_s.replace(i,'-')
            while new_s.count('--')!=0:
                new_s=new_s.replace('--','-')
            return new_s
        return wrapper
    return real_decorator


def main_funk(s):
    s=''.join([t[i] if i in t else i for i in s])
    return s

s=input().lower()

if __name__ == '__main__':
    main_funk=param()(main_funk)
    print(main_funk(s))