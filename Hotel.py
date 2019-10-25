import rpyc
from rpyc.utils.server import ThreadedServer


class HotelService(rpyc.Service):
    def exposed_pesquisaHotel(self, dataIda, dataVolta):
        return 'Achou Hotel'


thread = ThreadedServer(HotelService, port=35000)
thread.start()