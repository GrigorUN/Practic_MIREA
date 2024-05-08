def remove_empty_rows_and_columns(table):
    filtered_table = filter(
        len, map(lambda row: list(filter(bool, row)), table)
    )

    unique_rows = []
    unique_rows_set = set()
    for row in filtered_table:
        row_tuple = tuple(row)
        if row_tuple not in unique_rows_set:
            unique_rows.append(row)
            unique_rows_set.add(row_tuple)

    transposed_table = zip(*unique_rows)

    unique_columns = []
    unique_columns_set = set()
    for column in transposed_table:
        column_tuple = tuple(column)
        if column_tuple not in unique_columns_set:
            unique_columns.append(column)
            unique_columns_set.add(column_tuple)

    return list(zip(*unique_columns))


def replace_boolean_values(value):
    if value == "да":
        return "Выполнено"
    elif value == "нет":
        return "выполнено Не"
    else:
        return value


def replace_special_characters(value):
    return value.replace("[at]", "@").replace("-", ".")


def reverse_name_and_surname(value):
    if len(value.split()) > 1:
        name_parts = value.split()
        return name_parts[-1] + " " + " ".join(name_parts[:-1])
    else:
        return value


def replace_values_and_modify_names(table):
    replaced_table = []
    for row in table:
        replaced_row = [replace_boolean_values(item) for item in row]
        replaced_row = [
            replace_special_characters(item) for item in replaced_row
        ]
        replaced_row = [
            reverse_name_and_surname(item) for item in replaced_row
        ]
        replaced_table.append(replaced_row)

    return replaced_table


def main(table):
    cleaned_table = remove_empty_rows_and_columns(table)
    modified_table = replace_values_and_modify_names(cleaned_table)
    return modified_table


table = [
    [
        "rasebman63[at]yandex.ru",
        "Рашебман Глеб",
        "да",
        "",
        "rasebman63[at]yandex.ru",
        "01-01-07",
    ],
    [
        "valerij45[at]rambler.ru",
        "Сетев Валерий",
        "да",
        "",
        "valerij45[at]rambler.ru",
        "03-11-28",
    ],
    [
        "rostislav97[at]gmail.com",
        "Берирян Ростислав",
        "нет",
        "",
        "rostislav97[at]gmail.com",
        "01-07-04",
    ],
    [
        "rasebman63[at]yandex.ru",
        "Рашебман Глеб",
        "да",
        "",
        "rasebman63[at]yandex.ru",
        "01-01-07",
    ],
    [
        "vladislav28[at]yahoo.com",
        "Тачучин Владислав",
        "нет",
        "",
        "vladislav28[at]yahoo.com",
        "04-09-10",
    ],
]

print(main(table))
