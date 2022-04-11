class BlindageRawEncoder:
    interface_handler = None

    def __init__(self, interface_handler):
        self.interface_handler = interface_handler

    def encode(self, data):
        self.interface_handler.print_good("Skipping encoding...")
        return data

    def __str__(self):
        return 'Raw encoder'
