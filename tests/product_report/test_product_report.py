from inventory_report.inventory.product import Product


id_do_produto = 1
nome_do_produto = "Software de Gestão"
nome_da_empresa = "Software House"
data_de_fabricacao = "2022/04/21"
data_de_validade = "2023/05/21"
numero_de_serie = "MG199948"
instrucoes_de_uso = "instrução 2"


def test_relatorio_produto():
    mocked_product = Product(
        id_do_produto,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_uso,
    )
    assert mocked_product.id == id_do_produto
    assert mocked_product.nome_do_produto == nome_do_produto
    assert mocked_product.nome_da_empresa == nome_da_empresa
    assert mocked_product.data_de_validade == data_de_validade
    assert mocked_product.data_de_fabricacao == data_de_fabricacao
    assert mocked_product.numero_de_serie == numero_de_serie
    assert mocked_product.instrucoes_de_armazenamento == instrucoes_de_uso
