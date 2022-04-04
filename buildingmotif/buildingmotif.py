from buildingmotif.singleton import Singleton
class BuildingMOTIF(metaclass=Singleton):

    def __init__(self, something="unset") -> None:
        self.something=something