from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

report_types = {"simples": SimpleReport, "completo": CompleteReport}


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if ".csv" in path:
            content = CsvImporter.import_data(path)
        elif ".json" in path:
            content = JsonImporter.import_data(path)
        else:
            content = XmlImporter.import_data(path)

        return report_types[type].generate(content)
