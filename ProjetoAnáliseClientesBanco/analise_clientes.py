import pandas as pd
import plotly.express as px

#Carregando os dados
tabela = pd.read_csv("/Users/isabelacunha/VSCode-Workspace/python/ClientesBanco.csv", encoding="latin1")

#Tratando os dados 
tabela = tabela.drop("CLIENTNUM", axis=1)
tabela = tabela.dropna()
print(tabela.info())
print(tabela.describe().round(1))


#CLIENTES X CANCELADOS

qtde_categoria = tabela["Categoria"].value_counts()
print(qtde_categoria)

qtde_categoria_perc = tabela["Categoria"].value_counts(normalize=True)
print("Percentual de clientes e cancelados\n", qtde_categoria_perc)

#Comparar os clientes e os cancelados para descobrir o motivo de cancelamento
for coluna in tabela:
    grafico = px.histogram(tabela, x=coluna, color="Categoria")
    grafico.write_image(f"grafico_{coluna}.svg") 
    grafico.show()

