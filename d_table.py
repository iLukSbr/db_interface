import flet as ft
import pymysql as my
import psycopg2 as pg

from d_messages import *
from d_menu import *

# Lista dos bancos de dados disponíveis
def draw_table_view(page, usr_credentials, con):
    def db_selected(e):
        db_name = e.control.value
        table_selector = gen_tables_list(db_name)
        db_selector = gen_db_list(db_name)
        if db_name:
            table_view = ft.View(
                "/table",[
                    menubar,
                    db_selector,
                    table_selector
                ]
            )
            page.views.pop()
            page.views.append(table_view)
            page.update()
            page.go(table_view.route)

    def gen_db_list(val):
        try:
            cursor = con.cursor()
            if usr_credentials["database"] == "MySQL":
                cursor.execute("SHOW DATABASES;")
            elif usr_credentials["database"] == "PostgreSQL":
                cursor.execute("SELECT schema_name FROM information_schema.schemata;")
            databases = cursor.fetchall()
        except Exception as e:
            display_action(e, page)
        db_field = ft.Dropdown(
            label="Banco de dados",
            on_change=db_selected,
            value=val
        )
        for database in databases:
            db_field.options.append(ft.dropdown.Option(database[0]))
        return db_field
    
    def table_selected(e):
        pass

    def gen_tables_list(db_name):
        try:
            cursor = con.cursor()
            if usr_credentials["database"] == "MySQL":
                cursor.execute(f"USE {db_name};")
                cursor.execute("SHOW TABLES;")
            elif usr_credentials["database"] == "PostgreSQL":
                cursor.execute(f"SET search_path TO {db_name};")
                cursor.execute("SELECT table_name FROM information_schema.tables;")
            tables = cursor.fetchall()
        except Exception as e:
            display_action(e, page)
        table_field = ft.Dropdown(
            label="Tabela",
            on_change=table_selected
        )
        for table in tables:
            table_field.options.append(ft.dropdown.Option(table[0]))
        return table_field

    menubar = menu_bar(page, con)
    db_selector = gen_db_list(None)
    db_view = ft.View(
        "/table",[
            menubar,
            db_selector
        ]
    )
    page.views.append(db_view)
    page.update()
    page.go(db_view.route)

def table_changed(e):
    pass
    # display_action(f"Carregando a tabela {table_field.value}", page)
    # cursor = con.cursor()
    # cursor.execute(f"SELECT * FROM {table_field.value};")
    # table = cursor.fetchall()
    # table_display = ft.DataTable(
    #     columns=[
    #         ft.DataColumn(ft.Text("Coluna")),
    #         ft.DataColumn(ft.Text("Valor")),
    #     ],
    #     rows=[
    #         ft.DataRow(
    #             cells=[
    #                 ft.DataCell(ft.Text(column[0])),
    #                 ft.DataCell(ft.Text(str(column[1]))),
    #             ]
    #         )
    #         for column in table
    #     ]
    # )
    # page.add(table_display)