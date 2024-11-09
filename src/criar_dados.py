import os
import pandas as pd
import random
from datetime import datetime, timedelta

def criar_dados_ficticios():
    if not os.path.exists('../data'):
        os.makedirs('../data')

    produtos = ['Produto A', 'Produto B', 'Produto C', 'Produto D']
    categorias = ['Eletrônicos', 'Roupas', 'Brinquedos', 'Alimentos']
    data_inicial = datetime(2023, 1, 1)
    dados = []

    for i in range(100):
        produto = random.choice(produtos)
        categoria = random.choice(categorias)
        preco = round(random.uniform(10, 200), 2)
        quantidade = random.randint(1, 10)
        data_venda = data_inicial + timedelta(days=random.randint(0, 365))
        dados.append([produto, categoria, preco, quantidade, data_venda])

    df = pd.DataFrame(dados, columns=['Produto', 'Categoria', 'Preço', 'Quantidade', 'Data_Venda'])
    df.to_csv('../data/dados_ficticios.csv', index=False)
    return df
