def main(x):
    if x[1] == "VCL":
        return process_vcl(x)
    elif x[1] == "XML":
        return process_xml(x)
    elif x[1] == "DIFF":
        return 12


def process_vcl(x):
    if x[2] == "HAXE":
        return process_haxe(x)
    elif x[2] == "NINJA":
        return 7
    elif x[2] == "MIRAH":
        return 8


def process_haxe(x):
    if x[4] == 1964:
        return process_1964(x)
    elif x[4] == 2009:
        return process_2009(x)
    elif x[4] == 2019:
        return 6


def process_1964(x):
    if x[0] == "J":
        return 0
    elif x[0] == "X10":
        return 1
    elif x[0] == "CLEAN":
        return 2


def process_2009(x):
    if x[0] == "J":
        return 3
    elif x[0] == "X10":
        return 4
    elif x[0] == "CLEAN":
        return 5


def process_xml(x):
    if x[4] == 1964:
        return 9
    elif x[4] == 2009:
        return 10
    elif x[4] == 2019:
        return 11


print(main(["J", "VCL", "HAXE", 1981, 1964]))
print(main(["X10", "DIFF", "HAXE", 2006, 2009]))
print(main(["CLEAN", "VCL", "NINJA", 2006, 2019]))
print(main(["CLEAN", "XML", "MIRAH", 2006, 2009]))
print(main(["X10", "VCL", "MIRAH", 2006, 1964]))
