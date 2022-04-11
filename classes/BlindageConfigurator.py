class BlindageConfigurator:
    interface_handler = None
    cache = None

    def __init__(self, interface_handler, cache):
        self.interface_handler = interface_handler
        self.cache = cache

    def start(self, modules):
        self.interface_handler.print_good("Starting modules configurator...")
        return self._select_modules_config(modules)

    def _select_modules_config(self, modules):
        return [
            module.set_config(self._select_single_config(module))
            for module in modules
        ]

    def _select_single_config(self, module):
        self.interface_handler.print_good(
            "Configuring module {0}...".format(module.name))
        config = dict()
        for module_variable in module.variables or []:
            question = "{0}/{1} ({2})"
            cached_value = self.cache.get(module.file_name,
                                          module_variable['name'])

            new_value = self.interface_handler.ask_text(
                question.format(
                    module.name, module_variable['name'],
                    module_variable['description']
                ),
                default=cached_value,
                validate=lambda x: "".__ne__(x)
            )
            config[module_variable['name']] = new_value
            self.cache.set(module.file_name,
                           module_variable['name'], new_value)
        self.interface_handler.print_good(
            "Module {0} configured".format(module.name))
        return config
