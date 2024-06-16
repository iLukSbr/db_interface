import flet as ft
import pymysql as my
import psycopg2 as pg

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
def handle_tree_click(e):
    global page
    display_action(e.control.content.value, page)
    page.views.pop()
    pass

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