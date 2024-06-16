import pymysql as my
import psycopg2 as pg
import flet as ft

import credentials

def main(page: ft.Page):
    #page.client_storage.clear()

    def dialog(text):
        dlg = ft.AlertDialog(
            title=ft.Text(
                text,
                text_align="CENTER"
            )
        )
        page.dialog = dlg
        dlg.open = True
        page.update()

    def draw_select_db_page():
        for i in range(7):
            page.controls.pop()
        try:
            cursor = con.cursor()
            if usr_credentials["database"] == "MySQL":
                cursor.execute("SHOW DATABASES")
            elif usr_credentials["database"] == "PostgreSQL":
                cursor.execute("SELECT datname FROM pg_database")
            databases = cursor.fetchall()
            db_field = ft.Dropdown(label="Banco de dados")
            for database in databases:
                db_field.options.append(ft.dropdown.Option(database[0]))
            page.add(db_field)
            page.update()
        except Exception as e:
            dialog(e)
        

    def con_db(usr_credentials):
        global con
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
            dialog("Conexão realizada com sucesso.")
            draw_select_db_page()
        except Exception as e:
            dialog(e)

    def on_con_button_click(e):
        global usr_credentials
        if not user_field.value or not password_field.value or not db_type_field.value:
            dialog("Preencha todos os campos.")
        else:
            if not host_field.value or not port_field.value:
                host_field.value = "localhost"
                if db_type_field.value == "MySQL":
                    port_field.value = "3306"
                elif db_type_field.value == "PostgreSQL":
                    port_field.value = "5432"
                page.update()
            usr_credentials = {
                "host": host_field.value,
                "port": port_field.value,
                "user": user_field.value,
                "password": password_field.value,
                "database": db_type_field.value
            }
            if save_check.value: # Save credentials
                credentials.save_credentials(page, usr_credentials)
            else: # Clear saved credentials
                credentials.save_credentials(page, None)
            con_db(usr_credentials)
    
    page.title = "Interface de Bancos de Dados"
    page.window_height = 720
    page.window_width = 1280
    page.theme_mode = 'LIGHT'

    last_credentials = credentials.get_credentials(page)

    if not last_credentials:
        last_credentials = {
            "host": "",
            "port": "",
            "user": "",
            "password": "",
            "database": ""
        }

    # Create text fields for the database credentials
    host_field = ft.TextField(
        label="Host",
        value=last_credentials["host"]
    )

    port_field = ft.TextField(
        label="Porta",
        value=last_credentials["port"]
    )

    user_field = ft.TextField(
        label="Usuário",
        value=last_credentials["user"]
    )

    password_field = ft.TextField(
        label="Senha",
        password=True,
        can_reveal_password=True,
        value=last_credentials["password"]
    )

    save_check = ft.Checkbox(
        label="Salvar credenciais",
        value=True
    )

    db_type_field = ft.Dropdown(
        label="Banco de dados",
        options=[
            ft.dropdown.Option("MySQL"),
            ft.dropdown.Option("PostgreSQL")
        ],
        autofocus=True,
        value=last_credentials["database"]
    )

    con_button = ft.ElevatedButton(
        text="Conectar",
        on_click=on_con_button_click
    )

    page.add(
        host_field,
        port_field,
        user_field,
        password_field,
        save_check,
        db_type_field,
        con_button
    )

ft.app(target=main)