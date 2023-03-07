from WBT.whitebox_tools import WhiteboxTools

# We can use this file to change the official interface as we need it

class Whitebox(WhiteboxTools):
    def __init__(self):
        super().__init__()

        # add a few paths
        self.input_data_path = '/in'
        self.output_data_path = '/out'

wbt = Whitebox()
