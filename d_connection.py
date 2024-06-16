import flet as ft
import pymysql as my
import psycopg2 as pg

from d_messages import *
from d_table import *

def con_db(usr_credentials, page):
    connect_functions = {
        "MySQL": my.connect,
        "PostgreSQL": pg.connect
    }
    connect = connect_functions.get(usr_credentials["database"])
    try:
        con = connect(
            host=usr_credentials["host"],
            port=int(usr_credentials["port"]),
            user=usr_credentials["user"],
            password=usr_credentials["password"]
        )
        display_action("Conexão realizada com sucesso.", page)
        draw_table_view(page, usr_credentials, con)
    except Exception as e:
        display_action(e, page)
