from chevron import render
from operator import attrgetter
from utils.BashMinifier import minify


class BlindageGenerator:
    interface_handler = None
    script = str()

    def __init__(self, interface_handler):
        self.interface_handler = interface_handler
        self.script = ''

    def start(self, modules):
        self.interface_handler.print_good("Starting blindage generator...")
        for module in sorted(modules, key=attrgetter('priority')):
            module_script = render(module.script, module.config)
            self._add_function(module.file_name, module_script)
        self.script = minify(self.script)
        self.interface_handler.print_good("Blindage generation complete")
        return self.script

    def _add_function(self, name, function):
        new_function = self._wrap_function(name, function)
        self.script += "\n" + new_function
        return self

    def _wrap_function(self, name, function):
        wrapped_function = (
            "{0}() (set -e; {1}); {0} > /dev/null;"
            "if [ $? -eq 0 ]; then printf '\\033[1;32m[+]\\033[m {0}\\n';"
            "else printf '\\033[1;31m[-]\\033[m {0}\\n'; fi;"
        ).format(name, function)
        return wrapped_function
