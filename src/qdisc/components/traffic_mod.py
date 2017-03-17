from java.awt import Dimension, Font
from javax.swing import JLabel, JTextField, JPanel, BoxLayout, GroupLayout, SwingConstants

import combo_boxes


class TrafficMod(JPanel):
    def __init__(self, descr, title):
        self.descr = descr


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
        self.horizontal_layout = horizontal

        # Vertical group
        vertical = layout.createSequentialGroup()
        layout.setVerticalGroup(vertical)
        self.vertical_layout = vertical

        # Main title, label only
        main_title = JLabel(self.title)
        main_title.setFont(Font(main_title.getFont().getName(), Font.BOLD, 14))
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(main_title))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(main_title))

        rates_combo = combo_boxes.get_rate_combo()
        # rates_combo.setMaximumSize(Dimension(100, 20))
        # rates_combo.addActionListener(self) todo implement listener?

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


class Delay(TrafficMod):
    descr = "Add a Delay modification description here"
    title = "Delay Config"
    delay_time = JTextField()
    times_combo = combo_boxes.get_time_combo()
    delay_deviation = JTextField()
    deviation_combo = combo_boxes.get_time_combo()
    delay_correlation = JTextField()
    distribution_combo = combo_boxes.get_delay_correlation_combo()

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
        main_title = JLabel(self.title)
        main_title.setFont(Font(main_title.getFont().getName(), Font.BOLD, 14))
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(main_title))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(main_title))

        # Base rate
        delay_lbl = JLabel("Delay")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(delay_lbl)
                            .addComponent(self.delay_time)
                            .addComponent(self.times_combo))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(delay_lbl)
                          .addComponent(self.delay_time)
                          .addComponent(self.times_combo))
        self.delay_time.setMaximumSize(Dimension(100, 20))

        # Deviation (jitter)


        deviation_lbl = JLabel("Deviation")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(deviation_lbl)
                            .addComponent(self.delay_deviation)
                            .addComponent(self.deviation_combo))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(deviation_lbl)
                          .addComponent(self.delay_deviation)
                          .addComponent(self.deviation_combo))
        self.delay_deviation.setMaximumSize(Dimension(100, 20))

        layout.linkSize(SwingConstants.HORIZONTAL, deviation_lbl, delay_lbl)

        # Correlation
        corr_lbl = JLabel("Correlation %")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(corr_lbl)
                            .addComponent(self.delay_correlation))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(corr_lbl)
                          .addComponent(self.delay_correlation))
        self.delay_correlation.setMaximumSize(Dimension(100, 20))

        layout.linkSize(SwingConstants.HORIZONTAL, corr_lbl, delay_lbl)

        # Distribution
        dist_lbl = JLabel("Distribution")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(dist_lbl)
                            .addComponent(self.distribution_combo))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(dist_lbl)
                          .addComponent(self.distribution_combo))

        layout.linkSize(SwingConstants.HORIZONTAL, dist_lbl, delay_lbl)



class Loss(TrafficMod):
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


class Corrupt(TrafficMod):
    descr = "Add a Corrupt modification description here"
    title = "Corrupt Config"
    corrupt_percent = None
    corrupt_percent_correlation = None

    def __init__(self):
        TrafficMod.__init__(self, self.descr, self.title)
        x = 0


class Duplicate(TrafficMod):
    descr = "Add a Duplicate modification description here"
    title = "Duplicate Config"
    duplicate_percent = None
    duplicate_percent_correlation = None

    def __init__(self):
        TrafficMod.__init__(self, self.descr, self.title)
        x = 0


class Reorder(TrafficMod):
    descr = "Add a Reorder modification description here"
    title = "Reorder Config"
    reorder_percent = None
    reorder_percent_correlation = None
    reorder_gap = None

    def __init__(self):
        TrafficMod.__init__(self, self.descr, self.title)
        x = 0;
