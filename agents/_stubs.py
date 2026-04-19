# agents/_stubs.py

class Agent:
    def __init__(self, name):
        self.name = name

    def act(self):
        raise NotImplementedError("Subclasses should implement this method!")

class ReAct(Agent):
    def act(self):
        return f"{self.name} is reacting to input."

class Orchestrator(Agent):
    def act(self):
        return f"{self.name} is orchestrating tasks."

class SimpleAgent(Agent):
    def act(self):
        return f"{self.name} is performing a simple action."