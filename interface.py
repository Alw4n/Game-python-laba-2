import flet as ft

class MainMenu:
    def __init__(self, page: ft.Page, start_game_callback):
        self.page = page
        self.page.window_width = 480
        self.page.window_height = 800
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.bgcolor = ft.colors.BLUE_GREY_900  # Темный синий фон
        
        self.start_game_callback = start_game_callback

        # Главное меню
        self.menu_screen = ft.Column(
            controls=[
                ft.Text("Добро пожаловать в игру! (Демо)", size=28, color=ft.colors.CYAN_100),  # Крупный текст светло-синий
                ft.ElevatedButton(text="Играть", on_click=self.show_levels, bgcolor=ft.colors.CYAN_300, color=ft.colors.WHITE)  # Бирюзовые кнопки
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Выравнивание по центру по вертикали
            horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Выравнивание по центру по горизонтали
        )

        self.page.add(self.menu_screen)

    def show_menu_screen(self, e=None):
        self.page.clean()
        self.page.add(self.menu_screen)
        self.page.update()

    def show_levels(self, e):
        levels_screen = ft.Column(
            controls=[
                ft.ElevatedButton(text="Уровень 1", on_click=lambda e: self.start_game_callback(1), bgcolor=ft.colors.CYAN_300, color=ft.colors.WHITE),
                ft.ElevatedButton(text="Уровень 2 (В разработке)", bgcolor=ft.colors.CYAN_300, color=ft.colors.WHITE),
                ft.ElevatedButton(text="Назад в меню", on_click=self.show_menu_screen, bgcolor=ft.colors.CYAN_300, color=ft.colors.WHITE)
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Выравнивание по центру по вертикали
            horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Выравнивание по центру по горизонтали
        )
        self.page.clean()
        self.page.add(levels_screen)
        self.page.update()

class GameWindow:
    def __init__(self, page: ft.Page, handle_command_callback, restart_callback, menu_callback):
        self.page = page
        self.page.bgcolor = ft.colors.BLUE_GREY_900  # Темный синий фон
        self.handle_command_callback = handle_command_callback
        self.restart_callback = restart_callback
        self.menu_callback = menu_callback

        # Элементы интерфейса
        self.story = ft.Text("", size=20, color=ft.colors.CYAN_100)  # Крупный текст светло-синий
        self.user_input = ft.TextField(hint_text="Введите вашу команду", width=400, text_align="center", color=ft.colors.WHITE)  # Основной текст белый
        self.send_button = ft.ElevatedButton(text="Отправить", on_click=self.handle_command, bgcolor=ft.colors.CYAN_300, color=ft.colors.WHITE)
        self.status = ft.Text("Инвентарь: Пусто", size=16, color=ft.colors.WHITE)  # Основной текст белый
        
        self.page.add(
            ft.Column(
                controls=[
                    self.story,
                    self.user_input,
                    self.send_button,
                    self.status,
                    ft.ElevatedButton(text="Начать сначала", on_click=self.restart_callback, bgcolor=ft.colors.CYAN_300, color=ft.colors.WHITE),
                    ft.ElevatedButton(text="В меню", on_click=self.menu_callback, bgcolor=ft.colors.CYAN_300, color=ft.colors.WHITE)
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Выравнивание по центру по вертикали
                horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Выравнивание по центру по горизонтали
            )
        )

    def set_status(self, status):
        self.status.value = status
        self.page.update()

    def append_text(self, text):
        self.story.value += f"{text}\n"
        self.page.update()

    def clear_text(self):
        self.story.value = ""
        self.page.update()

    def clear_command(self):
        self.user_input.value = ""
        self.page.update()

    def get_command(self):
        return self.user_input.value.strip().lower()

    def handle_command(self, e=None):
        self.handle_command_callback()

    def disable_input(self):
        self.user_input.disabled = True
        self.send_button.disabled = True
        self.page.update()

    def enable_input(self):
        self.user_input.disabled = False
        self.send_button.disabled = False
        self.page.update()
