import re
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mt
import seaborn as sns

# Extract

with open('./base/Mente-Milionária.txt', 'r', encoding='utf8') as arquivo:
    texto = arquivo.read()

# Quantidade de palavras

# print(len(texto.split()))
# dados = texto.replace(",","")\
#     .replace (".","")\
#     .replace ("?", "")\
#     .replace ("\xad", "")\

#CRIAR UM REGX
# Eliminando caracteres de foma pythonica

regex = re.compile("[a-z-áàâãéêíóôõúüñç]+")	
dados = regex.findall(texto.lower())

# print(len(dados))
# # Quantidade de palavras distintas
# print(len(set(dados)))

#Frequencias

frequencia = Counter(dados).most_common()
# print(frequencia)
frequencia_10 = Counter(dados).most_common(10)
#print(frequencia_10)
frequencia_30 = dict(Counter(dados).most_common(30)) # dict transforma em dicionario

# frequencia 10 100 1000 10000
posicoes = []
tabela = {}
i = 0
while i < len(frequencia):
    posicao = 10

    for indice, item in enumerate(frequencia):  
    # [(palavre, quentidade)], ( palavra , quantidade)
        i+= 1

        if indice == posicao-1:
            posicoes.append(f'Posição : {posicao} Palavra: {item [0]}')
            tabela[item[0]] = item[1]  #posição 0 e as palavras e posição 1 quantidade
            posicao *= 10

# with open('./relatórios/zipf_10m.txt','w', encoding= 'utf8') as arquivo:
#     for item in posicoes:
#         arquivo.write(f'{item}\n')

# Criando visual zipf_10m

def visual10():
    x = posicoes
    y = list(tabela.values())

    dados_df = pd.DataFrame({'Palavras': x, 'Quantidade': y})

    with open('./relatórios/zipf_10m.txt','w', encoding= 'utf8') as arquivo:
        for item in posicoes:
            arquivo.write(f'\n {item}\n')
        arquivo.write(f'\n{str(dados_df)}')
        arquivo.write(f'\n\nQuantidade de palavras: {len(dados)}\
                    \nQuantidade de palavras Destintas: {len(set(dados))}',)
    fig, ax = plt.subplots(figsize=(10,5))
    x = np.arange(len(dados_df['Palavras']))

    visual = ax.bar(x=x, height="Quantidade", data=dados_df)

    ax.set_title('Análise ZipF', fontsize=14, pad=20) # dar nome, fonte da letra 
    ax.set_xlabel('Palavras', fontsize=12, labelpad=10)
    ax.set_ylabel('Quantidade', fontsize=12, labelpad=10)

    ax.set_xticks(x)
    ax.set_xticklabels(dados_df['Palavras'])
    ax.bar_label(visual, size=10, label_type='edge')

    plt.savefig('./relatórios/zipf_10m.png', dpi=600, bbox_inches='tight')

dados_dt = pd.DataFrame(
    {
        'Palavra': frequencia_30.keys(),
        'Quantidade': frequencia_30.values()
    })
x = list(frequencia_30.keys())
y = list(frequencia_30.values())

fig, ax = plt.subplots(figsize=(12,6))
mt.style.use(['seaborn'])

sns.barplot(x=x, y=y)

ax.set_title('Zipf 30+', fontsize=12)
ax.set_ylabel('Quantidade de repetições', fontsize=12, color='purple')
#ax.set_xlabel('Quantidade de repetições', fontsize=12, color='purple')

plt.xticks(rotation=60, fontsize=11)

for i, v in enumerate(y):
    ax.text(x=i-0.4, y=v+0.9, s=v, fontsize=10)
  
plt.savefig('./relatórios/zipf_11m.png', dpi=600, bbox_inches='tight')


