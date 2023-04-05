import json
from inventory_report.importer.importer import Importer

INVALID_FILE = "Arquivo inválido!"


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".json"):
            raise ValueError(INVALID_FILE)

        with open(path, "r") as file:
            return json.load(file)
