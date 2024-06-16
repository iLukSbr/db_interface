import flet as ft

# Mensagem na tela

def display_action(arg, page):
    page.show_snack_bar(ft.SnackBar(content=ft.Text(f"{arg}")))