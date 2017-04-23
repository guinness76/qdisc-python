from javax.swing import JComboBox, DefaultComboBoxModel, JTextField, JPanel, JLabel
from java.awt import Dimension, BorderLayout, Color
from javax.swing.border import LineBorder


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
    textfield.setMaximumSize(Dimension(100, 20))
    return textfield


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
