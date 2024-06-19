import flet as ft
from datetime import datetime

log_file_path = "db_interface.log"

def display_action(arg, page):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    message = f"{current_time}: {arg}"

    page.show_snack_bar(ft.SnackBar(content=ft.Text(message)))

    log_to_file(message)

def log_to_file(message):
    with open(log_file_path, 'a') as log_file:
        log_file.write(message + '\n')