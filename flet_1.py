import flet as ft
import flet.canvas as cv
import math
stroke_paint = ft.Paint(stroke_width=2, style=ft.PaintingStyle.STROKE)
fill_paint = ft.Paint(style=ft.PaintingStyle.FILL)

def main(page: ft.Page):
    page.title = "Flet Próba"
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    stroke_paint = ft.Paint(stroke_width=2, style=ft.PaintingStyle.STROKE)
    fill_paint = ft.Paint(style=ft.PaintingStyle.FILL)
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    txt_number2 = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=50)
    txt_szoveg = ft.TextField(value="Hello", text_align=ft.TextAlign.CENTER, width=150)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    def minus_click2(e):
        txt_number2.value = str(int(txt_number2.value) - 1)
        page.update()

    def plus_click2(e):
        txt_number2.value = str(int(txt_number2.value) + 1)
        page.update()

    cp = cv.Canvas(
        [
            cv.Circle(100, 100, 50, stroke_paint),
            cv.Circle(80, 90, 10, stroke_paint),
            cv.Circle(84, 87, 5, fill_paint),
            cv.Circle(120, 90, 10, stroke_paint),
            cv.Circle(124, 87, 5, fill_paint),
            cv.Arc(70, 95, 60, 40, 0, math.pi, paint=stroke_paint),
        ],
        width=float("inf"),
        expand=True,
    )
    
    
    page.add(
        ft.Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur quis nibh vitae purus consectetur Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur quis nibh vitae purus consectetur Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur quis nibh vitae purus consectetur Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur quis nibh vitae purus consectetur facilisis sed vitae ipsum. Quisque faucibus sed nulla placerat sagittis. Phasellus condimentum risus vitae nulla vestibulum auctor. Curabitur scelerisque, nibh eget imperdiet consequat, odio ante tempus diam, sed volutpat nisl erat eget turpis. Sed viverra, diam sit amet blandit vulputate, mi tellus dapibus lorem, vitae vehicula diam mauris placerat diam. Morbi sit amet pretium turpis, et consequat ligula. Nulla velit sem, suscipit sit amet dictum non, tincidunt sed nulla. Aenean pellentesque odio porttitor sagittis aliquam. Nam varius at metus vitae vulputate. Praesent faucibus nibh lorem, eu pretium dolor dictum nec. Phasellus eget dui laoreet, viverra magna vitae, pellentesque diam.",
            width=700,
            height=100,),
        
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
                ft.ElevatedButton("Say hello!"),
                ft.Divider(height=30, color="#aaff0000",thickness=40),                
                txt_szoveg,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        
        
    )
    page.add(cp)
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click2,scale=1,bgcolor="#aaff0000"),
                txt_number2,
                ft.IconButton(ft.icons.ENGINEERING, on_click=plus_click2,scale=1,bgcolor="#aaff0000", tooltip="Hello"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            
        )
        
    )

ft.app(main)