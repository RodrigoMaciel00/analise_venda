def gerar_relatorio(media_preco, mediana_preco, desvio_quantidade):
    print("Relatório de Análise de Dados")
    print(f"Média de Preços: {media_preco}")
    print(f"Mediana de Preços: {mediana_preco}")
    print(f"Desvio Padrão da Quantidade Vendida: {desvio_quantidade}")

def salvar_relatorio(
    media_preco, mediana_preco, desvio_quantidade,
    vendas_categoria, vendas_produto, correlacao,
    outliers_preco, outliers_quantidade, vendas_mensais
):
    with open('../data/relatorio_vendas_completo.txt', 'w') as f:
        f.write("Relatório de Análise de Dados Completo\n\n")
        f.write(f"Média de Preços: {media_preco}\n")
        f.write(f"Mediana de Preços: {mediana_preco}\n")
        f.write(f"Desvio Padrão da Quantidade Vendida: {desvio_quantidade}\n\n")

        f.write("Vendas Totais por Categoria:\n")
        f.write(vendas_categoria.to_string())

        f.write("\n\nVendas Totais por Produto:\n")
        f.write(vendas_produto.to_string())

        f.write("\n\nCorrelação entre Preço e Quantidade:\n")
        f.write(correlacao.to_string())

        f.write("\n\nOutliers de Preço:\n")
        f.write(outliers_preco.to_string())

        f.write("\n\nOutliers de Quantidade:\n")
        f.write(outliers_quantidade.to_string())

        f.write("\n\nVendas Mensais:\n")
        f.write(vendas_mensais.to_string())

    print("Relatório salvo em '../data/relatorio_vendas_completo.txt'.")
