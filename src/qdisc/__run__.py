from java.awt import BorderLayout, Color, Dimension, FlowLayout, Component
from javax.swing import JFrame, JPanel, BoxLayout, JScrollPane, JLabel, JList, DefaultListModel, ListCellRenderer, \
    JButton, Box, BorderFactory
from javax.swing.border import LineBorder, TitledBorder
from traffic_mods.rate import Rate
from traffic_mods.filter import Filter


class MainFrame(JFrame):
    filter_list = JList()
    filter_list_model = DefaultListModel();

    def __init__(self):
        super(MainFrame, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setTitle("QDisc Configuration")

        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.setLocation(300, 100)
        self.setSize(1024, 768)
        # self.setExtendedState(JFrame.MAXIMIZED_BOTH)

        main_panel = JPanel()
        bl = BorderLayout()
        main_panel.setLayout(bl)
        self.setContentPane(main_panel)

        b = LineBorder(Color.darkGray)
        left_panel = JPanel()
        left_panel.setLayout(BoxLayout(left_panel, BoxLayout.Y_AXIS))
        main_panel.add(left_panel, BorderLayout.CENTER)

        filter_panel = self.build_filters_panel(b)
        left_panel.add(filter_panel)

        right_panel = JPanel()
        right_panel.setLayout(BoxLayout(right_panel, BoxLayout.Y_AXIS))
        main_panel.add(right_panel, BorderLayout.LINE_END)

        config_panel = self.build_trafficmod_panel(b)
        right_panel.add(config_panel)

        status_panel = self.build_status_panel(b)
        main_panel.add(status_panel, BorderLayout.PAGE_END);

        self.setVisible(True)

    def build_filters_panel(self, line_border):
        filter_panel = JPanel()
        bl = BorderLayout()
        filter_panel.setLayout(bl)

        ftb = TitledBorder(line_border, "Filters")
        filter_panel.setBorder(ftb)

        # todo temp
        test_filter = Filter()
        test_filter.src_addr = "127.0.0.1"
        test_filter.src_port = 8089
        # test_filter.print_filter()
        self.filter_list_model.addElement(test_filter)
        # todo end temp

        self.filter_list.setCellRenderer(self.FilterRenderer())

        self.filter_list.setModel(self.filter_list_model)
        filter_panel.add(self.filter_list, BorderLayout.CENTER)

        # Buttons to add or remove a filter
        add_remove_panel = JPanel()
        add_remove_panel.setLayout(BoxLayout(add_remove_panel, BoxLayout.PAGE_AXIS))

        add_remove_panel.add(Box.createRigidArea(Dimension(0, 10)))

        # todo add an action listener and a '+' icon
        add_btn = JButton("Add")
        # add_btn.setMinimumSize(Dimension(200, 30))
        # add_btn.setPreferredSize(Dimension(100, 30))
        add_btn.setAlignmentX(Component.CENTER_ALIGNMENT)
        add_remove_panel.add(add_btn)

        # add_remove_panel.add(Box.createRigidArea(Dimension(0, 10)))

        minSize = Dimension(100, 10)
        prefSize = Dimension(100, 10)
        maxSize = Dimension(100, 10)
        add_remove_panel.add(Box.Filler(minSize, prefSize, maxSize))

        # todo add an action listener and a '-' icon
        remove_btn = JButton("Remove")
        # remove_btn.setPreferredSize(Dimension(100, 30))
        remove_btn.setAlignmentX(Component.CENTER_ALIGNMENT)
        add_remove_panel.add(remove_btn)
        filter_panel.add(add_remove_panel, BorderLayout.EAST)

        # Buttons such as activate, unactivate, save and export
        file_actions_panel = JPanel()
        flow_layout = FlowLayout()
        flow_layout.setAlignment(FlowLayout.LEADING)
        file_actions_panel.setLayout(flow_layout)

        activate_btn = JButton("Activate")
        file_actions_panel.add(activate_btn)

        unactivate_btn = JButton("Unactivate")
        file_actions_panel.add(unactivate_btn)

        save_btn = JButton("Save")
        file_actions_panel.add(save_btn)

        export_btn = JButton("Export")
        file_actions_panel.add(export_btn)

        filter_panel.add(file_actions_panel, BorderLayout.SOUTH)

        return filter_panel

    def build_trafficmod_panel(self, line_border):
        config_panel = JPanel()
        config_panel.setLayout(BorderLayout())
        ctb = TitledBorder(line_border, "Traffic Modification")
        config_panel.setBorder(ctb)

        config_items = JPanel()
        config_items.setPreferredSize(Dimension(500, 600))
        config_items.setLayout(BoxLayout(config_items, BoxLayout.Y_AXIS))
        # pane = JScrollPane(config_items)
        # pane.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_NEVER)
        config_panel.add(config_items)

        rate_panel = Rate()
        rate_panel.setAlignmentX(Component.LEFT_ALIGNMENT)
        config_items.add(rate_panel)

        delay_panel = JPanel()
        delay_panel.setAlignmentX(Component.LEFT_ALIGNMENT)
        delay_panel.add(JLabel("Delay"))
        config_items.add(delay_panel)

        loss_panel = JPanel()
        loss_panel.setAlignmentX(Component.LEFT_ALIGNMENT)
        loss_panel.add(JLabel("Loss"))
        config_items.add(loss_panel)

        corrupt_panel = JPanel()
        corrupt_panel.setAlignmentX(Component.LEFT_ALIGNMENT)
        corrupt_panel.add(JLabel("Corrupt"))
        config_items.add(corrupt_panel)

        duplicate_panel = JPanel()
        duplicate_panel.setAlignmentX(Component.LEFT_ALIGNMENT)
        duplicate_panel.add(JLabel("Duplicate"))
        config_items.add(duplicate_panel)

        reorder_panel = JPanel()
        reorder_panel.setAlignmentX(Component.LEFT_ALIGNMENT)
        reorder_panel.add(JLabel("Reorder"))
        config_items.add(reorder_panel)

        return config_panel

    def build_status_panel(self, line_border):
        status_panel = JPanel()
        stb = TitledBorder(line_border, "Status")
        status_panel.setBorder(stb)

        status_panel.setLayout(BoxLayout(status_panel, BoxLayout.Y_AXIS))
        no_items_lbl = JLabel("No filters active")
        status_panel.add(no_items_lbl)

        return status_panel

    class FilterRenderer(ListCellRenderer):
        def getListCellRendererComponent(self, list, value, index, isSelected, cellHasFocus):
            # todo Change background color when object is selected
            return JLabel(value.print_filter())


if __name__ == '__main__':
    MainFrame()
