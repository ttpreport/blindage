from time import time
from pathlib import Path


class BlindageFileWriter:
    DEFAULT_PATH = './blindage-package'

    target_path = ""
    interface_handler = None

    def __init__(self, interface_handler):
        self.interface_handler = interface_handler

    def save(self, data):
        self.interface_handler.print_good("Saving blindage to file...")
        self.target_path = Path(self.interface_handler.ask_text(
            "Enter filename [default: {0}]".format(
                self.DEFAULT_PATH
            )
        ) or self.DEFAULT_PATH)
        if self.target_path.is_file():
            action = self.interface_handler.ask_list(
                "File already exists. What do you want to do?",
                ['Backup existing', 'Rename current', 'Overwrite existing'])
            if action == 'Backup existing':
                self._backup()
            elif action == 'Rename current':
                while self.target_path.is_file():
                    self.target_path = Path(
                        self.interface_handler.ask_text("New filename")
                    )

        self.target_path.write_text(data)
        self.interface_handler.print_good("Blindage saved to file '{0}'".format(
            self.target_path
        ))
        return self

    def _backup(self):
        backup_path = self._generate_path()
        backup_path.write_text(self.target_path.read_text())
        return self

    def _generate_path(self):
        return self.target_path.with_stem(
            self.target_path.stem + "-" + str(int(time()))
        )

    def __str__(self):
        return "File writer"
