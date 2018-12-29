from guizero import App


class Application:
    # Default variables
    _is_full_screen = False
    _controller = None

    # Constructor
    def __init__(self):
        self.initialize_application()

    # Public methods
    def initialize_application(self):
        self._app = App(
            title=self._window_title(),
            width=self._window_width(),
            height=self._window_height(),
            layout="grid"
        )
        self._app.tk.attributes("-fullscreen", self._full_screen())

    def set_controller(self, controller):
        self.clear_controller()
        self._controller = controller(self)

    def update(self):
        self._app.update()

    def display(self):
        self._app.display()

    # Private methods
    def clear_controller(self):
        if self._controller is not None:
            self._controller.view().destroy()  # Destroy old view controller
        self._controller = None

    # Public Getters
    def app(self):
        return self._app

    # Getters
    def _window_width(self):
        return 300

    def _window_height(self):
        return 300

    def _window_title(self):
        return "title"

    def _full_screen(self):
        return self._is_full_screen