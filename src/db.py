# -*- coding: utf-8 -*-

import random
import json
import pymongo
from color import blue_print


class MongoDB(object):

    def __init__(self, yamldata):
        server = yamldata
        self._client = pymongo.Connection(
            host=server["host"], port=server["port"])
        self.database = self._client[server["database"]]

    def disconnect(self):
        self.database = None
        self._client.disconnect()

    def set_models(self, scheme):
        self.scheme = scheme

    def setup_run(self, setup):
        self.generated_records = []
        for running_model in setup:
            self.generated_records.append(
                {"model": running_model,
                 "records": self.generate_record(
                     running_model["model"])})

    def destory_run(self):
        for delete_record in self.generated_records:
            pass

    def generate_record(self, model):
        generated_records = []
        running_model = self.scheme[model["target"]]

        print json.dumps(running_model, indent=2)
        separate_number = model["generate"] / 10
        collection = self.database[model["target"]]
        for create_time in range(model["generate"] + 1):
            if (create_time % separate_number) == 0:
                blue_print("   * Now, %s times generate" % create_time)
            generated_record = self.generate_json_from_model(running_model)
            collection.insert(generated_record)
            generated_records.append(generated_record)
            print generated_record
        blue_print("   * End. %s records generated." % create_time)
        return generated_records

    def generate_json_from_model(self, model):
        generated_json = {}
        for key, value in model.items():
            if value["type"] == "RandomString":
                value["type"] = ("".join([
                    chr(random.randint(0, 90))
                    for x in range(0, 32)]))
            if value["type"] == "RandomEmbedded":
                value.pop("type")
                value["type"] = self.generate_embedded(value)
            generated_json[key] = value["type"]
        return generated_json

    def generate_embedded(self, model):
        pass
