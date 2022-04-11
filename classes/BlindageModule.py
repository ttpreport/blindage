from yaml import safe_load as load_yaml_file
from pathlib import Path


class BlindageModule:
    name = str()
    description = str()
    category = str()
    need_root = bool()
    variables = dict()
    config = dict()
    script = str()
    priority = int()
    tip = str()
    function_name = str()

    def load_yaml(self, file):
        file_stream = open(file, 'r')
        object = load_yaml_file(file_stream)
        self.name = str(object['name'])
        self.description = str(object['description'])
        self.category = str(object['category']).strip()
        self.need_root = bool(object['need_root'])
        self.variables = object['variables']
        self.script = str(object['script'])
        self.priority = int(object['priority'])
        self.tip = str(object['tip'])
        self.file_name = Path(file).stem
        return self

    def set_config(self, config):
        self.config = config
        return self

    def __str__(self):
        return self.name
