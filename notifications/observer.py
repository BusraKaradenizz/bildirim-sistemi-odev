class NotificationManager:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, mesaj):
        for observer in self.observers:
            observer.gonder(mesaj)
