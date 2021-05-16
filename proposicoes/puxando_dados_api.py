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
