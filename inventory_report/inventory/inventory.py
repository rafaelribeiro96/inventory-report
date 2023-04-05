from importlib import import_module
from pathlib import Path


INVALID_FILE = "Arquivo inválido!"


class Inventory:
    importers = {
        ".csv": "CsvImporter",
        ".json": "JsonImporter",
        ".xml": "XmlImporter"
    }
    report_types = {
        "simples": "SimpleReport",
        "completo": "CompleteReport"
    }

    @classmethod
    def import_data(cls, path, type):
        extension = Path(path).suffix
        if extension not in cls.importers:
            raise ValueError(INVALID_FILE)

        importer_module = import_module(
            f"inventory_report.importer.{cls.importers[extension]}"
        )
        content = importer_module.Importer.import_data(path)
        report_module = import_module(
            f"inventory_report.reports.{cls.report_types[type]}"
        )
        return report_module.generate(content)
