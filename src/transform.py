def transform_inventory(raw_json):
    result_sets = raw_json.get("ResultSets", [])
    if not result_sets:
        return []

    rows = result_sets[0].get("Rows", [])
    columns = result_sets[0].get("Columns", [])

    col_names = [col["Name"] for col in columns]

    clean_rows = []
    for row in rows:
        clean_rows.append(dict(zip(col_names, row)))

    return clean_rows
