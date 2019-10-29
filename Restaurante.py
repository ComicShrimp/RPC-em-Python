import rpyc
from rpyc.utils.server import ThreadedServer

adicionarRestaurante = input('Adicionar Novo Restaurante : ')

while adicionarRestaurante == 'S':
    databaseFile = open('Databases/Restaurante.txt', 'a+')
    nomeLocal = input('Nome do Local: ')
    telefoneLocal = input('Telefone: ')
    precoLocal = input('Preço do local: ')
    cidade = input('Cidade: ')
    localizacao = input('Localização: ')

    databaseFile.writelines('{},{},{},{},{}\n'.format(
        nomeLocal, telefoneLocal, precoLocal, cidade, localizacao))
    databaseFile.close()

    adicionarRestaurante = input(
        'Inserido com Sucesso. Deseja Inserir outro Local ? ')

print('Servidor iniciado')


class RestauranteService(rpyc.Service):
    def exposed_pesquisaRestaurante(self, local):
        databaseFile = open('Databases/Restaurante.txt', 'r')
        print('Nova consulta para ' + local)

        message = '\n ====== Restaurantes ======\n'
        for line in databaseFile.readlines():
            campos = line.split(',')
            if campos[3].__contains__(local):
                message += '\nLocal: ' + campos[0] + '\n'
                message += 'Telefone: ' + campos[1] + '\n'
                message += 'Preço: ' + campos[2] + '\n'
                message += 'Localização: ' + campos[4] + '\n'

        databaseFile.close()
        return message


thread = ThreadedServer(RestauranteService, port=35002)
thread.start()
