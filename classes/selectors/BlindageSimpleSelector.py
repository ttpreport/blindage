class BlindageSimpleSelector:
    interface_handler = None

    def __init__(self, interface_handler):
        self.interface_handler = interface_handler

    def configure(self, modules):
        self.interface_handler.print_good("Starting simple configurator...")
        selected_modules = self._select_modules(modules)
        self.interface_handler.print_good("Simple configuration complete")
        return selected_modules

    def _select_modules(self, modules):
        selected_modules = list()
        have_root = self.interface_handler.ask_yesno("Do you have root?")
        if have_root:
            selected_modules = modules
        else:
            selected_modules = filter(lambda x: not x.need_root, modules)
        return selected_modules
