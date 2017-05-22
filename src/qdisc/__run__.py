from java.awt import BorderLayout, Color, Dimension, FlowLayout, Component
from java.awt.event import MouseAdapter, ActionListener
from javax.swing import JFrame, JPanel, BoxLayout, JLabel, JTable, JButton, JOptionPane, JScrollPane, JComboBox, \
    DefaultCellEditor
from javax.swing.table import AbstractTableModel, TableColumn, DefaultTableCellRenderer, TableCellRenderer
from javax.swing.border import LineBorder, TitledBorder
from java.lang import String

from components import config_dialog, ui_components
from components.datamodel import Profile, Filter, Rate, Loss, Delay, Corrupt, Duplicate, Reorder


class MainFrame(JFrame):
    menu_panel = None
    profile_table = None
    profile_table_model = None

    def __init__(self):
        super(MainFrame, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setTitle("QDisc Edit Profile")

        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.setLocation(250, 100)
        self.setSize(1024, 400)
        # self.setExtendedState(JFrame.MAXIMIZED_BOTH)
        main_panel = JPanel()
        main_panel.setLayout(BorderLayout())
        self.setContentPane(main_panel)

        # Build the config dialog first, so it can be attached to the Edit button
        config_dialog = JPanel()
        config_dialog.setLayout(BorderLayout())
        self.build_panels(config_dialog)

        def show_config_dialog(event):
            result = JOptionPane.showConfirmDialog(self, config_dialog, "Edit Profile", JOptionPane.OK_CANCEL_OPTION,
                                                   JOptionPane.PLAIN_MESSAGE)
            if result == 0:
                print "Will save results"

        top_panel = JPanel()
        top_panel.setLayout(FlowLayout(FlowLayout.LEADING))
        title_lbl = JLabel("TODO Set title")
        title_lbl.setFont(ui_components.get_title_font(title_lbl))
        top_panel.add(title_lbl)
        main_panel.add(top_panel, BorderLayout.PAGE_START)

        self.profile_table = self.initProfilesTable()
        scrollPane = JScrollPane(self.profile_table);
        main_panel.add(scrollPane, BorderLayout.CENTER)
        # self.profile_list.setCellRenderer(ui_components.FilterRenderer())

        buttons_panel = JPanel()
        buttons_panel.setLayout(FlowLayout(FlowLayout.LEADING))
        main_panel.add(buttons_panel, BorderLayout.PAGE_END)

        edit_profile_btn = JButton("Edit", actionPerformed=show_config_dialog)
        buttons_panel.add(edit_profile_btn)

        # status_panel = self.build_status_panel(b)
        # main_panel.add(status_panel, BorderLayout.PAGE_END)

        self.setVisible(True)

    # For the config dialog
    def show_panel(self, menu_item):
        for component in self.menu_panel.getComponents():
            if isinstance(component, ui_components.MenuItem):
                component.set_selected(False)

        menu_item.set_selected(True)

    def build_panels(self, the_dialog):
        self.menu_panel = JPanel()
        self.menu_panel.setLayout(BoxLayout(self.menu_panel, BoxLayout.Y_AXIS))
        self.menu_panel.setPreferredSize(Dimension(200, 200))
        the_dialog.add(self.menu_panel, BorderLayout.LINE_START)

        config_panel = JPanel()
        config_panel.setPreferredSize(Dimension(500, 600))
        config_panel.setLayout(BoxLayout(config_panel, BoxLayout.Y_AXIS))
        the_dialog.add(config_panel, BorderLayout.CENTER)

        # Profile properties
        profile_props_panel = config_dialog.ProfilePropsConfig()
        profile_props_menu_item = ui_components.MenuItem("Profile Properties", profile_props_panel)
        profile_props_menu_item.addMouseListener(self.MenuMouseListener(self))
        self.menu_panel.add(profile_props_menu_item)
        config_panel.add(profile_props_panel)

        # Filters
        filters_panel = config_dialog.FiltersConfig()
        filters_menu_item = ui_components.MenuItem("Filters", filters_panel)
        filters_menu_item.addMouseListener(self.MenuMouseListener(self))
        self.menu_panel.add(filters_menu_item)
        config_panel.add(filters_panel)

        # Rate control
        rate_panel = config_dialog.RateConfig()
        rate_menu_item = ui_components.MenuItem("Rate", rate_panel)
        rate_menu_item.addMouseListener(self.MenuMouseListener(self))
        self.menu_panel.add(rate_menu_item)
        config_panel.add(rate_panel)

        # Delay control
        delay_panel = config_dialog.DelayConfig()
        delay_menu_item = ui_components.MenuItem("Delay", delay_panel)
        delay_menu_item.addMouseListener(self.MenuMouseListener(self))
        self.menu_panel.add(delay_menu_item)
        config_panel.add(delay_panel)

        # Loss control
        loss_panel = config_dialog.LossConfig()
        loss_menu_item = ui_components.MenuItem("Loss", loss_panel)
        loss_menu_item.addMouseListener(self.MenuMouseListener(self))
        self.menu_panel.add(loss_menu_item)
        config_panel.add(loss_panel)

        # Corruption control
        corrupt_panel = config_dialog.CorruptConfig()
        corrupt_menu_item = ui_components.MenuItem("Corrupt", corrupt_panel)
        corrupt_menu_item.addMouseListener(self.MenuMouseListener(self))
        self.menu_panel.add(corrupt_menu_item)
        config_panel.add(corrupt_panel)

        # Duplication control
        duplicate_panel = config_dialog.DuplicateConfig()
        duplicate_menu_item = ui_components.MenuItem("Duplicate", duplicate_panel)
        duplicate_menu_item.addMouseListener(self.MenuMouseListener(self))
        self.menu_panel.add(duplicate_menu_item)
        config_panel.add(duplicate_panel)

        # Reorder control
        reorder_panel = config_dialog.ReorderConfig()
        reorder_menu_item = ui_components.MenuItem("Reorder", reorder_panel)
        reorder_menu_item.addMouseListener(self.MenuMouseListener(self))
        self.menu_panel.add(reorder_menu_item)
        config_panel.add(reorder_panel)

        # Default selection
        profile_props_panel.set_selected(True)

    def initProfilesTable(self):
        profile_table = JTable()

        self.profile_table_model = self.ProfileTableModel()
        profile_table.setModel(self.profile_table_model)

        cm = profile_table.getColumnModel()
        # Set column widths
        for i in range(0, 4):
            width = self.profile_table_model.column_widths.get(i)
            if width is not None:
                column = cm.getColumn(i)
                column.setPreferredWidth(width)
                column.setMaxWidth(width)

        profile_table.setFillsViewportHeight(True);

        def doAction(event):
            print event

        # Add the actions dropdown
        actionCol = cm.getColumn(3)
        actions = JComboBox()
        actions.addItem("Activate")
        actions.addItem("Unactivate")
        actions.addItem("Edit")
        actions.addItem("Export")
        actions.addItem("Delete")
        actionCol.setCellEditor(DefaultCellEditor(actions))
        self.profile_table_model.actions_combo = actions

        renderer = self.ComboBoxTableCellRenderer()
        actionCol.setCellRenderer(renderer)

        actions.addActionListener(self.ComboActionListener(self))

        return profile_table

    class ComboActionListener(ActionListener):
        main_frame = None

        def __init__(self, main_frame):
            self.main_frame = main_frame

        def actionPerformed(self, event):
            if event.getSource().getSelectedIndex() > -1:
                print event.getSource().getSelectedItem()

    class ProfileTableModel(AbstractTableModel):

        columns = ["Name", "Is Active", "Description", "Actions"]
        column_widths = {
            0: 200,
            1: 100,
            2: None,
            3: 200
        }
        profiles = []
        actions_combo = None

        def __init__(self):
            # todo temp Load the profiles here
            profile = Profile()
            profile.profile_name = "Test profile"
            profile.profile_descr = "Description for the test profile"

            test_filter = Filter()
            test_filter.src_addr = "127.0.0.1"
            test_filter.src_port = 8089
            profile.filters.append(test_filter)

            self.profiles.append(profile)
            # todo end temp

        def getRowCount(self):
            return len(self.profiles)

        def getColumnCount(self):
            return len(self.columns)

        def getColumnName(self, columnIndex):
            return self.columns[columnIndex]

        # Needed to display something other than plain text in the cell
        def getColumnClass(self, column):
            # return [String, String, String, JComboBox][column]

            if column == 3:
                print self.actions_combo.getClass()
                return self.actions_combo.getClass()
            else:
                return String().getClass()  # Jython bug

        def isCellEditable(self, row, column):
            if column == 3:
                return True
            else:
                return False

        def getValueAt(self, rowIndex, columnIndex):

            # todo update for other columns
            return {
                0: self.profiles[rowIndex].profile_name,
                1: self.profiles[rowIndex].active,
                2: self.profiles[rowIndex].profile_descr
            }.get(columnIndex)

        def addProfile(self, theProfile):
            self.profiles.append(theProfile)
            # fireTableCellUpdated(row, col)

        def removeProfile(self, profile_name):
            for profile in self.profiles:
                if profile.profile_name == profile_name:
                    self.profiles.remove(profile)
                    break
                    # todo
                    # fireTableCellUpdated(row, col)

    class ComboBoxTableCellRenderer(JComboBox, TableCellRenderer):
        def getTableCellRendererComponent(self, table, value, isSelected, hasFocus, row, column):
            self.setSelectedItem(value)
            return self

    # Handles mouse clicking for all the Edit Profile config options
    class MenuMouseListener(MouseAdapter):

        main_frame = None

        def __init__(self, main_frame):
            self.main_frame = main_frame

        def mousePressed(self, event):
            self.main_frame.show_panel(event.getSource())


if __name__ == '__main__':
    MainFrame()
