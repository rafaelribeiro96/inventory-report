from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    product = [
        {
            "id": "1",
            "nome_do_produto": "Software de Gestão",
            "nome_da_empresa": "Software House",
            "data_de_fabricacao": "2022-04-21",
            "data_de_validade": "2023-05-21",
            "numero_de_serie": "MG199948",
            "instrucoes_de_armazenamento": "instrução 2"
        }
    ]

    report_decorator = ColoredReport(SimpleReport)

    report = report_decorator.generate(product)

    assert report == (
        "\033[32mData de fabricação mais antiga:\033[0m "
        "\033[36m2022-04-21\033[0m\n"
        "\033[32mData de validade mais próxima:\033[0m "
        "\033[36m2023-05-21\033[0m\n"
        "\033[32mEmpresa com mais produtos:\033[0m "
        "\033[31mSoftware House\033[0m"
    )
