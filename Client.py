import rpyc

turismo = rpyc.connect('localhost', 35000)
hotel = rpyc.connect('localhost', 35001)
restaurante = rpyc.connect('localhost', 35002)
area = rpyc.connect('localhost', 35003)

while True:
  cidade = input('Cidade para consulta (e para sair): ')
  
  if cidade == 'e':
    break

  resultadoTurismo = turismo.root.pesquisaTurismo(cidade)
  resultadoHotel = hotel.root.pesquisaHotel(cidade)
  resultadoRestaurante = restaurante.root.pesquisaRestaurante(cidade)
  resultadoAerea = area.root.pesquisaAerea(cidade)

  print(resultadoTurismo)
  print(resultadoHotel)
  print(resultadoRestaurante)
  print(resultadoAerea)