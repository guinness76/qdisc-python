from javax.swing import JLabel, JTextField, JPanel, BoxLayout, GroupLayout, SwingConstants, JComboBox, \
    DefaultComboBoxModel
from java.awt import Dimension, Component, Color, BorderLayout, Font
from javax.swing.border import LineBorder, TitledBorder
from java.lang import String
import components.bandwidth_combo as bandwidth_combo

from traffic_mod import TrafficMod


class Rate(TrafficMod):
    the_rate = None
    rate_descr = "Add a Rate modification description here"
    rate_textfield = JTextField()
    packet_textfield = JTextField()
    cellsize_textfield = JTextField()
    celloverhead_textfield = JTextField()

    def __init__(self):
        TrafficMod.__init__(self, self.rate_descr)
        self.setLayout(BoxLayout(self, BoxLayout.PAGE_AXIS))

        settings_panel = JPanel()
        # settings_panel.setBorder(TitledBorder(LineBorder(Color.darkGray), "Rate Settings"))
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

        # todo move this to a separate class
        bc = bandwidth_combo.BandwidthCombo()
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
