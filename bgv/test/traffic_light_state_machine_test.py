from MouseTrap import MouseTrap, MouseAction

# 28866

class TestTrafficLightsStateMachine(object):

    def test_simple(self):
        mouse_trap = MouseTrap()
        assert mouse_trap.currentState == MouseTrap.waiting

        mouse_trap.update(MouseAction.appears)
        assert mouse_trap.currentState == MouseTrap.luring

        mouse_trap.update(MouseAction.runsAway)
        assert mouse_trap.currentState == MouseTrap.waiting

