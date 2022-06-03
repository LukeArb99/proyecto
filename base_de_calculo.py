from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris
from sympy import true

solar_system_ephemeris.set("jpl")

# from poliastro.bodies import Sun, Earth, Jupiter
import poliastro.bodies as bodies
from poliastro.ephem import Ephem
from poliastro.maneuver import Maneuver
from poliastro.twobody import Orbit
from poliastro.util import time_range

## Orbitas Sistema Solar

class Planeta():
    def __init__(self, nombre, inicio, fin) -> None:
        mi_planeta = getattr(bodies,nombre)
        self.objeto = Ephem.from_body(mi_planeta, time_range(Time(inicio,scale="tdb"), end=Time(fin, scale="tdb"), periods=500))
        r0, v0 = self.objeto.rv(Time(inicio,scale="tdb"))
        self.rF, vF = self.objeto.rv(Time(fin, scale="tdb"))
        
        self.x = self.objeto._coordinates.x.to_value().tolist()
        self.y = self.objeto._coordinates.y.to_value().tolist()
        self.z = self.objeto._coordinates.z.to_value().tolist()
        self.r0 = r0.value.tolist()
        self.rf = self.rF.value.tolist()
    

class Manniobra2():
    def __init__(self) -> None:
        pass

    def lambert(self, nombre1, nombre2, inicio, fin):
        ss_0 = Orbit.from_ephem(bodies.Sun,Planeta(nombre1, inicio, fin).objeto, Time(inicio,scale='tdb'))
        ss_f = Orbit.from_ephem(bodies.Sun,Planeta(nombre2, inicio, fin).objeto, Time(fin, scale='tdb'))
        man = Maneuver.lambert(ss_0,ss_f)
        self.ic1, ss = ss_0.apply_maneuver(man,intermediate = True)
        self.ic1_end = self.ic1.propagate(Time(fin, scale='tdb'))
        self.coordenadas = self.ic1_end.sample().get_xyz().to_value().tolist()

     