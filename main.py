import flet as ft 

def main(page: ft.Page):
    page.title('Just avoe')

    page.add(
    ft.Row(controls=[
        ft.Text("A"),
        ft.Text("B"),
        ft.Text("C")
    ])
)
    
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)