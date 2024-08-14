import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

dados = pd.read_csv(r'C:\Users\seuarquivocsv.csv')

descricao = dados.describe()

print(descricao)


