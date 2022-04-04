from buildingmotif.buildingmotif import BuildingMOTIF
from buildingmotif.singleton import SingletonNotInstantiatedException

def get_building_motif():
    if hasattr(BuildingMOTIF,"instance"):
        return BuildingMOTIF.instance
    raise SingletonNotInstantiatedException