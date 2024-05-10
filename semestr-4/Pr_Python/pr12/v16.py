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


def parse_f(buf, offs):
    f1, offs = parse(buf, offs, "int16")
    f2, offs = parse(buf, offs, "uint8")
    f3, offs = parse(buf, offs, "uint32")
    f4, offs = parse(buf, offs, "uint32")
    f5, offs = parse(buf, offs, "double")
    return dict(F1=f1, F2=f2, F3=f3, F4=f4, F5=f5), offs


def parse_e(buf, offs):
    e1, offs = parse(buf, offs, "uint32")
    e2, offs = parse(buf, offs, "uint8")
    e3, offs = parse(buf, offs, "int64")
    e4, offs = parse(buf, offs, "int8")
    e5, offs = parse(buf, offs, "int64")
    e6 = []
    for _ in range(5):
        val, offs = parse(buf, offs, "float")
        e6.append(val)
    e7, offs = parse(buf, offs, "int8")
    e8 = []
    for _ in range(3):
        val, offs = parse(buf, offs, "float")
        e8.append(val)
    return dict(E1=e1, E2=e2, E3=e3, E4=e4, E5=e5, E6=e6, E7=e7, E8=e8), offs


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, "int8")
    d2, offs = parse(buf, offs, "int32")
    d3, offs = parse(buf, offs, "float")
    return dict(D1=d1, D2=d2, D3=d3), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, "uint16")
    c2size, offs = parse(buf, offs, "uint32")
    c2offs1, offs = parse(buf, offs, "uint16")
    c2offs, c2offs1 = parse(buf, c2offs1, "uint16")
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


def parse_b(buf, offs):
    b1, offs = parse_c(buf, offs)
    b2size, offs = parse(buf, offs, "uint16")
    b2offs, offs = parse(buf, offs, "uint32")
    b2 = []
    for _ in range(b2size):
        val, b2offs = parse(buf, b2offs, "double")
        b2.append(val)
    b3, offs = parse(buf, offs, "uint8")
    return dict(B1=b1, B2=b2, B3=b3), offs


def parse_a(buf, offs):
    a1, offs = parse(buf, offs, "int64")
    a2, offs = parse_b(buf, offs)
    return dict(A1=a1, A2=a2), offs


def main(stream):
    res, _ = parse_a(stream, 5)
    return res


print(
    main(
        b"\x9eNASB\xe8(\xe0\na}\xab\xea_m\x02\x00\x00\x004\x00\x97&8\x00o\x00\x02"
        b"\x00\x82\x00\x00\x00\x1b\x10[\x14\xb7\xa7xC\xcf\xbd\xd5\x874\x04\xb4"
        b'T\xa4,\xbc"\x00+\x00\x8b\x03\xe8\xb5i\xe8\xac3o\xd3\xe1\x8d \xa1\x0f;'
        b"\xbb\xc3_%\x9fc\xfd\xd7t\xbf\xd2\xffZ\xbf-d\xf6>\xf5\xbbs>\xa5H\xd8>\xb0'"
        b"}\x85\xbes\x04n?\xad\x0f\xf2>\xb5\x06\xc8\xa27\x0eD\xa6\xf7[\xe7\xd8h"
        b"L[\xf2\x07\xd2?<C&\n53\xd1?PE&\xbbhG\xc5?"
    )
)
# результат
# {'A1': -1536996992069130008,
#  'A2': {'B1': {'C1': 27999,
#                'C2': [{'D1': 16, 'D2': -1481173925, 'D3': -0.10120290517807007},
#                       {'D1': -43,
#                        'D2': -1274792825,
#                        'D3': -0.010537225753068924}],
#                'C3': 9879,
#                'C4': {'E1': 3051881355,
#                       'E2': 105,
#                       'E3': 2345779279149903080,
#                       'E4': -95,
#                       'E5': 7178497424287808271,
#                       'E6': [-0.9564207196235657,
#                              -0.8554660081863403,
#                              0.48123303055763245,
#                              0.23802168667316437,
#                              0.42242923378944397],
#                       'E7': -80,
#                       'E8': [-0.26072046160697937,
#                              0.9297553896903992,
#                              0.4727758467197418]},
#                'C5': {'F1': 1717,
#                       'F2': 200,
#                       'F3': 1141782434,
#                       'F4': 3881564070,
#                       'F5': 0.2817350284182232}},
#         'B2': [0.2687504386058668, 0.1662417329612631],
#         'B3': 27}}
