import rpyc
from rpyc.utils.server import ThreadedServer

adicionarPonto = input('Adicionar Novo Ponto Turistico: ')

while adicionarPonto == 'S':
    databaseFile = open('Databases/Turismo.txt', 'a+')
    nomeLocal = input('Nome do Local: ')
    telefoneLocal = input('Telefone: ')
    precoLocal = input('Preço do local: ')
    cidade = input('Cidade: ')
    localizacao = input('Localização: ')

    databaseFile.writelines('{},{},{},{},{}\n'.format(
        nomeLocal, telefoneLocal, precoLocal, cidade, localizacao))
    databaseFile.close()

    adicionarPonto = input(
        'Inserido com Sucesso. Deseja Inserir outro Local ? ')

print('Servidor iniciado')

class TurismoService(rpyc.Service):
    def exposed_pesquisaTurismo(self, local):
      databaseFile = open('Databases/Turismo.txt', 'r')
      print('Nova consulta para ' + local)

      message = '\n ====== Pontos Turisticos ======\n'
      for line in databaseFile.readlines():
        campos = line.split(',')
        if campos[3].__contains__(local):
          message += '\nLocal: ' + campos[0] + '\n'
          message += 'Telefone: ' + campos[1] + '\n'
          message += 'Preço: ' + campos[2] + '\n'
          message += 'Localização: ' + campos[4] + '\n'
      
      databaseFile.close()
      return message


thread = ThreadedServer(TurismoService, port=35000)
thread.start()
