import flet as ft
import subprocess as sp
import os
import re
import sys

from d_messages import display_action

def erd_generator(usr_credentials, db_name, page):
    try:
        output_file = os.path.join(os.getcwd(), 'schema.sql')

        if usr_credentials["database"] == "MySQL":
            command = f'mysqldump -u {usr_credentials["user"]} -p{usr_credentials["password"]} --no-data {db_name} > {output_file}'
            js_file = os.path.join(os.getcwd(), 'mysql2dbml.js')
        elif usr_credentials["database"] == "PostgreSQL":
            os.environ['PGPASSWORD'] = usr_credentials["password"]
            command = f'pg_dump -U {usr_credentials["user"]} -h {usr_credentials["host"]} -p {usr_credentials["port"]} -w -s -O -x --no-comments --no-publications --no-security-labels --no-subscriptions --no-table-access-method --no-tablespaces --no-toast-compression --no-unlogged-table-data -n {db_name} > {output_file}'
            js_file = os.path.join(os.getcwd(), 'postgres2dbml.js')

        try:
            sp.run(command, shell=True, check=True, capture_output=True, text=True)
        except sp.CalledProcessError as e:
            display_action(e.stderr, page)

        if(usr_credentials["database"] == "PostgreSQL"):
            with open(output_file, 'r') as file:
                sql = file.read()
            function_pattern = re.compile(r'-- Name: .*?; Type: FUNCTION;.*?END;\n\n\$\$;', re.DOTALL)
            sql_without_functions = re.sub(function_pattern, '', sql)
            with open(output_file, 'w') as file:
                file.write(sql_without_functions)

        sp.run(['node', js_file], check=True, capture_output=True, text=True)

        command = 'npx dbml-renderer -i schema.dbml -o schema.svg'
        sp.run(command, shell=True, check=True, capture_output=True, text=True)
        
    except Exception as e:
        display_action(e, page)

# Lista dos bancos de dados disponíveis
def draw_tree_view(page, con, usr_credentials):
    from d_menu import menu_bar

    menubar = menu_bar(page, con, usr_credentials)

    # Um banco de dados foi escolhido
    def db_selected(e):
        db_name = e.control.value
        db_selector = gen_db_list(db_name)

        erd_generator(usr_credentials, db_name, page)
        img = ft.Image(
            src=f"schema.svg",
            width=1000,
            height=1000,
            fit=ft.ImageFit.CONTAIN
        )
        vertical = ft.Column([img],scroll=True)
        horizontal = ft.Row([vertical], scroll=ft.ScrollMode.ALWAYS, expand=1,vertical_alignment=ft.CrossAxisAlignment.START)

        if db_name:
            tree_view = ft.View(
                "/tree",[
                    menubar,
                    db_selector,
                    horizontal
                ]
            )
            page.views.pop()
            page.views.append(tree_view)
            page.update()
            page.go(tree_view.route)

    # Gerar seletor de banco de dados
    def gen_db_list(val):
        try:
            cursor = con.cursor()
            if usr_credentials["database"] == "MySQL":
                cursor.execute("SHOW DATABASES;")
            elif usr_credentials["database"] == "PostgreSQL":
                cursor.execute("SELECT schema_name FROM information_schema.schemata ORDER BY schema_name ASC;")
            databases = cursor.fetchall()
        except Exception as e:
            display_action(e, page)
        db_field = ft.Dropdown(
            label="Banco de dados",
            on_change=db_selected,
            value=val
        )
        for database in databases:
            db_field.options.append(ft.dropdown.Option(database[0]))
        return db_field
    
    db_selector = gen_db_list(None)
    db_view = ft.View(
        "/tree",[
            menubar,
            db_selector
        ]
    )
    page.views.append(db_view)
    page.update()
    page.go(db_view.route)