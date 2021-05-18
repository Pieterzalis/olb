from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import spacy
import numpy as np
import pandas as pd

nlp = spacy.load("pt_core_news_md")

def limpando_texto(x):
  """Função que Limpa os Tokens das Proposições. A ideia é que o input seja a junção das ementas, palavras-chaves e temas da proposição"""
    tokens_final = []
    doc = nlp(x)
    for token in doc:
        if token.is_stop == False and token.is_alpha == True and token.is_punct == False and (token.pos_ == 'PROPN' or token.pos_ == 'NOUN' or token.pos_ == 'VERB'):
            if len(token.text) >= 3:
                tokens_final.append(token.text)
    return ' '.join(tokens_final)
  

### realizando tf-idf  
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=5, max_features=20000, stop_words=None)
tfidf = tfidf_vectorizer.fit_transform(df_texto_limpo['Texto Limpo'])

### transformando nmf
nmf = NMF(n_components=100, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit_transform(tfidf)

## pegando os tópicos
topicos = pd.read_csv('tabelas/100_nmf.csv')
topicos.columns = ['Topico','Categoria','Palavras-Chaves']
topicos = topicos.sort_values(by='Topico')

## criando um dataframe e nomeando as colunas de acordo com a classificação manual
df_nmf = pd.DataFrame(nmf)
df_nmf.columns = topicos['Categoria']

## Pegando principais categorias

lista_top3 = []
for i in nmf_final.index:
    x = nmf_final.loc[i,topicos['Categoria']]
    teste = ','.join(list(x[x > 0.0].sort_values(ascending=False).head(3).index.unique()))
    lista_top3.append(teste)

## dataframe final com id da proposição, mais 3 principai tópicos
df_final = pd.DataFrame({'id':nmf_final['id'],
             'topicos':lista_top3} )
