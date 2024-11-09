import pandas as pd

def carregar_dados(caminho='../data/dados_ficticios.csv'):
    try:
        df = pd.read_csv(caminho)
        # Verificação de colunas esperadas
        colunas_esperadas = {'Produto', 'Categoria', 'Preço', 'Quantidade', 'Data_Venda'}
        if not colunas_esperadas.issubset(df.columns):
            raise ValueError("O arquivo de dados não contém as colunas esperadas.")
        return df
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho}' não encontrado.")
    except ValueError as e:
        print(f"Erro no formato dos dados: {e}")
    except Exception as e:
        print(f"Ocorreu um erro ao carregar os dados: {e}")

def calcular_estatisticas(df):
    media_preco = df['Preço'].mean()
    mediana_preco = df['Preço'].median()
    desvio_quantidade = df['Quantidade'].std()
    return media_preco, mediana_preco, desvio_quantidade

def total_vendas_por_categoria(df):
    return df.groupby('Categoria')['Quantidade'].sum()

def total_vendas_por_produto(df):
    return df.groupby('Produto')['Quantidade'].sum()

def vendas_por_data(df):
    df['Data_Venda'] = pd.to_datetime(df['Data_Venda'])  # Converter para datetime se necessário
    return df.groupby('Data_Venda')['Quantidade'].sum()

def calcular_correlacao(df):
    return df[['Preço', 'Quantidade']].corr()

def identificar_outliers(df, coluna):
    limite_superior = df[coluna].mean() + 3 * df[coluna].std()
    limite_inferior = df[coluna].mean() - 3 * df[coluna].std()
    return df[(df[coluna] > limite_superior) | (df[coluna] < limite_inferior)]

def vendas_por_mes(df):
    df['Data_Venda'] = pd.to_datetime(df['Data_Venda'])
    df['Mes'] = df['Data_Venda'].dt.to_period('M')
    return df.groupby('Mes')['Quantidade'].sum()
