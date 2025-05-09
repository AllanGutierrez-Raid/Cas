class casa():
    def __init__(self,ventanas,puertas,techo,direccion,habitaciones,pisos):
        self.__vent = ventanas
        self.__puertas = puertas
        self.__techo = techo
        self.__dir = direccion
        self.__hab = habitaciones
        self.__pisos = pisos

    @property
    def _vent(self):
        return self.__vent

    @_vent.setter
    def _vent(self, value):
        self.__vent = value

    @property
    def _puertas(self):
        return self.__puertas

    @_puertas.setter
    def _puertas(self, value):
        self.__puertas = value

    @property
    def _techo(self):
        return self.__techo

    @_techo.setter
    def _techo(self, value):
        self.__techo = value

    @property
    def _dir(self):
        return self.__dir

    @_dir.setter
    def _dir(self, value):
        self.__dir = value

    @property
    def _hab(self):
        return self.__hab

    @_hab.setter
    def _hab(self, value):
        self.__hab = value

    @property
    def _pisos(self):
        return self.__pisos

    @_pisos.setter
    def _pisos(self, value):
        self.__pisos = value

class Vivienda_Familiar(casa):
    def __init__(self, ventanas, puertas, techo, direccion, habitaciones, pisos,tamFam,patio):
        super().__init__(ventanas, puertas, techo, direccion, habitaciones, pisos)
        self.__tamFam = tamFam
        self.__patio = patio

    @property
    def _tamFam(self):
        return self.__tamFam

    @_tamFam.setter
    def _tamFam(self, value):
        self.__tamFam = value

    @property
    def _patio(self):
        return self.__patio

    @_patio.setter
    def _patio(self, value):
        self.__patio = value


class Apartamento(casa):
    def __init__(self, ventanas, puertas, techo, direccion, habitaciones,pisos,numAp,nivelpiso):
        super().__init__(ventanas, puertas, techo, direccion, habitaciones, pisos)
        self.__numAp = numAp
        self.__nivPi = nivelpiso

    @property
    def _numAp(self):
        return self.__numAp

    @_numAp.setter
    def _numAp(self, value):
        self.__numAp = value

    @property
    def _nivPi(self):
        return self.__nivPi

    @_nivPi.setter
    def _nivPi(self, value):
        self.__nivPi = value


class Bongalo(casa):
    def __init__(self, ventanas, puertas, techo, direccion, habitaciones, pisos,tamañoy,tamañox):
        super().__init__(ventanas, puertas, techo, direccion, habitaciones, pisos)
        self.__tamy = tamañoy
        self.__tamx = tamañox
    

    @property
    def _tamy(self):
        return self.__tamy

    @_tamy.setter
    def _tamy(self, value):
        self.__tamy = value

    @property
    def _tamx(self):
        return self.__tamx

    @_tamx.setter
    def _tamx(self, value):
        self.__tamx = value

