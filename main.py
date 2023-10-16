import pandas as pd
import argparse

columns = []
headers = []
sql_query = ""
table = ""
s_path = ""
d_path = ""


def parse_flags():
    global table, s_path, d_path

    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--table", help="Table name")
    parser.add_argument("-s", "--source", help="Path of the source csv file")
    parser.add_argument("-d", "--destination", help="Path of the destination sql generated file")

    args = parser.parse_args()

    table = args.table
    s_path = args.source
    d_path = args.destination

    return


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


def read_csv(path="./a.csv"):
    global headers, headers_row, columns
    columns = pd.read_csv(path)
    headers = columns.columns
    columns = columns.values.tolist()

    return


def write_sql(path="./a.sql"):
    global sql_query
    f = open(path, "w+", encoding='utf-8')
    f.write(sql_query)

    return


if __name__ == '__main__':
    parse_flags()
    read_csv(path=s_path)
    sql_generate()
    write_sql(path=d_path)
