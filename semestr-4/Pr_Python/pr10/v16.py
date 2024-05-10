def remove_duplicate_columns(table):
    seen_columns = set()
    unique_columns = []
    for row in table:
        unique_row = []
        for col_idx, cell in enumerate(row):
            if cell is not None and cell not in seen_columns:
                seen_columns.add(cell)
                unique_row.append(cell)
        unique_columns.append(unique_row)
    return unique_columns


def remove_empty_columns(table):
    non_empty_columns = []
    for col_idx in range(len(table[0])):
        column = [row[col_idx] for row in table]
        if any(cell is not None for cell in column):
            non_empty_columns.append(column)
    return [list(col) for col in zip(*non_empty_columns)]


def transpose_table(table):
    transposed_table = list(zip(*table))
    transposed_table = [list(row) for row in transposed_table]
    return transposed_table


def main(table):
    table = remove_duplicate_columns(table)

    table = remove_empty_columns(table)

    for row in table:
        row[0] = row[0].replace("(", "").replace(")", "").replace(" ", "-")
        if row[1] is not None:
            row[1] = str(round(float(row[1]) * 100)) + "%"

        if row[2] is not None:
            parts = row[2].split("-")
            row[2] = f"{parts[2]}.{parts[1]}.{parts[0]}"

        if row[3] is not None:
            row[3] = row[3].split()[-1]

    table.sort(key=lambda x: x[3])

    table = transpose_table(table)

    return table


# Ваша таблица
table = [
    [
        "(533) 288-0615",
        "0.4532",
        None,
        None,
        "(533) 288-0615",
        "01-02-12",
        "Г.Т. Цомянц",
    ],
    [
        "(372) 487-9231",
        "0.4120",
        None,
        None,
        "(372) 487-9231",
        "04-02-23",
        "П.Ш. Кучемман",
    ],
    [
        "(412) 726-9282",
        "0.9534",
        None,
        None,
        "(412) 726-9282",
        "99-04-04",
        "К.М. Цафисяк",
    ],
    [
        "(021) 947-8931",
        "0.7172",
        None,
        None,
        "(021) 947-8931",
        "02-10-02",
        "Д.В. Лудко",
    ],
]

# Применяем преобразования
print(main(table))
