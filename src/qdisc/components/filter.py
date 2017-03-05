class Filter():
    src_addr = None
    src_port = -1
    dest_addr = None
    dest_port = -1

    # corrupt = Corrupt()
    # delay = Delay()
    # duplicate = Duplicate()
    # loss = Loss()
    # rate = Rate()
    # reorder = Reorder()

    # def __init__(self):

    def print_filter(self):
        return ("src_addr=%s, src_port=%d, dest_addr=%s, dest_port=%d" % (
            self.src_addr, self.src_port, self.dest_addr, self.dest_port))
