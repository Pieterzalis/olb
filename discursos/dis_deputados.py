import requests
import pandas as pd
import time
import json
import re


def limpando_discurso(discursos_dep,id_dep):
    
    """
    função que retorna um datataframe com as informações básicas dos discursos dos deputados.
    discursos_dep: é um dicionário com os dados da api da Câmara dos deputados
    id_dep: é o id do deputado
    """
    
    discursos = []
    if len(discursos_dep) >= 1:
            for num_dis in range(len(discursos_dep)):
                hora = discursos_dep[num_dis]['dataHoraInicio']
                tipo = discursos_dep[num_dis]['tipoDiscurso']
                keywords = discursos_dep[num_dis]['keywords']
                sumario = discursos_dep[num_dis]['sumario']
                transcricao = discursos_dep[num_dis]['transcricao']
                discursos.append([id_dep,hora,tipo,keywords,sumario,transcricao])
    df = pd.DataFrame(discursos,columns=['Deputado','Data','TipoDiscurso','Palavras-Chaves','Sumario','Transcricao'])
    return df
  
  
  def extraindo_discurso(deputado,inicio,fim):
    
    """
    função que puxa os dados da api da Câmara dos Deputados já limpos num dataframe. Aqui já estamos
    deputado: id do deputado
    inicio: data inicio do período de coleta dos discursos
    fim: data fim do período de coleta dos discursos 
    
    """
    
    url_base = 'https://dadosabertos.camara.leg.br/api/v2/deputados/id_deputado/discursos?dataInicio=periodoinicial&dataFim=periodofinal&itens=100'
    url_deputado = url_base.replace('id_deputado',deputado).replace('periodoinicial',inicio).replace('periodofinal',fim)
    resp = requests.get(url_deputado).json() 
    df_discurso_dep_final = pd.DataFrame()
    for i in resp['links']:
        url_dicurso_dep_paginas = url_deputado+'&pagina=numero'
        if i['rel'] == 'last':
            maximo = int(re.findall('pagina=(.*)&',i['href'])[0])
            for num in range(1,maximo+1):
                url_dicurso_dep_final = url_dicurso_dep_paginas.replace('numero',str(num))
                resp = requests.get(url_dicurso_dep_final).json() 
                df_discurso_dep_parcial = limpando_discurso(resp['dados'],deputado)
                df_discurso_dep_final = pd.concat([df_discurso_dep_parcial,df_discurso_dep_final])
    return df_discurso_dep_final
            
