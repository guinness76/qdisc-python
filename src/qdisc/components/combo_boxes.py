from javax.swing import JComboBox, DefaultComboBoxModel
from java.awt import Dimension


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
