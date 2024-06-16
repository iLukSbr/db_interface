import pymysql as my
import psycopg2 as pg
import flet as ft

import credentials

def main(page: ft.Page):
    def on_con_button_click(e):
        if not user_field.value or not password_field.value or not db_field.value:
            dlg = ft.AlertDialog(
                title=ft.Text(
                    "Preencha todos os campos.",
                    text_align="CENTER"
                ),

            )
            page.dialog = dlg
            dlg.open = True
            page.update()
        else:
            if save_check.value: # Save credentials
                credentials.save_credentials(page, {
                    "host": host_field.value,
                    "user": user_field.value,
                    "password": password_field.value,
                    "database": db_field.value
                })
            #con_db(credentials)
            pass
    
    page.title = "Database Interface"
    page.window_height = 720
    page.window_width = 1280
    page.theme_mode = 'LIGHT'

    last_credentials = credentials.get_credentials(page)

    # Create text fields for the database credentials
    host_field = ft.TextField(
        label="Host",
        value=last_credentials["host"]
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
        value=False
    )

    db_field = ft.Dropdown(
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
        user_field,
        password_field,
        save_check,
        db_field,
        con_button
    )

ft.app(target=main)