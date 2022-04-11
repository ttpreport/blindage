from itertools import groupby
from operator import attrgetter


class BlindageAdvancedSelector:
    interface_handler = None

    def __init__(self, interface_handler):
        self.interface_handler = interface_handler

    def configure(self, modules):
        self.interface_handler.print_good("Starting advanced configurator...")
        selected_modules = self._select_modules(modules)
        self.interface_handler.print_good("Advanced configuration complete")
        return selected_modules

    def _select_modules(self, modules):
        selected_modules = list()
        sorted_modules = sorted(
            modules, key=lambda x: (x.category, x.need_root))
        for category, category_grouped_modules in groupby(sorted_modules, key=attrgetter('category')):
            modules_choices = list()
            for need_root, need_root_grouped_modules in groupby(category_grouped_modules, key=attrgetter('need_root')):
                if need_root:
                    separator = self.interface_handler.get_separator(
                        "= ROOT LEVEL =")
                else:
                    separator = self.interface_handler.get_separator(
                        "= USER LEVEL =")

                modules_choices.extend([separator] + [
                    {
                        'name': ("{0} ({1})").format(module.name, module.description),
                        'value': module
                     } for module in need_root_grouped_modules
                ])
            selected_modules.extend(self.interface_handler.ask_checkbox(
                    "Select {0} modules".format(category),
                    modules_choices
                    ))

        return selected_modules
