# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/23 09:32


if __name__ == '__main__':
    key = input()
    content = input()

    # key = "TRAILBLAZERS".lower()
    # content = "Attack AT DAWN".lower()

    # remove duplicate word of keys
    key_rd = ""
    for ch in key:
        if ch not in key_rd:
            key_rd += ch

    # create a new alphabet
    start = 'a'
    alphabet = ""
    for i in range(26):
        ch = chr(ord(start) + i)
        alphabet += ch
        if ch not in key_rd:
            key_rd += ch

    # encrypt
    encrypt = list(content)
    for i in range(len(content)):
        ch = content[i]
        if ch == ' ':
            continue
        enc_ch = key_rd[alphabet.index(ch)]
        encrypt[i] = enc_ch
    print(''.join(encrypt))



