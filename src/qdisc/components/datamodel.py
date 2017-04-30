class Profile():
    profile_name = None
    profile_descr = None
    filters = []
    rate_config = None
    delay = None
    loss = None
    corrupt = None
    duplicate = None
    reorder = None


class Filter():
    src_addr = None
    src_port = -1
    dest_addr = None
    dest_port = -1

    def print_filter(self):
        return ("src_addr=%s, src_port=%d, dest_addr=%s, dest_port=%d" % (
            self.src_addr, self.src_port, self.dest_addr, self.dest_port))


class Rate():
    rate = None
    packets = None
    cellsize = None
    celloverhead = None


class Delay():
    delay_time = None
    delay_timescale = None
    delay_deviation = None
    deviation_timescale = None
    delay_correlation = None
    distribution = None


class Loss():
    loss_type = None
    random_percent = None
    random_percent_correlation = None

    loss_state_p13 = None
    loss_state_p31 = None
    loss_state_p32 = None
    loss_state_p23 = None
    loss_state_p14 = None

    loss_gemodel_p = None
    loss_gemodel_r = None
    loss_gemodel_h = None
    loss_gemodel_k = None


class Corrupt():
    corrupt_percent = None
    corrupt_percent_correlation = None


class Duplicate():
    duplicate_percent = None
    duplicate_percent_correlation = None


class Reorder():
    reorder_percent = None
    reorder_percent_correlation = None
    reorder_gap = None
