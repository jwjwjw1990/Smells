class Controller:

    def __init__(self, view, application):
        self._view = view()
        self._application = application
        self._view.render(self._application.app())
        self._application.update()

    # Getters
    def view(self):
        return self._view

    def app(self):
        return self._application
