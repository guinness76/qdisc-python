from javax.swing import JPanel


class TrafficMod(JPanel):
    descr = None

    def __init__(self, descr):
        self.descr = descr
