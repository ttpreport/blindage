from classes.BlindageModule import BlindageModule

from os import scandir, getenv


class BlindageLoader:
    DEFAULT_FOLDER = "./modules"

    modules_folder = "./modules"
    modules = list()
    categories = set()
    total_count = int()
    loaded_count = int()
    errors = list()
    interface_handler = None

    def __init__(self, interface_handler):
        self.interface_handler = interface_handler
        self.modules_folder = getenv('MODULES_FOLDER', self.DEFAULT_FOLDER)

    def load(self):
        self.interface_handler.print_good("Loading modules...")
        for module_file in scandir(self.modules_folder):
            self.total_count += 1
            try:
                module = BlindageModule()
                module.load_yaml(module_file.path)
                self.modules.append(module)
                self.categories.add(module.category)
                self.loaded_count += 1
            except Exception as e:
                error_object = {'file': module_file.path, 'error': str(e)}
                self.interface_handler.print_bad("Couldn't load {0}: {1}".format(
                    error_object['file'], error_object['error'])
                )
                self.errors.append(error_object)

        self.interface_handler.print_good("Loaded {0} out of {1} modules".format(
            self.loaded_count, self.total_count)
        )

        return self.modules
