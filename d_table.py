import flet as ft
import pymysql as my
import psycopg2 as pg

def create_table_display(table, column_names):
    table_display = ft.DataTable(
        columns=[ft.DataColumn(ft.Text(name)) for name in column_names],
        rows=[ft.DataRow(cells=[ft.DataCell(ft.Text(str(value))) for value in row]) for row in table],
    )
    vertical = ft.Column([table_display],scroll=True)
    horizontal = ft.Row([vertical], scroll=ft.ScrollMode.ALWAYS, expand=1,vertical_alignment=ft.CrossAxisAlignment.START)
    return horizontal

# Lista dos bancos de dados disponíveis
def draw_table_view(page, con, usr_credentials):
    from d_messages import display_action
    from d_menu import menu_bar

    menubar = menu_bar(page, con, usr_credentials)

    # Gerar seletor de tabela
    def gen_tables_list(db_name, val):
        try:
            cursor = con.cursor()
            if usr_credentials["database"] == "MySQL":
                cursor.execute(f"USE {db_name};")
                cursor.execute("SHOW TABLES;")
            elif usr_credentials["database"] == "PostgreSQL":
                cursor.execute(f"SELECT tablename FROM pg_catalog.pg_tables where schemaname='{db_name}' ORDER By tablename ASC;")
            tables = cursor.fetchall()
            if usr_credentials["database"] == "PostgreSQL":
                cursor.execute(f"SET search_path TO {db_name};")
        except Exception as e:
            display_action(e, page)
        table_field = ft.Dropdown(
            label="Tabela",
            on_change=lambda e: table_selected(e, db_name),
            value=val
        )
        for table in tables:
            table_field.options.append(ft.dropdown.Option(table[0]))
        return table_field

    # Um banco de dados foi escolhido
    def db_selected(e):
        db_name = e.control.value
        table_selector = gen_tables_list(db_name, None)
        db_selector = gen_db_list(db_name)
        if db_name:
            table_view = ft.View(
                "/table",[
                    menubar,
                    db_selector,
                    table_selector
                ]
            )
            page.views.pop()
            page.views.append(table_view)
            page.update()
            page.go(table_view.route)

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
    
    # Uma tabela foi escolhida
    def table_selected(e, db_name):
        limit_field = ft.TextField(
            label="Quantidade máxima de registros",
            value="1000"
        )
        load_table(e, db_name, limit_field)
   
    # Carregar tabela escolhida
    def load_table(table_selection_evt, db_name, limit_field):
        def on_limit_button_click(e, table_selection_evt, db_name, limit_field):
            load_table(table_selection_evt, db_name, limit_field)

        display_action(f"Carregando a tabela {table_selection_evt.control.value}", page)
        try:
            cursor = con.cursor()
            cursor.execute(f"SELECT * FROM {table_selection_evt.control.value} LIMIT {limit_field.value};")
            table = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
        except Exception as e:
            display_action(e, page)

        scroll_tab = create_table_display(table, column_names)
        
        table_selector = gen_tables_list(db_name, table_selection_evt.control.value)
        db_selector = gen_db_list(db_name)
        
        limit_button = ft.ElevatedButton(
            text="Limitar",
            on_click=lambda button_evt: on_limit_button_click(button_evt, table_selection_evt, db_name, limit_field)
        )

        if db_name:
            table_view = ft.View(
                "/table",[
                    menubar,
                    db_selector,
                    table_selector,
                    limit_field,
                    limit_button,
                    scroll_tab
                ]
            )
            page.views.pop()
            page.views.append(table_view)
            page.update()
            page.go(table_view.route)

    db_selector = gen_db_list(None)
    db_view = ft.View(
        "/table",[
            menubar,
            db_selector
        ]
    )
    page.views.append(db_view)
    page.update()
    page.go(db_view.route)
