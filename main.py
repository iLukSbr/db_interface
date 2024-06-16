# Bibliotecas
import flet as ft
import platform

# Conectar ao gerenciador de bancos de dados
# Página inicial
def main(page: ft.Page):
    # Limpar cache
    #page.client_storage.clear()

    from d_credentials import get_credentials

    if(platform.system() == "Windows"):
        page.platform = ft.PagePlatform.WINDOWS
    elif(platform.system() == "Linux"):
        page.platform = ft.PagePlatform.LINUX
    elif(platform.system() == "Darwin"):
        page.platform = ft.PagePlatform.MACOS

    # Ação do botão Conectar
    def on_con_button_click(e):
        from d_credentials import save_credentials
        from d_connection import con_db
        from d_messages import display_action

        if not user_field.value or not password_field.value or not db_type_field.value:
            display_action("Os campos usuário, senha e banco de dados devem estar preenchidos.", page)
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
            if save_check.value:
                save_credentials(page, usr_credentials)
            else:
                save_credentials(page, None)
            con_db(usr_credentials, page)
        
    page.title = "Interface de Bancos de Dados"
    page.window_height = 720
    page.window_width = 1280
    page.theme_mode = 'LIGHT'

    last_credentials = get_credentials(page)

    if not last_credentials:
        last_credentials = {
            "host": "",
            "port": "",
            "user": "",
            "password": "",
            "database": ""
        }

    # Campos de login
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

    home = ft.View("/", [
        host_field,
        port_field,
        user_field,
        password_field,
        save_check,
        db_type_field,
        con_button
    ])
    page.views.append(home)
    page.go("/")

ft.app(target=main)