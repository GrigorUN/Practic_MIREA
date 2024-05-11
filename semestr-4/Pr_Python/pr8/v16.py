def main(data):
    mask_o1 = 0b11111
    mask_o2 = 0b111
    mask_o3 = 0b111111
    mask_o5 = 0b11111

    o1 = data & mask_o1
    o2 = (data >> 5) & mask_o2
    o3 = (data >> 8) & mask_o3
    o5 = (data >> 22) & mask_o5

    result = hex((o3 << 21) | (o1 << 8) | (o5 << 3) | o2)

    return result


# Тесты
print(main(131301466))  # '0x1afa'
print(main(104496836))  # '0x7c004c6'
print(main(67830905))  # '0x801983'
print(main(77783491))  # '0x4200396'
