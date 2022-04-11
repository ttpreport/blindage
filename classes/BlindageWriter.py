from classes.writers.BlindageFileWriter import BlindageFileWriter
from classes.writers.BlindageStdoutWriter import BlindageStdoutWriter


class BlindageWriter:
    interface_handler = None
    modes = list()

    def __init__(self, interface_handler):
        self.interface_handler = interface_handler
        self.modes.append({
            'name': 'File',
            'value': BlindageFileWriter(self.interface_handler)
        })
        self.modes.append({
            'name': 'Stdout',
            'value': BlindageStdoutWriter(self.interface_handler)
        })

    def start(self, data=""):
        self.interface_handler.print_good("Starting blindage writer...")
        output_selection = self._select_output()
        output_selection.save(data)
        self.interface_handler.print_good("Blindage writing complete")

    def _select_output(self):
        return self.interface_handler.ask_list(
            "Select output mode",
            self.modes
        )
