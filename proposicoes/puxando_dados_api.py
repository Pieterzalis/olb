def proposicoes_api_camara(data):
  """ 
  input: ano
  output: dados de pl, plps, pec e mpv apresentadas em determinado ano
  """
  
  data = str(data)
  url_proposicoes = 'http://dadosabertos.camara.leg.br/arquivos/proposicoes/csv/proposicoes-ano.csv'
  url_ano = url_proposicoes.replace('ano',data)
  resp = requests.get(url_ano).content
  df_ano = pd.read_csv(io.StringIO(resp.decode('utf-8')),sep=';')
  df_ano = df_ano[df_ano['siglaTipo'].isin(['PL','PLP','PEC','MPV'])]
  return df_ano


def tema_proposicao(id_materia):
  """ 
  input: identificador da proposicao legislativa
  output: uma string com os temas da indexacao da camara. No caso de mais de uma a divisão é feita por uma vírgula
  """
  id_materia = str(id_materia)
  url  = 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/materia/temas'
  url = url.replace('materia',id_materia)
  try:
        resp = requests.get(url).json() 
        temas_materia = []
        for i in resp['dados']:
            temas_materia.append(i['tema'])
        return ','.join(temas_materia)
  except:
        return ''

