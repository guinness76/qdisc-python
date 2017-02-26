from traffic_mod import TrafficMod


class Duplicate(TrafficMod):
    duplicate_descr = "Add a Duplicate modification description here"
    duplicate_percent = None
    duplicate_percent_correlation = None

    def __init__(self):
        TrafficMod.__init__(self, self.duplicate_descr)
