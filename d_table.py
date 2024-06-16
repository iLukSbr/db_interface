import flet as ft
import pymysql as my
import psycopg2 as pg

from d_messages import *
from d_menu import *

# Lista dos bancos de dados disponíveis
def draw_table_view(page, usr_credentials, con):
    menubar = menu_bar(page, con)

    # Gerar seletor de tabela
    def gen_tables_list(db_name, val):
        try:
            cursor = con.cursor()
            if usr_credentials["database"] == "MySQL":
                cursor.execute(f"USE {db_name};SHOW TABLES;")
            elif usr_credentials["database"] == "PostgreSQL":
                cursor.execute(f"SELECT tablename FROM pg_catalog.pg_tables where schemaname='{db_name}' ORDER By tablename ASC;")
            tables = cursor.fetchall()
            if usr_credentials["database"] == "PostgreSQL":
                cursor.execute(f"SET search_path TO {db_name};")
        except Exception as e:
            display_action(e, page)
        table_field = ft.Dropdown(
            label="Tabela",
            on_change=lambda e: table_selected(e, db_name),
            value=val
        )
        for table in tables:
            table_field.options.append(ft.dropdown.Option(table[0]))
        return table_field

    # Um banco de dados foi escolhido
    def db_selected(e):
        db_name = e.control.value
        table_selector = gen_tables_list(db_name, None)
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

    # Gerar seletor de banco de dados
    def gen_db_list(val):
        try:
            cursor = con.cursor()
            if usr_credentials["database"] == "MySQL":
                cursor.execute("SHOW DATABASES;")
            elif usr_credentials["database"] == "PostgreSQL":
                cursor.execute("SELECT schema_name FROM information_schema.schemata ORDER BY schema_name ASC;")
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
    
    # Uma tabela foi escolhida
    def table_selected(e, db_name):
        display_action(f"Carregando a tabela {e.control.value}", page)
        try:
            cursor = con.cursor()
            cursor.execute(f"SELECT * FROM {e.control.value};")
            table = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
        except Exception as e:
            display_action(e, page)
        table_display = ft.DataTable(
            columns=[ft.DataColumn(ft.Text(name)) for name in column_names],
            rows=[ft.DataRow(cells=[ft.DataCell(ft.Text(str(value))) for value in row]) for row in table]
        )
        table_selector = gen_tables_list(db_name, e.control.value)
        db_selector = gen_db_list(db_name)
        if db_name:
            table_view = ft.View(
                "/table",[
                    menubar,
                    db_selector,
                    table_selector,
                    table_display
                ]
            )
            page.views.pop()
            page.views.append(table_view)
            page.update()
            page.go(table_view.route)

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
