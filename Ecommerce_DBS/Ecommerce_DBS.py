import pandas as pd
from datetime import datetime

# Lendo o arquivo CSV e transformando-o em um DataFrame!!
def ler_csv_para_dataframe(caminho_arquivo):
    return pd.read_csv(caminho_arquivo)

# Chamando a função!!
caminho = "Ecommerce_DBS.csv"
df = ler_csv_para_dataframe(caminho)

def ler_csv_para_dataframe(caminho_arquivo):
    try:
        df = pd.read_csv(caminho_arquivo, sep=';')
        return df
    except FileNotFoundError:
        print(f"Arquivo não foi encontrado: {caminho_arquivo}")
        return None
    except pd.errors.EmptyDataError:
        print("O arquivo CSV está vazio")
        return None
    except pd.errors.ParserError:
        print("Erro ao analisar o arquivo CSV")
        return None



# Ler o CSV em um DataFrame
caminho_arquivo = "Ecommerce_DBS.csv"
df = ler_csv_para_dataframe(caminho_arquivo)



# Resolução da questão 01 abaixo:

if df is not None:
    # Verificar as primeiras linhas do Dataframe!
    print(df.head())
else:
    print("Erro ao ler o arquivo CSV")

if df is not None:
    if 'Purchase Date' in df.columns:
        # Convertendo a coluna 'Purchase Date' para datetime!
        df['Purchase Date'] = pd.to_datetime(df['Purchase Date'], errors='coerce')

        data_atual = datetime.now()
        tres_anos_atras = data_atual - pd.DateOffset(years=3)
        df_ultimos_tres_anos = df[df['Purchase Date'] >= tres_anos_atras]

        # Agrupar os dados pelos produtos e somando as quantidades vendidas!
        df_agrupado = df_ultimos_tres_anos.groupby('Product Category')['Quantity'].sum().reset_index()

        df_ordenado = df_agrupado.sort_values(by='Quantity', ascending=False)

        top_produtos = df_ordenado.head(10)

        print("\n\nResposta da questão 01 abaixo: ")
        print(top_produtos)
    else:
        print("A coluna 'Purchase Date' não foi encontrada no DataFrame.")
else:
    print("Erro ao ler o arquivo CSV")



# Resolução da questão 02 abaixo:

# Encontrando o Produto mais caro!
produto_mais_caro = df.loc[df['Product Price'].idxmax()]

# Encontrando o Produto mais barato!
produto_mais_barato = df.loc[df['Product Price'].idxmin()]


print("\n\nResposta da questão 02 abaixo: ")
print("Produto mais caro abaixo:")
print(produto_mais_caro)

print("\nProduto mais barato abaixo:")
print(produto_mais_barato)



# Resolução da questão 03 abaixo:

# Encontrando a categoria mais vendida!!
categoria_mais_vendida = df.groupby('Product Category')['Quantity'].sum().idxmax()

# Encontrando a categoria menos vendida!!
categoria_menos_vendida = df.groupby('Product Category')['Quantity'].sum().idxmin()

# Encontrando a categoria mais cara!!
categoria_mais_cara = df.groupby('Product Category')['Product Price'].mean().idxmax()

# Encontrando a categoria menos cara!!
categoria_menos_cara = df.groupby('Product Category')['Product Price'].mean().idxmin()

print("\n\nResposta da questão 03 abaixo: ")
print("Categoria mais vendida:", categoria_mais_vendida)
print("Categoria menos vendida:", categoria_menos_vendida)
print("Categoria mais cara:", categoria_mais_cara)
print("Categoria menos cara:", categoria_menos_cara)



# Resolução da questão 04 abaixo:

# Encontrando o produto com melhor NPS
maximo_nps_category = df.loc[df['NPS'].idxmax()]

# Encontrando o produto com pior NPS
minimo_nps_category = df.loc[df['NPS'].idxmin()]

print("\n\nResposta da questão 04 abaixo: ")
print(f"O produto com o melhor NPS é: {maximo_nps_category['Product Category']} com NPS {maximo_nps_category['NPS']}")
print("Detalhes do produto:")
print(maximo_nps_category)
print()

print(f"O produto com o pior NPS é: {minimo_nps_category['Product Category']} com NPS {minimo_nps_category['NPS']}")
print("Detalhes do produto:")
print(minimo_nps_category)






