import rpyc
from rpyc.utils.server import ThreadedServer

adicionarHotel = input('Adicionar Novo Hotel: ')

while adicionarHotel == 'S':
    databaseFile = open('Databases/Hotel.txt', 'a+')
    nomeLocal = input('Nome do Local: ')
    telefoneLocal = input('Telefone: ')
    precoLocal = input('Preço do local: ')
    cidade = input('Cidade: ')
    localizacao = input('Localização: ')

    databaseFile.writelines('{},{},{},{},{}\n'.format(
        nomeLocal, telefoneLocal, precoLocal, cidade, localizacao))
    databaseFile.close()

    adicionarHotel = input(
        'Inserido com Sucesso. Deseja Inserir outro Local ? ')

print('Servidor iniciado')


class HotelService(rpyc.Service):
    def exposed_pesquisaHotel(self, local):
        databaseFile = open('Databases/Hotel.txt', 'r')
        print('Nova consulta para ' + local)

        message = '\n ====== Hoteis ======\n'
        for line in databaseFile.readlines():
            campos = line.split(',')
            if campos[3].__contains__(local):
                message += '\nLocal: ' + campos[0] + '\n'
                message += 'Telefone: ' + campos[1] + '\n'
                message += 'Preço: ' + campos[2] + '\n'
                message += 'Localização: ' + campos[4] + '\n'

        databaseFile.close()
        return message


thread = ThreadedServer(HotelService, port=35001)
thread.start()
