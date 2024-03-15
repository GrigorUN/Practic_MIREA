def main(data):
    z2 = (data >> 9) & 0xFF
    z3 = (data >> 17) & 0x3F
    z4 = data >> 23
    result = {
        'Z2': hex(z2),
        'Z3': hex(z3),
        'Z4': hex(z4)
    }
    return result

# Примеры тестов
print(main(1686864812))  # {'Z2': '0xc1', 'Z3': '0x5', 'Z4': '0xc9'}
print(main(3118518009))  # {'Z2': '0x67', 'Z3': '0x30', 'Z4': '0x173'}
print(main(2122082591))  # {'Z2': '0x34', 'Z3': '0x3e', 'Z4': '0xfc'}
print(main(2896071282))  # {'Z2': '0x45', 'Z3': '0xf', 'Z4': '0x159'}
