def transform_table(input_table):
    unique_columns = []
    for row in input_table:
        unique_row = []
        for cell in row:
            if cell not in unique_row:
                unique_row.append(cell)
        unique_columns.append(unique_row)

    non_empty_columns = []
    for column_index in range(len(unique_columns[0])):
        column = [row[column_index] for row in unique_columns]
        if any(cell is not None for cell in column):
            non_empty_columns.append(column)

    unique_rows = []
    for row in non_empty_columns:
        if row not in unique_rows:
            unique_rows.append(row)

    transformed_table = []
    for row in unique_rows:
        transformed_row = []
        for cell in row:
            if cell == "да":
                transformed_row.append("Выполнено")
            elif cell == "нет":
                transformed_row.append("Не выполнено")
            elif "-" in cell:
                parts = cell.split("-")
                formatted_date = f"{parts[0]}.{parts[1]}.{parts[2]}"
                transformed_row.append(formatted_date)
            else:
                transformed_row.append(cell)
        transformed_table.append(transformed_row)

    return transformed_table
