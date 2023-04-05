from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        products_by_company = cls.get_products_by_company(products)
        companies_str = cls.get_companies_str(products_by_company)
        return (
            f"{super().generate(products)}\n"
            f"Produtos estocados por empresa:\n{companies_str}"
        )

    @staticmethod
    def get_products_by_company(products):
        products_by_company = {}
        for product in products:
            company = product["nome_da_empresa"]
            if company not in products_by_company:
                products_by_company[company] = 0
            products_by_company[company] += 1
        return products_by_company

    @staticmethod
    def get_companies_str(products_by_company):
        companies_str = ""
        for company, quantity in products_by_company.items():
            companies_str += f"- {company}: {quantity}\n"
        return companies_str
