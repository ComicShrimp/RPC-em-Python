import rpyc
from rpyc.utils.server import ThreadedServer

adicionarAerea = input('Adicionar Novo Aerea: ')

while adicionarAerea == 'S':
    databaseFile = open('Databases/Aerea.txt', 'a+')
    nomeLocal = input('Nome da Cia.: ')
    telefoneLocal = input('Telefone: ')
    precoLocal = input('Preço da passagem: ')
    cidade = input('Cidade: ')

    databaseFile.writelines('{},{},{},{}\n'.format(
        nomeLocal, telefoneLocal, precoLocal, cidade))
    databaseFile.close()

    adicionarAerea = input(
        'Inserido com Sucesso. Deseja Inserir outro Local ? ')

print('Servidor iniciado')


class AereaService(rpyc.Service):
    def exposed_pesquisaAerea(self, local):
        databaseFile = open('Databases/Aerea.txt', 'r')
        print('Nova consulta para ' + local)

        message = '\n ====== CIA Aerea ======\n'
        for line in databaseFile.readlines():
            campos = line.split(',')
            if campos[3].__contains__(local):
                message += '\nCIA: ' + campos[0] + '\n'
                message += 'Telefone: ' + campos[1] + '\n'
                message += 'Preço: ' + campos[2] + '\n'

        databaseFile.close()
        return message


thread = ThreadedServer(AereaService, port=35003)
thread.start()
