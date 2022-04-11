from yaml import safe_load as load_yaml_file, safe_dump as save_yaml_file
from time import time
from collections import defaultdict
from pathlib import Path


class BlindageConfiguratorCache:
    config_path = Path('./cache.yml')
    interface_handler = None
    config = defaultdict(dict)
    dirty = False

    def __init__(self, interface_handler):
        self.interface_handler = interface_handler
        self.config = self._load_config()

    def __del__(self):
        if self.dirty:
            self._backup_config()
            self._save_config()

    def get(self, module_name, variable_name):
        try:
            return self.config[module_name][variable_name]
        except Exception:
            return None

    def set(self, module_name, variable_name, variable_value):
        if self.get(module_name, variable_name) != variable_value:
            self.dirty = True
            try:
                self.config[module_name][variable_name] = variable_value
            except KeyError:
                self.config[module_name] = {variable_name: variable_value}
        return self

    def _load_config(self):
        try:
            file_stream = open(self.config_path, "r")
        except FileNotFoundError:
            file_stream = open(self.config_path, 'w+')
        return load_yaml_file(file_stream) or self.config

    def _save_config(self):
        file_stream = open(self.config_path, 'w+')
        return save_yaml_file(dict(self.config), file_stream)

    def _backup_config(self):
        backup_path = self._generate_path()
        backup_path.write_text(self.config_path.read_text())
        return self

    def _generate_path(self):
        return self.config_path.with_stem(
            self.config_path.stem + "-" + str(int(time()))
        )
