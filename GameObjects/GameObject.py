class GameObject(object):
    def draw(self):
        raise NotImplementedError

    def handle_event(self, event):
        raise NotImplementedError
