import buildingmotif.utilities as utilities
import buildingmotif.template as template
class TemplateLibrary:
    def __init__(self, name):
        self.templates = []
        self.name = name
        bm = utilities.get_building_motif()
        bm.sync(self)

    def add(self, template: template.Template):
        print(f"adding template: {template.name}")
        self.templates.append(template)
        bm = utilities.get_building_motif()
        bm.sync(self)