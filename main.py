import flet as ft
from datetime import datetime


def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Hello world")
    history_text = ft.Text('История приветствий:')
    favorites_text = ft.Text('Избранные имена:')

    greeting_history = []
    favorites = []
    history_file = "history.txt"

   
    try:
        with open(history_file, "r", encoding="utf-8") as f:
            greeting_history = [line.strip() for line in f.readlines()]
        history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
    except FileNotFoundError:
       
        pass

    
    def on_button_click(_):
        name = name_input.value.strip()
        timestamp = datetime.now().strftime("%H:%M")

        if name:
            greeting = f"{timestamp} - {name}"
            greeting_text.value = f"{timestamp} Hello {name}"
            greeting_text.color = None
            name_input.value = ''

           
            greeting_history.append(greeting)
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)

            
            with open(history_file, "a", encoding="utf-8") as f:
                f.write(greeting + "\n")

        else:
            greeting_text.value = "Введите корректное имя"
            greeting_text.color = ft.Colors.YELLOW

        page.update()

    def add_to_favorites(_):
        if greeting_history:
            last_name = greeting_history[-1].split(" - ")[-1]
            if last_name not in favorites:
                favorites.append(last_name)
                favorites_text.value = "Избранные имена:\n" + "\n".join(favorites)
                page.update()

    
    def clear_history(_):
        greeting_history.clear()
        history_text.value = 'История приветствий:'
        
        with open(history_file, "w", encoding="utf-8") as f:
            f.write("")
        page.update()

    
    def theme_mode(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
          
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
          
        page.update()

    
    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)
    name_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, on_click=on_button_click)
    fav_button = ft.IconButton(icon=ft.Icons.FAVORITE, on_click=add_to_favorites)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    theme_mode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=theme_mode)
    
 
    page.add(greeting_text,name_input,name_button,fav_button,clear_button,theme_mode_button, history_text,favorites_text)


ft.app(target=main)

