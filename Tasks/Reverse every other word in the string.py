##Reverse every other word in a given string, then return the string.
# Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word.
# Punctuation marks should be treated as if they are a part of the word in this kata.

def reverse_alternate(s):
    if s=="   ":
         print('""')
    else:
        s = s.split()
        s.insert(0, 'el')
        for i in range(len(s)):
            if i % 2 == 0:
                s[i] = s[i][::-1]
        s.pop(0)
        print(s)


if __name__ == '__main__':
    reverse_alternate("Did it work?")
    reverse_alternate("I really hope it works this time...")
    reverse_alternate("Reverse this string, please!")
    reverse_alternate("   ")
