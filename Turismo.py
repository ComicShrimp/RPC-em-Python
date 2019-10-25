import rpyc
from rpyc.utils.server import ThreadedServer

print('Servidor iniciado')


class TurismoService(rpyc.Service):
    def exposed_pesquisaTurismo(self, local):
        return 'Turismo'


thread = ThreadedServer(TurismoService, port=35000)
thread.start()
