from classes.selectors.BlindageSimpleSelector import BlindageSimpleSelector
from classes.selectors.BlindageAdvancedSelector import BlindageAdvancedSelector


class BlindageSelector:
    interface_handler = None
    modes = list()

    def __init__(self, interface_handler):
        self.interface_handler = interface_handler
        self.modes.append(
            {
                'name': 'Simple',
                'value': BlindageSimpleSelector(self.interface_handler)
            }
        )
        self.modes.append(
            {
                'name': 'Advanced',
                'value': BlindageAdvancedSelector(self.interface_handler)
            }
        )

    def start(self, modules):
        mode_selection = self._select_mode()
        return mode_selection.configure(modules)

    def _select_mode(self):
        return self.interface_handler.ask_list(
            "Select configuration mode",
            self.modes
        )
