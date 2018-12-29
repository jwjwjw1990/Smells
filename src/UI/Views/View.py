class View:
    _childs = {}

    # Public methods
    def add_child(self, key, child):
        self._childs[key] = child

    def add_childs(self, childs):
        for key in childs:
            self.add_child(key, childs[key])

    def find_child(self, key):
        return self._childs[key]

    def render(self, app):
        raise Exception('Render method is not implemented in view!')

    def destroy(self):
        for key in self._childs:
            self._childs[key].destroy()

        self._childs = {}
