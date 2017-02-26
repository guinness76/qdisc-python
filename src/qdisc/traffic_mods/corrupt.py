from traffic_mod import TrafficMod


class Corrupt(TrafficMod):
    corrupt_descr = "Add a Corrupt modification description here"
    corrupt_percent = None
    corrupt_percent_correlation = None


    def __init__(self):
        TrafficMod.__init__(self, self.corrupt_descr)