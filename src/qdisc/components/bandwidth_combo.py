from javax.swing import JComboBox, DefaultComboBoxModel
from java.awt import Dimension


# Builds out a combobox preconfigured with various bandwidth settings
# todo turn into a static Jython class?
class BandwidthCombo:
    combo_box = JComboBox()

    def __init__(self):
        combo_model = DefaultComboBoxModel()
        combo_model.addElement("MB/sec")
        combo_model.addElement("KB/sec")
        combo_model.addElement("bytes/sec")
        combo_model.addElement("mbit/sec")
        combo_model.addElement("kbit/sec")
        self.combo_box.setModel(combo_model)
        self.combo_box.setMaximumSize(Dimension(100, 20))

    def get_combo_box(self):
        return self.combo_box;

        # todo add translators for the elements:
        # MB/sec -> mbps
        # KB/sec -> kbps
        # bytes/sec -> bps or a bare number
        # mbit/sec -> mbit
        # kbit/sec -> kbit
