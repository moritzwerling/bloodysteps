from MouseTrap import MouseTrap, MouseAction
from traffic_light_fsm import TrafficLightFSM, TrafficLightsEvents

# 28866

'''
class TestMouseTrap(object):
    def test_simple(self):
        mouse_trap = MouseTrap()
        assert mouse_trap.currentState == MouseTrap.waiting

        mouse_trap.update(MouseAction.appears)
        assert mouse_trap.currentState == MouseTrap.luring

        mouse_trap.update(MouseAction.runsAway)
        assert mouse_trap.currentState == MouseTrap.waiting
'''


class TestTrafficLightsStateMachine(object):
    def test_state_transitions(self):

        traffic_light = TrafficLightFSM()
        assert traffic_light.currentState == TrafficLightFSM.go

        traffic_light.update(TrafficLightsEvents.light_change_timer_elapsed)
        assert traffic_light.currentState == TrafficLightFSM.go

        traffic_light.update(TrafficLightsEvents.button_pressed)
        assert traffic_light.currentState == TrafficLightFSM.prepare_to_stop

        traffic_light.update(TrafficLightsEvents.light_change_timer_elapsed)
        assert traffic_light.currentState == TrafficLightFSM.stop

        traffic_light.update(TrafficLightsEvents.button_pressed)
        assert traffic_light.currentState == TrafficLightFSM.stop

        traffic_light.update(TrafficLightsEvents.pedestrian_green_timer_elapsed)
        assert traffic_light.currentState == TrafficLightFSM.prepare_to_start

        traffic_light.update(TrafficLightsEvents.light_change_timer_elapsed)
        assert traffic_light.currentState == TrafficLightFSM.go



