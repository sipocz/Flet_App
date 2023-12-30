import flet as ft

def main(page: ft.Page):
    page.title = "Flet Próba"
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.MainAxisAlignment.SPACE_EVENLY

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    txt_number2 = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    def minus_click2(e):
        txt_number2.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click2(e):
        txt_number2.value = str(int(txt_number.value) + 1)
        page.update()

    
    
    
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        
    )
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click2),
                txt_number2,
                ft.IconButton(ft.icons.ADD, on_click=plus_click2),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        
    )

ft.app(main)