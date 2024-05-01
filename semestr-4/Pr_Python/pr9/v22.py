def main(input_string):
    input_string = input_string.strip()[1:-1]
    parts = input_string.split("\\begin opt")
    result = {}
    for part in parts:
        if part.strip():  # Пропускаем пустые части
            key_value_pair = part.split(":")
            key = key_value_pair[0].strip()
            value = (
                key_value_pair[1].split(";")[0].strip().strip("@'")
            )
            result[key] = value

    return result
