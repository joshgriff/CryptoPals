# CryptoPals Challenge 2 - XOR

def b16_b2(b16):
    b16=b16.upper()
    b16_b2_map={
            '0':'0000',
            '1':'0001',
            '2':'0010',
            '3':'0011',
            '4':'0100',
            '5':'0101',
            '6':'0110',
            '7':'0111',
            '8':'1000',
            '9':'1001',
            'A':'1010',
            'B':'1011',
            'C':'1100',
            'D':'1101',
            'E':'1110',
            'F':'1111'}
    b2 = ''.join([b16_b2_map[h] for h in b16])
    return(b2)

def b2_b16(b2):
    b2_b16_map={
        '0000':'0',
        '0001':'1',
        '0010':'2',
        '0011':'3',
        '0100':'4',
        '0101':'5',
        '0110':'6',
        '0111':'7',
        '1000':'8',
        '1001':'9',
        '1010':'A',
        '1011':'B',
        '1100':'C',
        '1101':'D',
        '1110':'E',
        '1111':'F'
        }

    b16 = ''.join([b2_b16_map[b2[4*i:4*i+4]] for i in range(int(len(b2)/4))])
    return(b16)

def XOR(h1,h2):
    b2_1 = b16_b2(h1)
    b2_2 = b16_b2(h2)
    xor_1_2 = ''.join([str(int(d1)+int(d2)) for d1,d2 in zip(b2_1,b2_2)])
    xor_1_2 = xor_1_2.replace('2','0')
    return(b2_b16(xor_1_2))

if __name__ == '__main__':
    s1 = '1c0111001f010100061a024b53535009181c'
    s2 = '686974207468652062756c6c277320657965'
    r1 = '746865206b696420646f6e277420706c6179'.upper()
    xor_1_2 = XOR(s1,s2)
    print(xor_1_2 == r1)

#
