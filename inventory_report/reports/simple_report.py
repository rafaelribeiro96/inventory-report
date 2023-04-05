from collections import Counter
from datetime import date


class SimpleReport:
    @staticmethod
    def generate(products):
        dates_of_manufacture = sorted(
            [product["data_de_fabricacao"] for product in products]
        )

        expiration_dates = sorted(
            [product["data_de_validade"] for product in products if
             product["data_de_validade"] > str(date.today())])

        companies = [product["nome_da_empresa"] for product in products]
        most_common_company = Counter(companies).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {dates_of_manufacture[0]}\n"
            f"Data de validade mais próxima: {expiration_dates[0]}\n"
            f"Empresa com mais produtos: {most_common_company}"
        )
