from traffic_mod import TrafficMod


class Loss(TrafficMod):
    loss_descr = "Add a Loss modification description here"
    loss_type = None
    loss_random_percent = None
    loss_random_percent_correlation = None
    loss_state_p13 = None
    loss_state_p31 = None
    loss_state_p32 = None
    loss_state_p23 = None
    loss_state_p14 = None
    loss_gemodel_p = None
    loss_gemodel_r = None
    loss_gemodel_h = None
    loss_gemodel_k = None

    def __init__(self):
        TrafficMod.__init__(self, self.loss_descr)
