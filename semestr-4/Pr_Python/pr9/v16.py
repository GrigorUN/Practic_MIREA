import re


def main(input_str):
    matches = re.findall(
        r"\.do let\s*([^\s]*)\s*<==\s*{\s*(#?-?\d+\s*"
        r"(?:,\s*#?-?\d+\s*)*)}\s*\.end\.",
        input_str,
    )
    result = []
    for match in matches:
        key = match[0]
        values = [
            int(val.replace("#", "").strip()) for val in match[1].split(",")
        ]
        result.append((key, values))
    return result


# Примеры использования:

input_str_1 = ".do let direxe<== {#7736 , #-979 , #-98, #6905 } .end. .do let isaat_675 <== { #-9312 , #-7737,#-1633}.end. .do let quus_691 <== { #5986 ,#-9597, #6799, #1791} .end. .do let receor_181<== { #-7100,#-4373 } .end."
print(main(input_str_1))

input_str_2 = ".do let cera<== {#-4335,#-5497 , #-8290 ,#9794 } .end. .do let veinti <=={ #8414 , #3389, #6694} .end. .do let inerte <== { #-283,#-7181 , #-6368 , #-2526 } .end."
print(main(input_str_2))
