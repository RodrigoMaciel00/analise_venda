import matplotlib.pyplot as plt
import seaborn as sns
from src.analise_dados import vendas_por_mes

def plotar_distribuicao_precos(df):
    plt.figure(figsize=(8, 5))
    plt.hist(df['Preço'], bins=20, color='skyblue', edgecolor='black')  # Correção de 'bin' para 'bins'
    plt.title('Distribuição de Preços')
    plt.xlabel('Preço')
    plt.ylabel('Frequência')
    plt.show()

def plotar_vendas_por_categoria(df):
    vendas_categoria = df.groupby('Categoria')['Quantidade'].sum()
    vendas_categoria.plot(kind='bar', color='teal', figsize=(8, 5))
    plt.xlabel('Categoria')
    plt.ylabel('Quantidade Vendida')
    plt.title('Vendas Totais por Categoria')
    plt.xticks(rotation=45)
    plt.show()

def plotar_vendas_por_produto(df):
    vendas_produto = df.groupby('Produto')['Quantidade'].sum()
    vendas_produto.plot(kind='bar', color='orange', figsize=(8, 5))
    plt.title('Vendas Totais por Produto')
    plt.xlabel('Produto')
    plt.ylabel('Quantidade Vendida')
    plt.xticks(rotation=45)
    plt.show()

def plotar_vendas_ao_longo_do_tempo(df):
    df['Data_Venda'] = pd.to_datetime(df['Data_Venda'])  # Converter para datetime se necessário
    vendas_por_data = df.groupby('Data_Venda')['Quantidade'].sum()
    plt.figure(figsize=(10, 5))
    vendas_por_data.plot(color='purple', marker='o')
    plt.title('Vendas ao Longo do Tempo')
    plt.xlabel('Data')
    plt.ylabel('Quantidade Vendida')
    plt.grid()
    plt.show()

def plotar_correlacao_preco_quantidade(df):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x='Preço', y='Quantidade')
    plt.title('Correlação entre Preço e Quantidade')
    plt.xlabel('Preço')
    plt.ylabel('Quantidade')
    plt.show()

def plotar_vendas_por_mes(df):
    vendas_mensais = vendas_por_mes(df)
    plt.figure(figsize=(10, 5))
    vendas_mensais.plot(kind='bar', color='skyblue')
    plt.title('Vendas Totais por Mês')
    plt.xlabel('Mês')
    plt.ylabel('Quantidade Vendida')
    plt.xticks(rotation=45)
    plt.show()
