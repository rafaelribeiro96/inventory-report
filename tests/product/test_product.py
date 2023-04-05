from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        '1',
        'Software de Gestão',
        'Software House',
        '2022/04/21',
        '2023/05/21',
        'MG199948',
        'instrução 2'
    )

    assert product.id == '1'
    assert product.nome_do_produto == 'Software de Gestão'
    assert product.nome_da_empresa == 'Software House'
    assert product.data_de_fabricacao == '2022/04/21'
    assert product.data_de_validade == '2023/05/21'
    assert product.numero_de_serie == 'MG199948'
    assert product.instrucoes_de_armazenamento == 'instrução 2'
