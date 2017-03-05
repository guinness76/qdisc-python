from java.awt import Dimension, Font
from javax.swing import JLabel, JTextField, JPanel, BoxLayout, GroupLayout, SwingConstants

from combo_boxes import BandwidthCombo, TimeCombo


class TrafficMod(JPanel):
    # descr = None
    # horizontal = None
    # vertical = None
    # layout = None
    # settings_panel = None

    def __init__(self, descr, title):
        self.descr = descr
        # self.setLayout(BoxLayout(self, BoxLayout.PAGE_AXIS))
        #
        # self.settings_panel = JPanel()
        # self.layout = GroupLayout(self.settings_panel)
        # self.layout.setAutoCreateGaps(True)
        # self.layout.setAutoCreateContainerGaps(True)
        # self.settings_panel.setLayout(self.layout)
        # self.add(self.settings_panel)
        #
        # # Horizontal group
        # self.horizontal = self.layout.createParallelGroup()
        # self.layout.setHorizontalGroup(self.layout.createSequentialGroup().addGroup(self.horizontal))
        #
        # # Vertical group
        # self.vertical = self.layout.createSequentialGroup()
        # self.layout.setVerticalGroup(self.vertical)
        #
        # # Main title, label only
        # main_title = JLabel(title)
        # main_title.setFont(Font(main_title.getFont().getName(), Font.BOLD, 14))
        # self.horizontal.addGroup(self.layout.createSequentialGroup()
        #                          .addComponent(main_title))
        # self.vertical.addGroup(self.layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
        #                        .addComponent(main_title))


class Rate(TrafficMod):
    the_rate = None
    descr = "Add a Rate modification description here"
    title = "Rate Config"
    rate_textfield = JTextField()
    packet_textfield = JTextField()
    cellsize_textfield = JTextField()
    celloverhead_textfield = JTextField()

    def __init__(self):
        TrafficMod.__init__(self, self.descr, self.title)
        self.setLayout(BoxLayout(self, BoxLayout.PAGE_AXIS))

        settings_panel = JPanel()
        layout = GroupLayout(settings_panel)
        layout.setAutoCreateGaps(True)
        layout.setAutoCreateContainerGaps(True)
        settings_panel.setLayout(layout)
        self.add(settings_panel)

        # Horizontal group
        horizontal = layout.createParallelGroup()
        layout.setHorizontalGroup(layout.createSequentialGroup().addGroup(horizontal))

        # Vertical group
        vertical = layout.createSequentialGroup()
        layout.setVerticalGroup(vertical)

        # Main title, label only
        main_title = JLabel("Rate Settings")
        main_title.setFont(Font(main_title.getFont().getName(), Font.BOLD, 14))
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(main_title))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(main_title))

        bc = BandwidthCombo()
        rates_combo = bc.get_combo_box()
        # rates_combo.setMaximumSize(Dimension(100, 20))
        # rates_combo.addActionListener(self) todo implement listener

        # Base rate
        rate_lbl = JLabel("Rate")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(rate_lbl)
                            .addComponent(self.rate_textfield)
                            .addComponent(rates_combo))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(rate_lbl)
                          .addComponent(self.rate_textfield)
                          .addComponent(rates_combo))
        self.rate_textfield.setMaximumSize(Dimension(100, 20))

        # Packet overhead
        packet_overhead_lbl = JLabel("Packet Overhead")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(packet_overhead_lbl)
                            .addComponent(self.packet_textfield))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(packet_overhead_lbl)
                          .addComponent(self.packet_textfield))
        self.packet_textfield.setMaximumSize(Dimension(100, 20))

        layout.linkSize(SwingConstants.HORIZONTAL, packet_overhead_lbl, rate_lbl)

        # Cell size
        cell_size_lbl = JLabel("Cell Size")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(cell_size_lbl)
                            .addComponent(self.cellsize_textfield))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(cell_size_lbl)
                          .addComponent(self.cellsize_textfield))
        self.cellsize_textfield.setMaximumSize(Dimension(100, 20))

        layout.linkSize(SwingConstants.HORIZONTAL, cell_size_lbl, rate_lbl)

        # Cell overhead
        cell_overhead_lbl = JLabel("Cell Overhead")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(cell_overhead_lbl)
                            .addComponent(self.celloverhead_textfield))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(cell_overhead_lbl)
                          .addComponent(self.celloverhead_textfield))
        self.celloverhead_textfield.setMaximumSize(Dimension(100, 20))

        layout.linkSize(SwingConstants.HORIZONTAL, cell_overhead_lbl, rate_lbl)


class Delay(JPanel):
    descr = "Add a Delay modification description here"
    title = "Delay Config"
    delay_time = JTextField()
    delay_jitter = JTextField()
    delay_jitter_correlation = JTextField()
    delay_distribution = None

    def __init__(self):
        TrafficMod.__init__(self, self.descr, self.title)
        self.setLayout(BoxLayout(self, BoxLayout.PAGE_AXIS))

        settings_panel = JPanel()
        layout = GroupLayout(settings_panel)
        layout.setAutoCreateGaps(True)
        layout.setAutoCreateContainerGaps(True)
        settings_panel.setLayout(layout)
        self.add(settings_panel)

        # Horizontal group
        horizontal = layout.createParallelGroup()
        layout.setHorizontalGroup(layout.createSequentialGroup().addGroup(horizontal))

        # Vertical group
        vertical = layout.createSequentialGroup()
        layout.setVerticalGroup(vertical)

        # Main title, label only
        main_title = JLabel("Rate Settings")
        main_title.setFont(Font(main_title.getFont().getName(), Font.BOLD, 14))
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(main_title))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(main_title))

        tc = TimeCombo()
        times_combo = tc.get_combo_box()

        # Base rate
        delay_lbl = JLabel("Delay")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(delay_lbl)
                            .addComponent(self.delay_time)
                            .addComponent(times_combo))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(delay_lbl)
                          .addComponent(self.delay_time)
                          .addComponent(times_combo))
        self.delay_time.setMaximumSize(Dimension(100, 20))


class Loss(JPanel):
    descr = "Add a Loss modification description here"
    title = "Loss Config"
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
        TrafficMod.__init__(self, self.descr, self.title)


class Corrupt(JPanel):
    descr = "Add a Corrupt modification description here"
    title = "Corrupt Config"
    corrupt_percent = None
    corrupt_percent_correlation = None

    def __init__(self):
        TrafficMod.__init__(self, self.descr, self.title)
        x = 0


class Duplicate(JPanel):
    descr = "Add a Duplicate modification description here"
    title = "Duplicate Config"
    duplicate_percent = None
    duplicate_percent_correlation = None

    def __init__(self):
        TrafficMod.__init__(self, self.descr, self.title)
        x = 0


class Reorder(JPanel):
    descr = "Add a Reorder modification description here"
    title = "Reorder Config"
    reorder_percent = None
    reorder_percent_correlation = None
    reorder_gap = None

    def __init__(self):
        TrafficMod.__init__(self, self.descr, self.title)
        x = 0;
