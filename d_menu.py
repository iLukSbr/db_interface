import flet as ft
import pymysql as my
import psycopg2 as pg

from d_messages import *
from d_save import *

global page

def menu_bar(p, con):
    global page
    page = p
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
                        content=ft.Text("Exportar como .csv"),
                        leading=ft.Icon(ft.icons.SAVE_AS_OUTLINED),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=handle_save_csv_click
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Exportar como .json"),
                        leading=ft.Icon(ft.icons.SAVE_AS_SHARP),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=handle_save_json_click
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Exportar como .svg"),
                        leading=ft.Icon(ft.icons.SAVE),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=handle_save_json_click
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

def handle_save_csv_click(e):
    global page
    display_action(e.control.content.value, page)
    page.views.pop()
    pass

def handle_save_json_click(e):
    global page
    display_action(e.control.content.value, page)
    page.views.pop()
    pass

def handle_limit_click(e):
    global page
    display_action(e.control.content.value, page)
    page.views.pop()
    pass

def handle_tree_click(e):
    global page
    display_action(e.control.content.value, page)
    page.views.pop()
    pass

def handle_table_click(e):
    global page
    display_action(e.control.content.value, page)
    page.views.pop()
    
    pass