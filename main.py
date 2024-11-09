from src import criar_dados, analise_dados, visualizacao, relatorio
from config import DADOS_CAMINHO, RELATORIO_CAMINHO

def executar_analise():
    # Criar dados fictícios e carregar os dados
    df = criar_dados.criar_dados_ficticios()
    media_preco, mediana_preco, desvio_quantidade = analise_dados.calcular_estatisticas(df)

    # Análise Adicional
    vendas_categoria = analise_dados.total_vendas_por_categoria(df)
    vendas_produto = analise_dados.total_vendas_por_produto(df)
    correlacao = analise_dados.calcular_correlacao(df)
    outliers_preco = analise_dados.identificar_outliers(df, 'Preço')
    outliers_quantidade = analise_dados.identificar_outliers(df, 'Quantidade')
    vendas_mensais = analise_dados.vendas_por_mes(df)

    # Visualização
    visualizacao.plotar_vendas_por_categoria(df)
    visualizacao.plotar_vendas_por_produto(df)
    visualizacao.plotar_vendas_ao_longo_do_tempo(df)
    visualizacao.plotar_correlacao_preco_quantidade(df)
    visualizacao.plotar_vendas_por_mes(df)

    # Relatório Final
    relatorio.salvar_relatorio(
        media_preco, mediana_preco, desvio_quantidade,
        vendas_categoria, vendas_produto, correlacao,
        outliers_preco, outliers_quantidade, vendas_mensais
    )

if __name__ == "__main__":
    executar_analise()
