import rpyc
from rpyc.utils.server import ThreadedServer


class AereaService(rpyc.Service):
    def exposed_pesquisaAerea(self, dataIda, dataVolta):
        return 'Achou Hotel'


thread = ThreadedServer(AereaService, port=35000)
thread.start()