from base64 import b64encode


class BlindageBase64Encoder:
    interface_handler = None

    def __init__(self, interface_handler):
        self.interface_handler = interface_handler

    def encode(self, data):
        self.interface_handler.print_good("Starting base64 encoder...")
        encoded_data = b64encode(data.encode()).decode()
        return "printf {0} | base64 -d | sh".format(encoded_data)

    def __str__(self):
        return 'Base64 encoder'
