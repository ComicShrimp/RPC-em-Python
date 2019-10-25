# import rpyc

# conn = rpyc.connect("localhost", 35000)
# x = conn.root.add(4,7)
# print(x)

# try:
#     resultado = conn.root.div(4,2)
#     print(resultado)
# except ZeroDivisionError:
#     pass
import rpyc

connection = rpyc.connect('localhost', 35000)

while True:
  cidade = input('Cidade para consulta (e para sair): ')
  
  if cidade == 'e':
    break

  dataIda = input('Digite a data de ida (DD/MM/AAAA): ')
  dataVolta = input('Digite a data de Volta (DD/MM/AAAA): ')

  resultadoTurismo = connection.root.pesquisaTurismo()
  resultadoHotel = connection.root.pesquisaHotel()
  resultadoRestaurante = connection.root.pesquisaRestaurante()
  resultadoAerea = connection.root.pesquisaAerea()

  print(resultadoTurismo)
  print(resultadoHotel)
  print(resultadoRestaurante)
  print(resultadoAerea)