import flet as ft

global table, column_names

def queries(page, con, usr_credentials):
    from d_table import create_table_display
    from d_menu import menu_bar
    from d_messages import display_action

    menubar = menu_bar(page, con, usr_credentials)
    query_field = ft.TextField(
        label="",
        multiline=True
    )

    def handle_query_click(e):
        global table, column_names
        query_text = query_field.value

        query_button = ft.ElevatedButton(
            text="Executar",
            on_click=handle_query_click
        )

        try:
            cursor = con.cursor()
            if ';' in query_text:
                queries = query_text.split(';')
                for query in queries:
                    if query.strip():  # Ignorar consultas vazias
                        cursor.execute(query)
            else:
                cursor.execute(query_text)
            table = cursor.fetchall()
            display_action(f"Executando consulta...", page)
            if not table or len(table) == 0:
                display_action("Nenhum resultado recebido.", page)
                scroll_tab = None
            else:
                column_names = [desc[0] for desc in cursor.description]
                scroll_tab = create_table_display(table, column_names)
                query_view = ft.View(
                    "/query",[
                        menubar,
                        query_field,
                        query_button,
                        scroll_tab
                    ]
                )
                page.views.pop()
                page.views.append(query_view)
                page.update()
                page.go(query_view.route)
        except Exception as e:
            display_action(e, page)

    query_button = ft.ElevatedButton(
        text="Executar",
        on_click=handle_query_click
    )

    query_view = ft.View(
        "/query",[
            menubar,
            query_field,
            query_button
        ]
    )
    page.views.pop()
    page.views.append(query_view)
    page.update()
    page.go(query_view.route)

def get_table_query():
    global table, column_names
    if 'table' in globals():
        return table, column_names
    else:
        return None, None