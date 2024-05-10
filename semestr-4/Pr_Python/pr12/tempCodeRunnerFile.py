def parse_c(buf, offs):
    c1, offs = parse(buf, offs, "uint16")
    c2size, offs = parse(buf, offs, "uint32")
    c2offs, offs = parse(buf, offs, "uint16")
    c2 = []
    for _ in range(c2size):
        val, c2offs = parse_d(buf, c2offs)
        c2.append(val)
    c3, offs = parse(buf, offs, "int16")
    c4offs, offs = parse(buf, offs, "uint16")
    c4, c4offs = parse_e(buf, c4offs)
    c5offs, offs = parse(buf, offs, "uint16")
    c5, c5offs = parse_f(buf, c5offs)
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5), offs