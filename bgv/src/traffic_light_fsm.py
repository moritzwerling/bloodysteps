from StateMachine import StateMachine, State


class Go(State):
    def run(self):
        print("vehicles: green, pedestrians: red")

    def next(self, event):
        if event == TrafficLightsEvents.button_pressed:
            return TrafficLightFSM.prepare_to_stop
        return TrafficLightFSM.go


class PrepareToStop(State):
    def run(self):
        print("vehicles: yellow, pedestrians: yellow")

    def next(self, event):
        if event == TrafficLightsEvents.light_change_timer_elapsed:
            return TrafficLightFSM.stop
        return TrafficLightFSM.prepare_to_stop


class Stop(State):
    def run(self):
        print("vehicles: red, pedestrians: green")

    def next(self, event):
        if event == TrafficLightsEvents.pedestrian_green_timer_elapsed:
            return TrafficLightFSM.prepare_to_start
        return TrafficLightFSM.stop

class PrepareToStart(State):
    def run(self):
        print("vehicles: yellow, pedestrians: yellow")

    def next(self, event):
        if event == TrafficLightsEvents.light_change_timer_elapsed:
            return TrafficLightFSM.go
        return TrafficLightFSM.prepare_to_start


class TrafficLightFSM(StateMachine):
    go = Go()
    prepare_to_stop = PrepareToStop()
    stop = Stop()
    prepare_to_start = PrepareToStart()

    def __init__(self):
        # Initial state
        StateMachine.__init__(self, TrafficLightFSM.go)


# todo move to generic class Events in StateMachine
class TrafficLightsEvents:
    def __init__(self, event):
        self.event = event

    def __str__(self): return self.event

    def __eq__(self, other):
        return self.event == other.event

    # Necessary when __cmp__ or __eq__ is defined
    # in order to make this class usable as a
    # dictionary key:
    def __hash__(self):
        return hash(self.event)


# Static fields; an enumeration of instances:
TrafficLightsEvents.button_pressed = TrafficLightsEvents("button_pressed")
TrafficLightsEvents.light_change_timer_elapsed = TrafficLightsEvents("light change timer elapsed")
TrafficLightsEvents.pedestrian_green_timer_elapsed = TrafficLightsEvents("pedestrian green timer elapsed")
