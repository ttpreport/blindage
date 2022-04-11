from classes.encoders.BlindageRawEncoder import BlindageRawEncoder
from classes.encoders.BlindageBase64Encoder import BlindageBase64Encoder
from classes.encoders.BlindageAESEncoder import BlindageAESEncoder


class BlindageEncoder:
    interface_handler = None
    mode = list()

    def __init__(self, interface_handler):
        self.interface_handler = interface_handler
        self.mode.append(
            {
                'name': 'None',
                'value': BlindageRawEncoder(self.interface_handler)
            }
        )
        self.mode.append(
            {
                'name': 'Base64',
                'value': BlindageBase64Encoder(self.interface_handler)
            }
        )
        self.mode.append(
            {
                'name': 'AES',
                'value': BlindageAESEncoder(self.interface_handler)
            }
        )

    def start(self, data):
        mode_selection = self._select_mode()
        result = mode_selection.encode(data)
        self.interface_handler.print_good("Encoder complete")
        return result

    def _select_mode(self):
        return self.interface_handler.ask_list(
            "Select encoding mode",
            self.mode
        )
