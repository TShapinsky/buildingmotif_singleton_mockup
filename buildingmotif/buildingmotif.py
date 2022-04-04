import buildingmotif.singleton as singleton
import buildingmotif.template as template
import buildingmotif.template_library as template_library
class BuildingMOTIF(metaclass=singleton.Singleton):

    def __init__(self, something="unset") -> None:
        self.something=something

    def sync(self, obj):
        klazz = type(obj)
        if klazz is template.Template:
            print(f"syncing template: {obj.name}")
        elif klazz is template_library.TemplateLibrary:
            print(f"syncing template library: {obj.name}")