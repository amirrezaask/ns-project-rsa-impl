jadval = [
    '_', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2',
    '3', '4', '5', '6', '7', '8', '9', '.', '?', ',', '-'
]


class Helpers:
    @classmethod
    def text_to_int(cls, s: str):
        s = s.upper()
        number = str()
        for c in s:
            if c in jadval:
                temp = jadval.index(c)
                if temp < 10:
                    number = '{}0{}'.format(number, str(temp))
                else:
                    number = '{}{}'.format(number, str(temp))
            else:
                raise ValueError
        return int(number)

    @classmethod
    def int_to_text(cls, num_input):
        if len(str(num_input)) % 2 == 1:
            decrypted = "0" + str(num_input)
        else:
            decrypted = str(num_input)
        str_input = [decrypted[i:i + 2] for i in range(0, len(decrypted), 2)]
        out = str()
        for kir in str_input:
            out = out + jadval[int(kir)]

        return out
