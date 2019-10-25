import rpyc

turismo = rpyc.connect('localhost', 35000)
#hotel = rpyc.connect('localhost', 35001)
#restaurante = rpyc.connect('localhost', 35002)
#area = rpyc.connect('localhost', 35003)

while True:
  cidade = input('Cidade para consulta (e para sair): ')
  
  if cidade == 'e':
    break

  dataIda = input('Digite a data de ida (DD/MM/AAAA): ')
  dataVolta = input('Digite a data de Volta (DD/MM/AAAA): ')

  resultadoTurismo = turismo.root.pesquisaTurismo(cidade)
  #resultadoHotel = hotel.root.pesquisaHotel(1, 2)
  #resultadoRestaurante = restaurante.root.pesquisaRestaurante(1, 2)
  #resultadoAerea = area.root.pesquisaAerea(1, 2)

  print(resultadoTurismo)
  #print(resultadoHotel)
  #print(resultadoRestaurante)
  #print(resultadoAerea)