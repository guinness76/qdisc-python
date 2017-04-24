from javax.swing import JComboBox, DefaultComboBoxModel, JTextField, JPanel, ListCellRenderer, JLabel, JTextArea
from java.awt import Dimension, BorderLayout, Color, Font
from javax.swing.border import LineBorder


def get_title_font(jLabel):
    return Font(jLabel.getFont().getName(), Font.BOLD, 14)


# Builds out a combobox preconfigured with various bandwidth settings
def get_rate_combo():
    combo_box = JComboBox()
    combo_model = DefaultComboBoxModel()
    combo_model.addElement("MB/sec")
    combo_model.addElement("KB/sec")
    combo_model.addElement("bytes/sec")
    combo_model.addElement("mbit/sec")
    combo_model.addElement("kbit/sec")
    combo_box.setModel(combo_model)
    combo_box.setMaximumSize(Dimension(100, 20))
    return combo_box

    # todo add translators for the elements:
    # MB/sec -> mbps
    # KB/sec -> kbps
    # bytes/sec -> bps or a bare number
    # mbit/sec -> mbit
    # kbit/sec -> kbit


# Builds out a combobox preconfigured with various time settings
def get_time_combo():
    combo_box = JComboBox()
    combo_model = DefaultComboBoxModel()
    combo_model.addElement("seconds")
    combo_model.addElement("milliseconds")
    combo_model.addElement("microseconds")
    combo_box.setModel(combo_model)
    combo_box.setMaximumSize(Dimension(100, 20))
    return combo_box

    # todo add translators for the elements:
    # seconds -> s
    # milliseconds -> ms
    # microseconds -> us


def get_delay_correlation_combo():
    combo_box = JComboBox()
    combo_model = DefaultComboBoxModel()
    combo_model.addElement("normal")
    combo_model.addElement("uniform")
    combo_model.addElement("pareto")
    combo_model.addElement("paretonormal")
    combo_box.setModel(combo_model)
    combo_box.setMaximumSize(Dimension(120, 20))
    return combo_box


# Textfields for the traffic modifications panels. Textfield is set to a default max size
def get_setting_textfield():
    textfield = JTextField()
    textfield.setMinimumSize(Dimension(100, 20))
    textfield.setMaximumSize(Dimension(100, 20))
    return textfield

def get_setting_textarea():
    textarea = JTextArea(100, 10)
    #textarea.setMinimumSize(Dimension(400, 100))
    return textarea


class MenuItem(JPanel):
    is_selected = False
    settings_panel = None

    def __init__(self, menu_title, the_settings_panel):
        self.settings_panel = the_settings_panel
        self.settings_panel.set_selected(False)

        self.setLayout(BorderLayout())
        self.setBorder(LineBorder(Color.darkGray))
        self.add(JLabel(menu_title), BorderLayout.CENTER)

    def set_selected(self, is_selected):
        self.is_selected = is_selected
        self.settings_panel.set_selected(is_selected)


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


class FilterRenderer(ListCellRenderer):
    def getListCellRendererComponent(self, list, value, index, isSelected, cellHasFocus):
        # todo Change background color when object is selected
        return JLabel(value.print_filter())
