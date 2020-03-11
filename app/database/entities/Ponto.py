class Ponto:
    def __init__(self):
        self._cod = None
        self._nome = None
        self._lat = None
        self._lng = None
        self._id = None
    
    def toDict(self):
        return {
            "cod":self._cod,
            "nome":self._nome,
            "lat":float(self._lat),
            "lng":float(self._lng),
            "id":self._id
        }
   
    @staticmethod
    def toObj(dict):
        ponto = Ponto()

        ponto.cod = dict['cod']
        ponto.nome = dict['nome']
        ponto.lat = dict['lat']
        ponto.lng = dict['lng']
        ponto.id = dict['id']

        return ponto
        
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def cod(self):
        return self._cod

    @cod.setter
    def cod(self, cod):
        self._cod = cod

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, lat):
        self._lat = lat

    @property
    def lng(self):
        return self._lng

    @lng.setter
    def lng(self, lng):
        self._lng = lng
