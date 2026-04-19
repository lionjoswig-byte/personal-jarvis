class Engine:
    def start(self):
        raise NotImplementedError("The start method must be implemented by subclasses.")

    def stop(self):
        raise NotImplementedError("The stop method must be implemented by subclasses.")

    def status(self):
        raise NotImplementedError("The status method must be implemented by subclasses.")
