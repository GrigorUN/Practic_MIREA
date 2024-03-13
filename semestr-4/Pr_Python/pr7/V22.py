def evaluate_COBOL(x):
    if x[0] == "COBOL":
        return 10
    return None


def evaluate_RUST(x):
    if x[0] != "RUST":
        return None
    if x[2] == "MAKO":
        return 6
    if x[2] == "IDL":
        if x[3] == 1988:
            return 7
        elif x[3] == 1986:
            return 8
        elif x[3] == 1958:
            return 9
    return None


def evaluate_XTEND_MAKO(x):
    if x[2] != "MAKO":
        return None
    if x[1] == 1998:
        return 0
    elif x[1] == 1967:
        return 1
    elif x[1] == 2006:
        return 2
    return None


def evaluate_XTEND_IDL(x):
    if x[2] != "IDL":
        return None
    if x[3] == 1988:
        return 3
    elif x[3] == 1986:
        return 4
    elif x[3] == 1958:
        return 5
    return None


def evaluate_XTEND(x):
    if x[0] != "XTEND":
        return None
    result = evaluate_XTEND_MAKO(x)
    if result is not None:
        return result
    result = evaluate_XTEND_IDL(x)
    if result is not None:
        return result
    return None


def main(x):
    result = evaluate_COBOL(x)
    if result is not None:
        return result

    result = evaluate_RUST(x)
    if result is not None:
        return result

    result = evaluate_XTEND(x)
    if result is not None:
        return result


print(
    main(["RUST", 1998, "MAKO", 1986]),
    main(["XTEND", 1967, "MAKO", 1988]),
    main(["COBOL", 1998, "IDL", 1986]),
    main(["XTEND", 2006, "IDL", 1988]),
    main(["RUST", 1998, "IDL", 1958]),
)
