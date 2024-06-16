import pymysql as my
import psycopg2 as pg
import flet as ft

import credentials

def on_con_button_click(event):
    # Check if any of the fields are empty
    if not user_field.value or not password_field.value or not db_field.value:
        # Display an error dialog
        ft.Dialog(
            title="Erro",
            text="Por favor, preencha todos os campos.",
            buttons=[ft.dialog.CloseButton("Fechar")]
        ).show()
    else:
        # Attempt to connect to the database
        pass  # replace with your connection code

def main(page: ft.Page):
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

    check_field = ft.Checkbox(
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

    con_button = ft.ElevatedButton(text="Conectar")

    # Set the button click event handler
    #con_button.on_click(on_con_button_click)

    page.add(
        host_field,
        user_field,
        password_field,
        check_field,
        db_field,
        con_button
    )

ft.app(target=main)