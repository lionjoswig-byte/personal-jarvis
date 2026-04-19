class Tool:
    def __init__(self, name):
        self.name = name

    def execute(self):
        raise NotImplementedError("This method should be overridden by subclasses")
