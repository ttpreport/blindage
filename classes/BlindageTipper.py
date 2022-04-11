from chevron import render


class BlindageTipper:
    interface_handler = None

    def __init__(self, interface_handler):
        self.interface_handler = interface_handler

    def start(self, modules):
        self.interface_handler.print_good("Writing out tips...")
        for module in modules:
            if module.tip:
                tip = render(module.tip, module.config)
                print("* {0}".format(tip))
        self.interface_handler.print_good("Writing tips complete")
        return
