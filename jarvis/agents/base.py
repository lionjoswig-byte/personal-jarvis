class Agent:
    """
    Base class for all agents.
    """
    def __init__(self, name):
        self.name = name

    def perform_action(self, action):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def get_name(self):
        return self.name

    def __str__(self):
        return f"Agent: {self.name}"