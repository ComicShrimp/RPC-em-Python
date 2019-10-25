import rpyc
from rpyc.utils.server import ThreadedServer


class TurismoService(rpyc.Service):
    def exposed_pesquisaTurismo(self, dataIda, dataVolta):
        return 'Achou Turismo'


thread = ThreadedServer(TurismoService, port=35000)
thread.start()
