import jwt

# This function that will contain the algoritm to pretect the passwords
passphrases = ['kosasd', 'axiw', 'sdcus', 'hwshxw', 'sdcnwsi']

def offuscator(password: str) -> str:
    if type(password) is not str:
        raise TypeError()
    factor = round(len(password) / 5)

    final_string = ''
    start = 0
    next = factor
    index = 0

    for i in range(0, (len(password) % 5) + 1):
        for i in range(0, 5):
            index += 1

            if index > len(password):
                break

            final_string += jwt.encode({'pass': password[start:next]}, passphrases[i]) + '|'

            start += factor
            next += factor
    
    return final_string

# This function will contain the reverse algoritm
def deoffuscator(password: str) -> str:
    if type(password) is not str:
        raise TypeError()
    peaces = password.rsplit('|')

    loops = 1
    rest = len(peaces) % 5

    while rest > 0:
        loops += 1
        
        if rest < 5:
            break

        rest = rest % 5

    index = 0

    for i in range(0, loops):
        for i in range(0, 5):
            if index == (len(peaces) -1):
                break

            peaces[index] = jwt.decode(peaces[index], passphrases[i], algorithms=["HS256"])['pass']
            index += 1

    return ''.join(peaces)
