from traffic_light_fsm import TrafficLightFSM


class TestTrafficLightsStateMachine(object):
    def test_state_transitions(self):

        traffic_light = TrafficLightFSM()
        assert traffic_light.currentState == TrafficLightFSM.go_state

        traffic_light.update(TrafficLightFSM.light_change_timer_elapsed_event)
        assert traffic_light.currentState == TrafficLightFSM.go_state

        traffic_light.update(TrafficLightFSM.button_pressed_event)
        assert traffic_light.currentState == TrafficLightFSM.prepare_to_stop_state

        traffic_light.update(TrafficLightFSM.light_change_timer_elapsed_event)
        assert traffic_light.currentState == TrafficLightFSM.stop_state

        traffic_light.update(TrafficLightFSM.button_pressed_event)
        assert traffic_light.currentState == TrafficLightFSM.stop_state

        traffic_light.update(TrafficLightFSM.pedestrian_green_timer_elapsed_event)
        assert traffic_light.currentState == TrafficLightFSM.prepare_to_start_state

        traffic_light.update(TrafficLightFSM.light_change_timer_elapsed_event)
        assert traffic_light.currentState == TrafficLightFSM.go_state



