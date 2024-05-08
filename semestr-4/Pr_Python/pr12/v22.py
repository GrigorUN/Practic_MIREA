from struct import *


FMT = dict(
    char="c",
    int8="b",
    uint8="B",
    int16="h",
    uint16="H",
    int32="i",
    uint32="I",
    int64="q",
    uint64="Q",
    float="f",
    double="d",
)


def parse(buf, offs, ty, order="<"):
    pattern = FMT[ty]
    size = calcsize(pattern)
    value = unpack_from(order + pattern, buf, offs)[0]
    return value, offs + size


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, "double")
    d2, offs = parse(buf, offs, "float")
    d3, offs = parse(buf, offs, "uint8")
    return dict(D1=d1, D2=d2, D3=d3), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, "int32")
    c2size, offs = parse(buf, offs, "uint32")
    c2offs, offs = parse(buf, offs, "uint16")
    c2 = []
    for _ in range(c2size):
        val, c2offs = parse(buf, c2offs, 'int32')
        c2.append(val)
    return dict(C1=c1, C2=c2), offs


def parse_b(buf, offs):
    b1, offs = parse(buf, offs, "uint8")
    b2, offs = parse(buf, offs, "int16")
    b3, offs = parse(buf, offs, "int32")
    b4 = []
    for _ in range(2):
        val, offs = parse_c(buf, offs)
        b4.append(val)
    b5 = []
    for _ in range(5):
        val, offs = parse(buf, offs, "uint8")
        b5.append(val)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5), offs


def parse_a(buf, offs):
    a1, offs = parse(buf, offs, "int32")
    a2offs, offs = parse(buf, offs, "uint32")
    a2, a2offs = parse_b(buf, a2offs)
    a3size, offs = parse(buf, offs, "uint32")
    a3offs, offs = parse(buf, offs, "uint16")
    a3 = []
    for _ in range(a3size):
        val, a3offs = parse(buf, a3offs, "int16")
        a3.append(val)
    a4, offs = parse(buf, offs, "uint32")
    a5offs, offs = parse(buf, offs, "uint32")
    a5, a5offs = parse_d(buf, a5offs)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5), offs


def main(stream):
    res, _ = parse_a(stream, 4)
    return res


print(
    main(
        b"UPMZ\x03\xc6F\x1b2\x00\x00\x00\x02\x00\x00\x00R\x00I\x9c\xb1\x93V\x00"
        b"\x00\x00\xcfM\x1f\x940i\x83\xfa\xe5;\x85\rQ>\xe7\x8c}\xce\x93\xf0\xf4\xaf"
        b"I\x029\x7f\xe2S\xd5\xcb\x90\xa1`\r\xa7\x03\x00\x00\x00\x1a\x00\xba"
        b';\x99\xe6\x03\x00\x00\x00&\x00}\xbd\xb9\x9c\xdbw("\x97\xe4\xbet\x91\x9e\xf4'
        b"\xe7\xbf\xf1\xb6\x84>\xa0"
    )
)
