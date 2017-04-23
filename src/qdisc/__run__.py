from java.awt import BorderLayout, Color, Dimension, FlowLayout, Component
from java.awt.event import MouseAdapter
from javax.swing import JFrame, JPanel, BoxLayout, JLabel, JList, DefaultListModel, \
    JButton, Box
from javax.swing.border import LineBorder, TitledBorder

from components import traffic_options, components


class MainFrame(JFrame):
    menu_panel = None

    def __init__(self):
        super(MainFrame, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setTitle("QDisc Edit Profile")

        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.setLocation(300, 100)
        self.setSize(1024, 768)
        # self.setExtendedState(JFrame.MAXIMIZED_BOTH)

        main_panel = JPanel()
        bl = BorderLayout()
        main_panel.setLayout(bl)
        self.setContentPane(main_panel)
        b = LineBorder(Color.darkGray)

        # left_panel = JPanel()
        # left_panel.setLayout(BoxLayout(left_panel, BoxLayout.Y_AXIS))
        # main_panel.add(left_panel, BorderLayout.CENTER)

        self.build_panels(main_panel)

        # filter_panel = self.build_filters_panel(b)
        # left_panel.add(filter_panel)

        # right_panel = JPanel()
        # right_panel.setLayout(BoxLayout(right_panel, BoxLayout.Y_AXIS))
        # main_panel.add(right_panel, BorderLayout.CENTER)

        # config_panel = self.build_trafficmod_panel(b)
        # right_panel.add(config_panel)
        #
        # status_panel = self.build_status_panel(b)
        # main_panel.add(status_panel, BorderLayout.PAGE_END)

        self.setVisible(True)

    def show_panel(self, menu_item):
        for component in self.menu_panel.getComponents():
            if isinstance(component, components.MenuItem):
                component.set_selected(False)

        menu_item.set_selected(True)

    class MenuMouseListener(MouseAdapter):

        main_frame = None

        def __init__(self, main_frame):
            self.main_frame = main_frame

        def mousePressed(self, event):
            self.main_frame.show_panel(event.getSource())

    def handle_click(self, event):
        pass

    # if self.task is not None:
    # self.task.cancel()

    def build_panels(self, main_panel):
        self.menu_panel = JPanel()
        self.menu_panel.setLayout(BoxLayout(self.menu_panel, BoxLayout.Y_AXIS))
        self.menu_panel.setPreferredSize(Dimension(200, 200))
        main_panel.add(self.menu_panel, BorderLayout.LINE_START)

        config_panel = JPanel()
        config_panel.setPreferredSize(Dimension(500, 600))
        config_panel.setLayout(BoxLayout(config_panel, BoxLayout.Y_AXIS))
        main_panel.add(config_panel, BorderLayout.CENTER)

        filters_panel = traffic_options.Filters()
        filters_menu_item = components.MenuItem("Filters", filters_panel)
        filters_menu_item.addMouseListener(self.MenuMouseListener(self))

        self.menu_panel.add(filters_menu_item)
        config_panel.add(filters_panel)

        rate_panel = traffic_options.Rate()
        rate_menu_item = components.MenuItem("Rate", rate_panel)
        rate_menu_item.addMouseListener(self.MenuMouseListener(self))
        self.menu_panel.add(rate_menu_item)
        config_panel.add(rate_panel)

        delay_panel = traffic_options.Delay()
        delay_menu_item = components.MenuItem("Delay", delay_panel)
        delay_menu_item.addMouseListener(self.MenuMouseListener(self))
        self.menu_panel.add(delay_menu_item)
        config_panel.add(delay_panel)

        loss_panel = traffic_options.Loss()
        loss_menu_item = components.MenuItem("Loss", loss_panel)
        loss_menu_item.addMouseListener(self.MenuMouseListener(self))
        self.menu_panel.add(loss_menu_item)
        config_panel.add(loss_panel)

        corrupt_panel = traffic_options.Corrupt()
        corrupt_menu_item = components.MenuItem("Corrupt", corrupt_panel)
        corrupt_menu_item.addMouseListener(self.MenuMouseListener(self))
        self.menu_panel.add(corrupt_menu_item)
        config_panel.add(corrupt_panel)

        duplicate_panel = traffic_options.Duplicate()
        duplicate_menu_item = components.MenuItem("Duplicate", duplicate_panel)
        duplicate_menu_item.addMouseListener(self.MenuMouseListener(self))
        self.menu_panel.add(duplicate_menu_item)
        config_panel.add(duplicate_panel)

        reorder_panel = traffic_options.Reorder()
        reorder_menu_item = components.MenuItem("Reorder", reorder_panel)
        reorder_menu_item.addMouseListener(self.MenuMouseListener(self))
        self.menu_panel.add(reorder_menu_item)
        config_panel.add(reorder_panel)

        # todo temp
        filters_panel.set_selected(True)


if __name__ == '__main__':
    MainFrame()
