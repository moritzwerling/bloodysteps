class StateMachine:
    def __init__(self, initial_state):
        self.currentState = initial_state
        self.currentState.run()

    def update(self, event):
        self.currentState = self.currentState.next(event)
        self.currentState.run()


class State:
    def run(self):
        assert 0, "run not implemented"

    def next(self, event):
        assert 0, "next not implemented"

