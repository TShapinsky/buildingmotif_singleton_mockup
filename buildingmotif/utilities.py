import buildingmotif.singleton as singleton
import buildingmotif.buildingmotif as buildingmotif

def get_building_motif():
    if hasattr(buildingmotif.BuildingMOTIF,"instance"):
        return buildingmotif.BuildingMOTIF.instance
    raise singleton.SingletonNotInstantiatedException