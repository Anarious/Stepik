code = 'Hawnj pk swhg xabkna ukq nqj.'


def ceasers_code(code, n):
    language = input('Please write EN or RU: ')
    code_type = input('Do you want to cipher or decipher: ')

    if language.lower() == 'ru' and code_type.lower() == 'decipher':
        res = ''
        for i in code:
            if not i.isalpha():
                res += i
                continue
            decipher = ord(i) + n

            if i.isupper():
                if decipher < 1040:
                    decipher += 32
                elif decipher > 1071:
                    decipher -= 32

            else:
                if decipher < 1072:
                    decipher += 32
                elif decipher > 1103:
                    decipher -= 32
            res += chr(decipher)
        return res

    if language.lower() == 'ru' and code_type.lower() == 'cipher':
        res = ''
        for i in code:
            if not i.isalpha():
                res += i
                continue
            cipher = ord(i) + n
            if i.isupper():
                if cipher > 1071:
                    cipher -= 32
                elif cipher < 1040:
                    cipher += 32

            else:
                if cipher > 1103:
                    cipher -= 32
                elif cipher < 1072:
                    cipher += 32
            res += chr(cipher)
        return res


    if language.lower() == 'en' and code_type.lower() == 'decipher':
        res = ''
        for i in code:
            if not i.isalpha():
                res += i
                continue
            decipher = ord(i) - n
            if i.isupper():
                if decipher < 65:
                    decipher += 26
                elif decipher > 90:
                    decipher -= 26
            else:
                if decipher < 97:
                    decipher += 26
                elif decipher > 122:
                    decipher -= 26
            res += chr(decipher)
        return res

    if language.lower() == 'en' and code_type.lower() == 'cipher':
        res = ''
        for i in code:
            if not i.isalpha():
                res += i
                continue

            cipher = ord(i) + n
            if i.isupper():
                if cipher > 90:
                    cipher -= 26
                elif cipher < 65:
                    cipher += 26
            else:
                if cipher > 122:
                    cipher -= 26
                elif cipher < 97:
                    cipher += 26
            res += chr(cipher)
        return res

for i in range(1, 26):
    n = i
    print(ceasers_code(code, n))
