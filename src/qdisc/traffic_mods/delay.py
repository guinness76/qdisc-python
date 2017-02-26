from traffic_mod import TrafficMod


class Delay(TrafficMod):
    delay_descr = "Add a Delay modification description here"
    delay_time = None
    delay_jitter = None
    delay_jitter_correlation = None
    delay_distribution = None

    def __init__(self):
        TrafficMod.__init__(self, self.delay_descr)
