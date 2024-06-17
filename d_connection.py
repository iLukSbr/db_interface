import flet as ft
import pymysql as my
import psycopg2 as pg

def con_db(usr_credentials, page):
    from d_messages import display_action
    from d_table import draw_table_view
    connect_functions = {
        "MySQL": my.connect,
        "PostgreSQL": pg.connect
    }
    connect = connect_functions.get(usr_credentials["database"])
    try:
        if usr_credentials["database"] == "PostgreSQL":
            con = connect(
                host=usr_credentials["host"],
                port=int(usr_credentials["port"]),
                user=usr_credentials["user"],
                password=usr_credentials["password"],
                database=usr_credentials["pg_database"]
            )
        else:
            con = connect(
                host=usr_credentials["host"],
                port=int(usr_credentials["port"]),
                user=usr_credentials["user"],
                password=usr_credentials["password"]
            )
        display_action("Conexão realizada com sucesso.", page)
        draw_table_view(page, con, usr_credentials)
    except Exception as e:
        display_action(e, page)
