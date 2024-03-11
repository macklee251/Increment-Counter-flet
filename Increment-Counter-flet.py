import flet as ft

def main(page: ft.Page) -> None:
    page.title="Increment Counter"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.theme_mode="light"
    
    TextField = ft.TextField(value='0', text_align=ft.TextAlign.CENTER, width=100)
    
    # e -> controle event
    def increment(e) -> None:
        TextField.value = str(int(TextField.value) + 1)
        page.update(TextField)
    
    def decrease(e) -> None:
        TextField.value = str(int(TextField.value) - 1)
        page.update(TextField)
        
    page.add(ft.Row(
        controls=[
            ft.IconButton(ft.icons.REMOVE, on_click=decrease), 
            TextField,
            ft.IconButton(ft.icons.ADD, on_click=increment),
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ))
    
    
ft.app(target=main, view=ft.AppView.WEB_BROWSER)