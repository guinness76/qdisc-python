from traffic_mod import TrafficMod


class Reorder(TrafficMod):
    reorder_descr = "Add a Reorder modification description here"
    reorder_percent = None
    reorder_percent_correlation = None
    reorder_gap = None

    def __init__(self):
        TrafficMod.__init__(self, self.reorder_descr)
