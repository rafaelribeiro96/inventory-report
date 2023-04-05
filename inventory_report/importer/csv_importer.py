import csv
from inventory_report.importer.importer import Importer

INVALID_FILE = "Arquivo inválido!"


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".csv"):
            raise ValueError(INVALID_FILE)

        with open(path, "r") as file:
            content = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(content)
