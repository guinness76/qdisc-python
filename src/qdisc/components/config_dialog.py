from java.awt import Dimension, Font, BorderLayout, Component, Color, FlowLayout
from java.awt.event import ActionListener
from javax.swing import JLabel, JTextField, JPanel, BoxLayout, GroupLayout, SwingConstants, JComboBox, \
    DefaultComboBoxModel, JList, DefaultListModel, JButton, JOptionPane
from javax.swing.border import EmptyBorder

import ui_components
import datamodel
from ui_components import get_title_font


class TrafficMod(JPanel):
    is_selected = False
    max_x = 1024 - 200
    max_y = 350

    def __init__(self):
        pass
        # self.setMaximumSize(Dimension(self.max_x, self.max_y))  # todo pass in sizes from parent

    def set_selected(self, is_selected):
        self.is_selected = is_selected
        self.setVisible(is_selected)


class ProfilePropsConfig(TrafficMod):
    descr = "Add a profile property description here"
    title = "Profile Properties"
    name_textfield = JTextField()
    descr_textarea = ui_components.get_setting_textarea()

    def __init__(self):
        TrafficMod.__init__(self)
        self.setLayout(BorderLayout())

        settings_panel = JPanel()
        # settings_panel.setBorder(LineBorder(Color.RED))
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
        main_title.setFont(get_title_font(main_title))
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(main_title))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(main_title))

        # Profile name
        name_lbl = JLabel("Profile Name")
        name_lbl.setToolTipText("The name of this profile")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(name_lbl)
                            .addComponent(self.name_textfield))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(name_lbl)
                          .addComponent(self.name_textfield))

        # Profile description
        descr_lbl = JLabel("Description")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(descr_lbl)
                            .addComponent(self.descr_textarea))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(descr_lbl)
                          .addComponent(self.descr_textarea))

        layout.linkSize(SwingConstants.HORIZONTAL, name_lbl, descr_lbl)


class FiltersConfig(TrafficMod):
    descr = "Add a Filter description here"
    title = "Filters"
    filter_list = JList()
    filter_list_model = DefaultListModel()

    def __init__(self):
        TrafficMod.__init__(self)
        self.setLayout(BorderLayout())
        self.setBorder(EmptyBorder(18, 18, 18, 18))

        main_title = JLabel(self.title)
        main_title.setFont(get_title_font(main_title))
        self.add(main_title, BorderLayout.PAGE_START)

        self.filter_list.setCellRenderer(ui_components.FilterRenderer())
        self.filter_list.setModel(self.filter_list_model)
        self.add(self.filter_list, BorderLayout.CENTER)

        # Buttons to add or remove a filter
        add_remove_panel = JPanel()
        add_remove_panel.setLayout(FlowLayout(FlowLayout.LEADING))
        # add_remove_panel.setBorder(EmptyBorder(10, 10, 10, 10))
        # add_remove_panel.setBorder(LineBorder(Color.RED))
        # add_remove_panel.setLayout(BoxLayout(add_remove_panel, BoxLayout.X_AXIS))

        # add_remove_panel.add(Box.createRigidArea(Dimension(0, 10)))

        # Edit Filter button
        edit_filter_panel = self.edit_filter_panel()

        def edit_filter(event):
            # TODO Set the properties on the edit filter based on the passed event
            result = JOptionPane.showConfirmDialog(self, edit_filter_panel, "Edit Filter", JOptionPane.OK_CANCEL_OPTION,
                                                   JOptionPane.PLAIN_MESSAGE)
            if result == 0:
                print "Will save filter"

        edit_btn = JButton("Edit", actionPerformed=edit_filter)
        edit_btn.setEnabled(False)
        add_remove_panel.add(edit_btn)

        # Add Filter button
        def add_filter(event):
            result = JOptionPane.showConfirmDialog(self, edit_filter_panel, "Add Filter", JOptionPane.OK_CANCEL_OPTION,
                                                   JOptionPane.PLAIN_MESSAGE)
            if result == 0:
                print "Will save new filter"

        add_btn = JButton("Add", actionPerformed=add_filter)

        # add_btn.setMinimumSize(Dimension(200, 30))
        # add_btn.setPreferredSize(Dimension(100, 30))
        # add_btn.setAlignmentX(Component.CENTER_ALIGNMENT)
        add_remove_panel.add(add_btn)

        # add_remove_panel.add(Box.createRigidArea(Dimension(0, 10)))

        # minSize = Dimension(100, 10)
        # prefSize = Dimension(100, 10)
        # maxSize = Dimension(100, 10)
        # add_remove_panel.add(Box.Filler(minSize, prefSize, maxSize))

        # todo add an action listener
        remove_btn = JButton("Remove")
        remove_btn.setEnabled(False)
        # remove_btn.setAlignmentX(Component.CENTER_ALIGNMENT)
        add_remove_panel.add(remove_btn)
        self.add(add_remove_panel, BorderLayout.PAGE_END)

    def edit_filter_panel(self):
        edit_panel = JPanel()
        layout = GroupLayout(edit_panel)
        layout.setAutoCreateGaps(True)
        # layout.setAutoCreateContainerGaps(True)
        edit_panel.setLayout(layout)

        # Horizontal group
        horizontal = layout.createParallelGroup()
        layout.setHorizontalGroup(layout.createSequentialGroup().addGroup(horizontal))

        # Vertical group
        vertical = layout.createSequentialGroup()
        layout.setVerticalGroup(vertical)

        # Main title, label only
        # main_title = JLabel(self.title)
        # main_title.setFont(get_title_font(main_title))
        # horizontal.addGroup(layout.createSequentialGroup()
        #                     .addComponent(main_title))
        # vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
        #                   .addComponent(main_title))

        # Packet source IP address
        src_ip_lbl = JLabel("Source IP Addr")
        src_ip_fld = JTextField()
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(src_ip_lbl)
                            .addComponent(src_ip_fld))

        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(src_ip_lbl)
                          .addComponent(src_ip_fld))

        # Packet source port
        src_port_lbl = JLabel("Source Port")
        src_port_fld = JTextField()
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(src_port_lbl)
                            .addComponent(src_port_fld))

        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(src_port_lbl)
                          .addComponent(src_port_fld))
        layout.linkSize(SwingConstants.HORIZONTAL, src_port_lbl, src_ip_lbl)

        # Packet destination IP address
        dest_ip_lbl = JLabel("Destination IP Addr")
        dest_ip_fld = JTextField()
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(dest_ip_lbl)
                            .addComponent(dest_ip_fld))

        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(dest_ip_lbl)
                          .addComponent(dest_ip_fld))
        layout.linkSize(SwingConstants.HORIZONTAL, dest_ip_lbl, src_ip_lbl)

        # Packet destination port
        dest_port_lbl = JLabel("Destination Port")
        dest_port_fld = JTextField()
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(dest_port_lbl)
                            .addComponent(dest_port_fld))

        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(dest_port_lbl)
                          .addComponent(dest_port_fld))
        layout.linkSize(SwingConstants.HORIZONTAL, dest_port_lbl, src_ip_lbl)

        return edit_panel


class RateConfig(TrafficMod):
    descr = "Add a Rate modification description here"
    title = "Rate Config"
    rate_textfield = ui_components.get_setting_textfield()
    packet_textfield = ui_components.get_setting_textfield()
    cellsize_textfield = ui_components.get_setting_textfield()
    celloverhead_textfield = ui_components.get_setting_textfield()

    def __init__(self):
        TrafficMod.__init__(self)
        self.setLayout(FlowLayout(FlowLayout.LEADING))

        settings_panel = JPanel()
        # settings_panel.setBorder(LineBorder(Color.RED))
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
        main_title.setFont(get_title_font(main_title))
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(main_title))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(main_title))

        rates_combo = ui_components.get_rate_combo()

        # Base rate
        rate_lbl = JLabel("Rate")
        rate_lbl.setToolTipText("Simulates a network connector with a limited throughput")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(rate_lbl)
                            .addComponent(self.rate_textfield)
                            .addComponent(rates_combo))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(rate_lbl)
                          .addComponent(self.rate_textfield)
                          .addComponent(rates_combo))

        # Packet overhead
        packet_overhead_lbl = JLabel("Packet Overhead")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(packet_overhead_lbl)
                            .addComponent(self.packet_textfield))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(packet_overhead_lbl)
                          .addComponent(self.packet_textfield))

        layout.linkSize(SwingConstants.HORIZONTAL, packet_overhead_lbl, rate_lbl)

        # Cell size
        cell_size_lbl = JLabel("Cell Size")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(cell_size_lbl)
                            .addComponent(self.cellsize_textfield))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(cell_size_lbl)
                          .addComponent(self.cellsize_textfield))

        layout.linkSize(SwingConstants.HORIZONTAL, cell_size_lbl, rate_lbl)

        # Cell overhead
        cell_overhead_lbl = JLabel("Cell Overhead")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(cell_overhead_lbl)
                            .addComponent(self.celloverhead_textfield))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(cell_overhead_lbl)
                          .addComponent(self.celloverhead_textfield))

        layout.linkSize(SwingConstants.HORIZONTAL, cell_overhead_lbl, rate_lbl)


class DelayConfig(TrafficMod):
    descr = "Add a Delay modification description here"
    title = "Delay Config"
    delay_time = ui_components.get_setting_textfield()
    times_combo = ui_components.get_time_combo()
    delay_deviation = ui_components.get_setting_textfield()
    deviation_combo = ui_components.get_time_combo()
    delay_correlation = ui_components.get_setting_textfield()
    distribution_combo = ui_components.get_delay_correlation_combo()

    def __init__(self):
        TrafficMod.__init__(self)
        self.setLayout(FlowLayout(FlowLayout.LEADING))

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
        main_title.setFont(get_title_font(main_title))
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

        layout.linkSize(SwingConstants.HORIZONTAL, deviation_lbl, delay_lbl)

        # Correlation
        corr_lbl = JLabel("Correlation %")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(corr_lbl)
                            .addComponent(self.delay_correlation))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(corr_lbl)
                          .addComponent(self.delay_correlation))

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


class LossConfig(TrafficMod):
    descr = "Add a Loss modification description here"
    title = "Loss Config"
    loss_random_items = []
    loss_state_items = []
    loss_gemodel_items = []

    loss_type_combo = None
    loss_random_percent = ui_components.get_setting_textfield()
    loss_random_percent_correlation = ui_components.get_setting_textfield()

    loss_state_p13 = ui_components.get_setting_textfield()
    loss_state_p31 = ui_components.get_setting_textfield()
    loss_state_p32 = ui_components.get_setting_textfield()
    loss_state_p23 = ui_components.get_setting_textfield()
    loss_state_p14 = ui_components.get_setting_textfield()

    loss_gemodel_p = ui_components.get_setting_textfield()
    loss_gemodel_r = ui_components.get_setting_textfield()
    loss_gemodel_h = ui_components.get_setting_textfield()
    loss_gemodel_k = ui_components.get_setting_textfield()

    def __init__(self):
        TrafficMod.__init__(self)
        self.setLayout(FlowLayout(FlowLayout.LEADING))

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
        main_title.setFont(get_title_font(main_title))
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

        layout.linkSize(SwingConstants.HORIZONTAL, loss_corr_lbl, loss_type_lbl)
        self.loss_random_items.append(loss_corr_lbl)
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
            self.ComboListener(self.loss_random_items, self.loss_state_items, self.loss_gemodel_items))
        return combo_box

    class ComboListener(ActionListener):

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
            if selected == "random":
                for item in self.loss_random_items:
                    item.setVisible(True)

                for item in self.loss_state_items:
                    item.setVisible(False)

                for item in self.loss_gemodel_items:
                    item.setVisible(False)

            elif selected == "state":
                for item in self.loss_random_items:
                    item.setVisible(False)

                for item in self.loss_state_items:
                    item.setVisible(True)

                for item in self.loss_gemodel_items:
                    item.setVisible(False)

            elif selected == "gemodel":
                for item in self.loss_random_items:
                    item.setVisible(False)

                for item in self.loss_state_items:
                    item.setVisible(False)

                for item in self.loss_gemodel_items:
                    item.setVisible(True)


class CorruptConfig(TrafficMod):
    descr = "Add a Corrupt modification description here"
    title = "Corrupt Config"
    corrupt_percent = ui_components.get_setting_textfield()
    corrupt_percent_correlation = ui_components.get_setting_textfield()

    def __init__(self):
        TrafficMod.__init__(self)
        self.setLayout(FlowLayout(FlowLayout.LEADING))

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
        main_title.setFont(get_title_font(main_title))
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(main_title))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(main_title))

        # Corrupt percentage
        percent_lbl = JLabel("Corrupt %")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(percent_lbl)
                            .addComponent(self.corrupt_percent))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(percent_lbl)
                          .addComponent(self.corrupt_percent))

        # Corrupt percentage correlation
        corr_lbl = JLabel("Correlation %")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(corr_lbl)
                            .addComponent(self.corrupt_percent_correlation))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(corr_lbl)
                          .addComponent(self.corrupt_percent_correlation))

        layout.linkSize(SwingConstants.HORIZONTAL, corr_lbl, percent_lbl)


class DuplicateConfig(TrafficMod):
    descr = "Add a Duplicate modification description here"
    title = "Duplicate Config"
    duplicate_percent = ui_components.get_setting_textfield()
    duplicate_percent_correlation = ui_components.get_setting_textfield()

    def __init__(self):
        TrafficMod.__init__(self)
        self.setLayout(FlowLayout(FlowLayout.LEADING))

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

        # Duplicate percentage
        percent_lbl = JLabel("Duplicate %")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(percent_lbl)
                            .addComponent(self.duplicate_percent))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(percent_lbl)
                          .addComponent(self.duplicate_percent))

        # Duplicate percentage correlation
        corr_lbl = JLabel("Correlation %")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(corr_lbl)
                            .addComponent(self.duplicate_percent_correlation))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(corr_lbl)
                          .addComponent(self.duplicate_percent_correlation))

        layout.linkSize(SwingConstants.HORIZONTAL, corr_lbl, percent_lbl)


class ReorderConfig(TrafficMod):
    descr = "Add a Reorder modification description here"
    title = "Reorder Config"
    reorder_percent = ui_components.get_setting_textfield()
    reorder_percent_correlation = ui_components.get_setting_textfield()
    reorder_gap = ui_components.get_setting_textfield()

    def __init__(self):
        TrafficMod.__init__(self)
        self.setLayout(FlowLayout(FlowLayout.LEADING))

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
        main_title.setFont(get_title_font(main_title))
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(main_title))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(main_title))

        # Reorder percentage
        percent_lbl = JLabel("Reorder %")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(percent_lbl)
                            .addComponent(self.reorder_percent))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(percent_lbl)
                          .addComponent(self.reorder_percent))

        # Reorder percentage correlation
        corr_lbl = JLabel("Correlation %")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(corr_lbl)
                            .addComponent(self.reorder_percent_correlation))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(corr_lbl)
                          .addComponent(self.reorder_percent_correlation))

        layout.linkSize(SwingConstants.HORIZONTAL, corr_lbl, percent_lbl)

        # Reorder gap
        gap_lbl = JLabel("Gap")
        horizontal.addGroup(layout.createSequentialGroup()
                            .addComponent(gap_lbl)
                            .addComponent(self.reorder_gap))
        vertical.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                          .addComponent(gap_lbl)
                          .addComponent(self.reorder_gap))

        layout.linkSize(SwingConstants.HORIZONTAL, gap_lbl, percent_lbl)
