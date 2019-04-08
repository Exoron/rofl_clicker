class GameObject(object):
    def draw(self, surface, coords):
        raise NotImplementedError

    def handle_event(self, event):
        raise NotImplementedError
