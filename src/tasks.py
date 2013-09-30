# -*- coding: utf-8 -*-
import os
import re
import yaml
from db import MongoDB


def _package_parse(filename):
    return ".".join(
        filename.split(".")[:-1])


class TaskTracker(object):

    def __init__(self, filename):
        self._dynamic_import(filename)

    def _is_exist(self, filename):
        if not os.path.exists(filename):
            raise IOError(
                "IOError: File '%s' does not exists." % filename)

    def _dynamic_import(self, filename):
        self._is_exist(filename)
        package_name = _package_parse(filename)
        self.export_module = __import__(package_name, fromlist=['*'])

    def _do_function(self, target_prefix):
        return [
            getattr(self.export_module, attr)
            for attr in dir(self.export_module)
            if re.match(target_prefix, attr)]

    def yaml_read(self):
        yamlpath = self.export_module.settings
        self._is_exist(yamlpath)
        raw_yaml_file = open(yamlpath)
        self.settings = yaml.load(raw_yaml_file)

    def connect_database(self):
        self.db = MongoDB(self.settings.get("server"))

    def disconnect_database(self):
        self.db.disconnect()

    def create_setup_data(self):
        self.db.set_models(self.settings["scheme"])
        self.db.setup_run(self.settings["setup"])

    def destory_setup_data(self):
        self.db.destroy_run()

    def previous_run(self):
        for f in self._do_function("setup_"):
            f()
