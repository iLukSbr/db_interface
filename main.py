import pymysql as my
import psycopg2 as pg
import flet as ft
import platform

import credentials

global page
global usr_credentials

# Mensagem na tela
def banner(text):
    # Ação do botão OK
    def close_banner(e):
        page.banner.open = False
        page.update()

    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        content=ft.Text(
            text,
            text_align="CENTER"
        ),
        actions=[
            ft.TextButton("OK", on_click=close_banner)
        ],
    )
    page.banner.open = True
    page.update()

def menu_bar():
    menubar = ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor=ft.colors.RED_100,
            mouse_cursor={
                ft.MaterialState.HOVERED: ft.MouseCursor.WAIT,
                ft.MaterialState.DEFAULT: ft.MouseCursor.ZOOM_OUT
            },
        ),
        controls=[
            ft.SubmenuButton(
                content=ft.Text("Arquivo"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Salvar como .csv"),
                        leading=ft.Icon(ft.icons.SAVE_AS_OUTLINED),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=handle_save_csv_click
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Salvar como .json"),
                        leading=ft.Icon(ft.icons.SAVE_AS_SHARP),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=handle_save_json_click
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Desconectar"),
                        leading=ft.Icon(ft.icons.CLOSE),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=handle_disconnect_click
                    )
                ]
            ),
            ft.SubmenuButton(
                content=ft.Text("Editar"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Limite de registros"),
                        leading=ft.Icon(ft.icons.FORMAT_LIST_NUMBERED),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=handle_limit_click
                    )
                ]
            ),
            ft.SubmenuButton(
                content=ft.Text("Ferramentas"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Árvore de Tabelas"),
                        leading=ft.Icon(ft.icons.ACCOUNT_TREE_OUTLINED),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=handle_tree_click
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Tabela de Dados"),
                        leading=ft.Icon(ft.icons.DATASET_OUTLINED),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=handle_table_click
                    )
                ]
            )
        ]
    )
    return ft.Row([menubar])

def handle_disconnect_click(e):
    display_action(e)
    page.views.pop()
    page.go("/")
    try:
        if con:
            con.close()
    except Exception as e:
        banner(e)

def display_action(e):
    page.show_snack_bar(ft.SnackBar(content=ft.Text(f"{e.control.content.value}")))

def handle_save_csv_click(e):
    display_action(e)
    pass

def handle_save_json_click(e):
    display_action(e)
    pass

def handle_limit_click(e):
    display_action(e)
    pass

def handle_tree_click(e):
    display_action(e)
    pass

def handle_table_click(e):
    display_action(e)
    pass

# Lista dos bancos de dados disponíveis
def draw_select_db_page():
    # Banco de dados foi selecionado
    def db_changed(e):
        # Tabela foi selecionada
        def table_changed(e):
            banner(f"Carregando a tabela {table_field.value}")
            cursor = con.cursor()
            cursor.execute(f"SELECT * FROM {table_field.value};")
            table = cursor.fetchall()
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

        db_name = db_field.value
        if db_name:
            try:
                cursor = con.cursor()
                if usr_credentials["database"] == "MySQL":
                    cursor.execute(f"USE {db_name};")
                    cursor.execute("SHOW TABLES;")
                elif usr_credentials["database"] == "PostgreSQL":
                    cursor.execute(f"SET search_path TO {db_name};")
                    cursor.execute("SELECT table_name FROM information_schema.tables;")
                tables = cursor.fetchall()
                table_field = ft.Dropdown(
                    label="Tabela",
                    on_change=table_changed
                )
                for table in tables:
                    table_field.options.append(ft.dropdown.Option(table[0]))
                page.add(menu_bar(), table_field)
                page.update()
            except Exception as e:
                 banner(e)

    try:
        cursor = con.cursor()
        if usr_credentials["database"] == "MySQL":
            cursor.execute("SHOW DATABASES;")
        elif usr_credentials["database"] == "PostgreSQL":
            cursor.execute("SELECT schema_name FROM information_schema.schemata;")
        databases = cursor.fetchall()
        db_field = ft.Dropdown(
            label="Banco de dados",
            on_change=db_changed    
        )
        for database in databases:
            db_field.options.append(ft.dropdown.Option(database[0]))
        db_view = ft.View("/db",[
            menu_bar(),
            db_field
        ])
        page.views.append(db_view)
        page.go("/db")
    except Exception as e:
        banner(e)
        
# Conectar ao gerenciador de bancos de dados
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
        banner("Conexão realizada com sucesso.")
        draw_select_db_page()
    except Exception as e:
        banner(e)

# Página inicial
def main(p: ft.Page):
    global page
    page = p
    #page.client_storage.clear()

    if(platform.system() == "Windows"):
        page.platform = ft.PagePlatform.WINDOWS
    elif(platform.system() == "Linux"):
        page.platform = ft.PagePlatform.LINUX
    elif(platform.system() == "Darwin"):
        page.platform = ft.PagePlatform.MACOS

    # Ação do botão Conectar
    def on_con_button_click(e):
        global page
        global usr_credentials
        if not user_field.value or not password_field.value or not db_type_field.value:
            banner("Os campos usuário, senha e banco de dados devem estar preenchidos.")
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
                credentials.save_credentials(page, usr_credentials)
            else:
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