from xml.etree import ElementTree
from inventory_report.importer.importer import Importer


INVALID_FILE = "Arquivo inválido!"


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".xml"):
            raise ValueError(INVALID_FILE)

        with open(path, "r") as file:
            root = ElementTree.parse(file).getroot()
            records = []
            for record in root.findall("record"):
                record_dict = {}
                for child in record:
                    record_dict[child.tag] = child.text
                records.append(record_dict)
            return records
