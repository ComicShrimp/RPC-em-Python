import rpyc
from rpyc.utils.server import ThreadedServer
import sqlite3

connect = sqlite3.connect('Databases/turismo.db', check_same_thread=False)
cursor = connect.cursor()

criaTabela = input('Criar Tabela (S/N): ')
if criaTabela == 'S':
    cursor.execute("""
  CREATE TABLE turismo (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        preco TEXT,
        localizacao text
  )
  """)
    print('Tabela Criada Com sucesso')

adicionarTurismo = input('Adicionar Mais um Ponto Turistico: ')

while adicionarTurismo == 'S':
    nomeLocal = input('Nome do Local: ')
    telefoneLocal = input('Telefone: ')
    precoLocal = input('Preço do local: ')
    localizacao = input('Localização: ')

    cursor.execute('INSERT INTO turismo (nome, telefone, preco, localizacao) VALUES (?, ?, ?, ?)',
                   (nomeLocal, telefoneLocal, precoLocal, localizacao.upper()))

    connect.commit()
    adicionarTurismo = input(
        'Inserido com Sucesso. Deseja Inserir outro Local ? ')

print('Servidor iniciado')


class TurismoService(rpyc.Service):
    def exposed_pesquisaTurismo(self, local):
        cursor.execute(
            """SELECT * FROM turismo WHERE localizacao = ?""", (local,))

        stringDeLocais = 'Locais em ' + local + '\n'
        for linha in cursor.fetchall():
            print(linha)
            stringDeLocais += '\n ========= \n'
            stringDeLocais += 'Nome: ' + linha[1] + '\n'
            stringDeLocais += 'Telefone: ' + linha[2] + '\n'
            stringDeLocais += 'Preço: ' + linha[3] + '\n'
            stringDeLocais += ' ========= \n'

        return stringDeLocais


thread = ThreadedServer(TurismoService, port=35000)
thread.start()
