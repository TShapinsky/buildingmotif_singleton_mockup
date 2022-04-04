import buildingmotif.utilities as utilities


class Template:
    def __init__(self, name) -> None:
        self.name = name
        bm = utilities.get_building_motif()
        bm.sync(self)