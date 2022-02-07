from kivy.app import App
from kivy.uix.button import Button
from infi.systray import SysTrayIcon
from kivy.core.window import Window
from kivy.clock import Clock
import sys


class TestApp(App):

    def build(self):
        btn = Button(text='Hello World')

        # tracking window events
        Window.on_minimize = self.on_minimize
        Window.on_request_close = self.on_close

        # create tray icon
        menu_options = (('Show', None, self.systray_show),)
        self.systray = SysTrayIcon(
            'icon.ico',
            'Example',
            menu_options,
            self.systray_close,
            default_menu_index=0, )
        self.systray.start()

        return btn

    def systray_show(self, systray):
        """
        A command that is called from the tray icon.
        """

        Clock.schedule_once(self.show, 0.1)

    def systray_close(self, systray):
        """
        A command that is called from the tray icon.
        """

        Clock.schedule_once(self.on_close, 0.1)

    def show(self, e):
        Window.restore()
        Window.show()
        Window.raise_window()

    def on_minimize(self):
        Window.hide()

    def on_close(self, x=None):
        try:
            self.systray.shutdown()
        except Exception as e:
            print(e)
        Clock.schedule_once(Window.close, 0.1)
        sys.exit()


TestApp().run()
