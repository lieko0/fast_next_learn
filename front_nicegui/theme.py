from contextlib import contextmanager

from nicegui import ui

from front_nicegui.menu import menu


@contextmanager
def frame(navigation_title: str):
    """Custm pag fram to shre the same styling and behavior acrss all pages"""
    ui.colors(
        primary='#6E93D6',
        secondary='#53B689',
        accent='#111B1E',
        positive='#53B689',
    )
    with ui.header():
        ui.label('☁️').classes('font-bold')
        ui.space()
        ui.label(navigation_title)
        ui.space()
        with ui.row():
            menu()
    with ui.column().classes('absolute-center items-center'):
        yield
