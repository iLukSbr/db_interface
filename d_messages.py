import flet as ft

# Mensagem na tela
def banner(text, page):
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

def display_action(e, page):
    page.show_snack_bar(ft.SnackBar(content=ft.Text(f"{e.control.content.value}")))