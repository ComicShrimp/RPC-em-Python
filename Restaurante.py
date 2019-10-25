import rpyc
from rpyc.utils.server import ThreadedServer


class RestauranteService(rpyc.Service):
    def exposed_pesquisaRestaurante(self, dataIda, dataVolta):
        return 'Achou restaurante'


thread = ThreadedServer(RestauranteService, port=35002)
thread.start()