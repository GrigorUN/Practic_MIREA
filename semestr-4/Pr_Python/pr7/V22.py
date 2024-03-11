def main(x):
    if x[0] == "COBOL":
        return 10
    if x[0] == "RUST":
        if x[2] == "MAKO":
            return 6
        if x[2] == "IDL":
            if x[3] == 1988:
                return 7
            if x[3] == 1986:
                return 8
            if x[3] == 1958:
                return 9
    if x[0] == "XTEND":
        if x[2] == "MAKO":
            if x[1] == 1998:
                return 0
            if x[1] == 1967:
                return 1
            if x[1] == 2006:
                return 2
        if x[2] == "IDL":
            if x[3] == 1988:
                return 3
            if x[3] == 1986:
                return 4
            if x[3] == 1958:
                return 5


print(
    main(["RUST", 1998, "MAKO", 1986]),
    main(["XTEND", 1967, "MAKO", 1988]),
    main(["COBOL", 1998, "IDL", 1986]),
    main(["XTEND", 2006, "IDL", 1988]),
    main(["RUST", 1998, "IDL", 1958]),
)
