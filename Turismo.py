import rpyc
from rpyc.utils.server import ThreadedServer

adicionarPonto = input('Adicionar Novo Ponto Turistico: ')

while adicionarPonto == 'S':
    databaseFile = open('Databases/Turismo.txt', 'a+')
    nomeLocal = input('Nome do Local: ')
    telefoneLocal = input('Telefone: ')
    precoLocal = input('Preço do local: ')
    localizacao = input('Localização: ')

    databaseFile.writelines('{},{},{},{}'.format(
        nomeLocal, telefoneLocal, precoLocal, localizacao))
    databaseFile.close()

    adicionarPonto = input(
        'Inserido com Sucesso. Deseja Inserir outro Local ? ')

databaseFile = open('Databases/Turismo.txt', 'r')

print('Servidor iniciado')

class TurismoService(rpyc.Service):
    def exposed_pesquisaTurismo(self, local):
      message = '\n ====== Locais ======\n'
      for line in databaseFile.readlines():
        campos = line.split(',')
        if campos[3] == local:
          message += 'Local: ' + campos[0] + '\n'
          message += 'Telefone: ' + campos[1] + '\n'
          message += 'Preço: ' + campos[2] + '\n'
          message += 'Localização: ' + campos[3] + '\n'
      
      return message


thread = ThreadedServer(TurismoService, port=35000)
thread.start()
