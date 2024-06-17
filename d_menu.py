import flet as ft
import pymysql as my
import psycopg2 as pg
import os
import pandas as pd

from d_messages import display_action

global page, con, usr_credentials

def menu_bar(p, c, u):
    global page, con, usr_credentials
    page = p
    con = c
    usr_credentials = u
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
                        content=ft.Text("Exportar como..."),
                        leading=ft.Icon(ft.icons.SAVE_AS_OUTLINED),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=handle_save_click
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Desconectar"),
                        leading=ft.Icon(ft.icons.CLOSE),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=lambda e: handle_disconnect_click(e, con)
                    )
                ]
            ),
            ft.SubmenuButton(
                content=ft.Text("Ferramentas"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Árvore de tabelas"),
                        leading=ft.Icon(ft.icons.ACCOUNT_TREE_OUTLINED),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=handle_tree_click
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Tabela de dados"),
                        leading=ft.Icon(ft.icons.DATASET_OUTLINED),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=handle_table_click
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Consulta personalizada"),
                        leading=ft.Icon(ft.icons.DASHBOARD_CUSTOMIZE_OUTLINED),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=handle_query_click
                    )
                ]
            )
        ]
    )
    return ft.Row([menubar])
    
def handle_disconnect_click(e, con):
    global page
    display_action(e.control.content.value, page)
    page.views.pop()
    page.go("/")
    try:
        if con:
            con.close()
    except Exception as e:
        display_action(e, page)

def handle_save_click(e):
    from d_table import get_table
    from d_query import get_table_query
    global page

    display_action(e.control.content.value, page)
    current_view = page.views[-1]
    if current_view.route == "/table" or current_view.route == "/query":
        extensions=[
            ".csv",
            ".json"
        ]
        if current_view.route == "/query":
            data, column_list = get_table_query()
        else:
            data, column_list = get_table()
        if not data or len(data) == 0:
            display_action("Nenhum dado para salvar.", page)
            return
        df = pd.DataFrame(data, columns=column_list)
    elif current_view.route == "/tree":
        extensions=[
            ".svg"
        ]
    if current_view.route == "/table" and len(page.views[-1].controls) == 6:
        filename = page.views[-1].controls[2].value + ".csv"
    elif current_view.route == "/table" or current_view.route == "/query":
        filename = "table_export.csv"
    elif current_view.route == "/tree":
        filename = "tree_export.svg"

    def save_file(e):
        filepath = e.path
        if filepath:
            extension = os.path.splitext(filepath)[1]
            if extension in extensions:
                if extension == ".csv":
                    df.to_csv(filepath,
                        header=True,
                        index=False
                    )
                elif extension == ".json":
                    df.to_json(
                        filepath,
                        orient='records',
                        lines=True
                    )

    save_file_dialog = ft.FilePicker(on_result = save_file)
    page.overlay.append(save_file_dialog)
    page.update()
    save_file_dialog.save_file(
        dialog_title="Exportar como...",
        file_name=filename,
        initial_directory=".",
        allowed_extensions=extensions
    )

def handle_tree_click(e):
    from d_tree import draw_tree_view

    global page

    display_action(e.control.content.value, page)
    page.views.pop()
    page.update()
    draw_tree_view(page, con, usr_credentials)

def handle_table_click(e):
    from d_table import draw_table_view

    global page, con, usr_credentials

    display_action(e.control.content.value, page)
    page.views.pop()
    page.update()
    draw_table_view(page, con, usr_credentials)

def handle_query_click(e):
    from d_query import queries

    global page, con
    
    display_action(e.control.content.value, page)
    queries(page, con, usr_credentials)