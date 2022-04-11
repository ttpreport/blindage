class BlindageStdoutWriter:
    interface_handler = None

    def __init__(self, interface_handler):
        self.interface_handler = interface_handler

    def save(self, data):
        self.interface_handler.print_good("Writing blindage to stdout...")
        print(data)

    def __str__(self):
        return "Stdout writer"
