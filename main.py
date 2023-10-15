import pandas as pd

sql_query = ""
columns = []
headers = []
headers_row = 0
table = ""


def sql_generate():
    global headers, columns, sql_query

    if len(columns) == 0:
        return

    sql_query = F"REPLACE INTO `{table}` "
    sql_query += "( "

    for i, header in enumerate(headers):
        sql_query += F"`{header}` "
        if i + 1 != len(headers):
            sql_query += ","

    sql_query += ") Values"
    sql_query += "\n"

    for i, columns in enumerate(columns):
        sql_query += "("
        for j, _ in enumerate(columns):
            sql_query += F"'{columns[j]}'"
            if j + 1 != len(columns):
                sql_query += ','
        sql_query += ")"
        if i + 1 == len(columns):
            sql_query += ";"
        else:
            sql_query += ","

        sql_query += "\n"

    return


def read_csv(path=""):
    global headers, headers_row, columns
    columns = pd.read_csv(path, header=headers_row)
    headers = columns.columns
    columns = columns.values.tolist()

    return


def write_sql(path=""):
    global sql_query
    f = open(path, "w+", encoding='utf-8')
    f.write(sql_query)

    return


if __name__ == '__main__':
    read_csv()
    sql_generate()
    write_sql()
