from java.awt import Dimension, Font
from java.awt.event import ActionListener
from javax.swing import JLabel, JTextField, JPanel, BoxLayout, GroupLayout, SwingConstants, JComboBox, \
    DefaultComboBoxModel

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
    loss_random_items = []
    loss_state_items = []
    loss_gemodel_items = []

    loss_type_combo = None
    loss_random_percent = JTextField()
    loss_random_percent_correlation = JTextField()

    loss_state_p13 = JTextField()
    loss_state_p31 = JTextField()
    loss_state_p32 = JTextField()
    loss_state_p23 = JTextField()
    loss_state_p14 = JTextField()

    loss_gemodel_p = JTextField()
    loss_gemodel_r = JTextField()
    loss_gemodel_h = JTextField()
    loss_gemodel_k = JTextField()

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

        # loss type (random, state, or gemodel)
        self.loss_type_combo = self.get_loss_type_combo()
        loss_type_lbl = JLabel("Loss type")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(loss_type_lbl)
                            .addComponent(self.loss_type_combo))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(loss_type_lbl)
                          .addComponent(self.loss_type_combo))

        # Random loss fields
        # Loss percentage
        loss_percent_lbl = JLabel("Loss %")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(loss_percent_lbl)
                            .addComponent(self.loss_random_percent))

        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(loss_percent_lbl)
                          .addComponent(self.loss_random_percent))

        self.loss_random_percent.setMaximumSize(Dimension(100, 20))
        layout.linkSize(SwingConstants.HORIZONTAL, loss_percent_lbl, loss_type_lbl)
        self.loss_random_items.append(loss_percent_lbl)
        self.loss_random_items.append(self.loss_random_percent)

        # Loss percent correlation
        loss_corr_lbl = JLabel("Correlation %")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(loss_corr_lbl)
                            .addComponent(self.loss_random_percent_correlation))

        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(loss_corr_lbl)
                          .addComponent(self.loss_random_percent_correlation))

        self.loss_random_percent_correlation.setMaximumSize(Dimension(100, 20))
        layout.linkSize(SwingConstants.HORIZONTAL, loss_corr_lbl, loss_type_lbl)
        self.loss_random_items.append(self.loss_random_percent_correlation)

        # State loss fields
        # P13
        loss_p13_lbl = JLabel("P13")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(loss_p13_lbl)
                            .addComponent(self.loss_state_p13))

        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(loss_p13_lbl)
                          .addComponent(self.loss_state_p13))
        self.loss_state_p13.setMaximumSize(Dimension(100, 20))
        self.loss_state_items.append(loss_p13_lbl)
        self.loss_state_items.append(self.loss_state_p13)

        # P31
        loss_p31_lbl = JLabel("P31")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(loss_p31_lbl)
                            .addComponent(self.loss_state_p31))

        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(loss_p31_lbl)
                          .addComponent(self.loss_state_p31))
        self.loss_state_p31.setMaximumSize(Dimension(100, 20))
        layout.linkSize(SwingConstants.HORIZONTAL, loss_p31_lbl, loss_p13_lbl)
        self.loss_state_items.append(loss_p31_lbl)
        self.loss_state_items.append(self.loss_state_p31)

        # P32
        loss_p32_lbl = JLabel("P32")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(loss_p32_lbl)
                            .addComponent(self.loss_state_p32))

        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(loss_p32_lbl)
                          .addComponent(self.loss_state_p32))
        self.loss_state_p32.setMaximumSize(Dimension(100, 20))
        layout.linkSize(SwingConstants.HORIZONTAL, loss_p32_lbl, loss_p13_lbl)
        self.loss_state_items.append(loss_p32_lbl)
        self.loss_state_items.append(self.loss_state_p32)

        # P23
        loss_p23_lbl = JLabel("P23")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(loss_p23_lbl)
                            .addComponent(self.loss_state_p23))

        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(loss_p23_lbl)
                          .addComponent(self.loss_state_p23))
        self.loss_state_p23.setMaximumSize(Dimension(100, 20))
        layout.linkSize(SwingConstants.HORIZONTAL, loss_p23_lbl, loss_p13_lbl)
        self.loss_state_items.append(loss_p23_lbl)
        self.loss_state_items.append(self.loss_state_p23)

        # P14
        loss_p14_lbl = JLabel("P14")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(loss_p14_lbl)
                            .addComponent(self.loss_state_p14))

        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(loss_p14_lbl)
                          .addComponent(self.loss_state_p14))
        self.loss_state_p14.setMaximumSize(Dimension(100, 20))
        layout.linkSize(SwingConstants.HORIZONTAL, loss_p14_lbl, loss_p13_lbl)
        self.loss_state_items.append(loss_p14_lbl)
        self.loss_state_items.append(self.loss_state_p14)

        # Gemodel loss fields
        # P
        ge_p_lbl = JLabel("p")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(ge_p_lbl)
                            .addComponent(self.loss_gemodel_p))

        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(ge_p_lbl)
                          .addComponent(self.loss_gemodel_p))
        self.loss_gemodel_p.setMaximumSize(Dimension(100, 20))
        self.loss_gemodel_items.append(ge_p_lbl)
        self.loss_gemodel_items.append(self.loss_gemodel_p)

        # R
        ge_r_lbl = JLabel("r")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(ge_r_lbl)
                            .addComponent(self.loss_gemodel_r))

        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(ge_r_lbl)
                          .addComponent(self.loss_gemodel_r))
        self.loss_gemodel_r.setMaximumSize(Dimension(100, 20))
        layout.linkSize(SwingConstants.HORIZONTAL, ge_r_lbl, ge_p_lbl)
        self.loss_gemodel_items.append(ge_r_lbl)
        self.loss_gemodel_items.append(self.loss_gemodel_r)

        # H
        ge_h_lbl = JLabel("1-h")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(ge_h_lbl)
                            .addComponent(self.loss_gemodel_h))

        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(ge_h_lbl)
                          .addComponent(self.loss_gemodel_h))
        self.loss_gemodel_h.setMaximumSize(Dimension(100, 20))
        layout.linkSize(SwingConstants.HORIZONTAL, ge_h_lbl, ge_p_lbl)
        self.loss_gemodel_items.append(ge_h_lbl)
        self.loss_gemodel_items.append(self.loss_gemodel_h)

        # K
        ge_k_lbl = JLabel("1-k")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(ge_k_lbl)
                            .addComponent(self.loss_gemodel_k))

        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(ge_k_lbl)
                          .addComponent(self.loss_gemodel_k))
        self.loss_gemodel_k.setMaximumSize(Dimension(100, 20))
        layout.linkSize(SwingConstants.HORIZONTAL, ge_k_lbl, ge_p_lbl)
        self.loss_gemodel_items.append(ge_k_lbl)
        self.loss_gemodel_items.append(self.loss_gemodel_k)

        # Initially show the loss_random textboxes
        for item in self.loss_random_items:
            item.setVisible(True)

        for item in self.loss_state_items:
            item.setVisible(False)

        for item in self.loss_gemodel_items:
            item.setVisible(False)

    def get_loss_type_combo(self):
        combo_box = JComboBox()
        combo_model = DefaultComboBoxModel()
        combo_model.addElement("random")
        combo_model.addElement("state")
        combo_model.addElement("gemodel")
        combo_box.setModel(combo_model)
        combo_box.setMaximumSize(Dimension(120, 20))

        combo_box.addActionListener(
            self.MyListener(self.loss_random_items, self.loss_state_items, self.loss_gemodel_items))
        return combo_box

    class MyListener(ActionListener):

        loss_random_items = []
        loss_state_items = []
        loss_gemodel_items = []

        def __init__(self, loss_random_items, loss_state_items, loss_gemodel_items):
            self.loss_random_items = loss_random_items
            self.loss_state_items = loss_state_items
            self.loss_gemodel_items = loss_gemodel_items

        def actionPerformed(self, event):
            combo_box = event.getSource()
            selected = str(combo_box.getSelectedItem())

            # todo clear out values of the textboxes being hidden
            if (selected == "random"):
                for item in self.loss_random_items:
                    item.setVisible(True)

                for item in self.loss_state_items:
                    item.setVisible(False)

                for item in self.loss_gemodel_items:
                    item.setVisible(False)

            elif (selected == "state"):
                for item in self.loss_random_items:
                    item.setVisible(False)

                for item in self.loss_state_items:
                    item.setVisible(True)

                for item in self.loss_gemodel_items:
                    item.setVisible(False)

            elif (selected == "gemodel"):
                for item in self.loss_random_items:
                    item.setVisible(False)

                for item in self.loss_state_items:
                    item.setVisible(False)

                for item in self.loss_gemodel_items:
                    item.setVisible(True)


class Corrupt(TrafficMod):
    descr = "Add a Corrupt modification description here"
    title = "Corrupt Config"
    corrupt_percent = None
    corrupt_percent_correlation = None

    def __init__(self):
        TrafficMod.__init__(self, self.descr, self.title)


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
